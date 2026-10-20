# Running the recorder on a cloud VM

The recorder (`arbdata record`) needs to run continuously for weeks so the models can be retrained on 10 ms data. A laptop sleeps, and its network adds latency. A small always-on VM fixes both. Setup takes about 15 minutes.

## Where and what size

- **Region:** close to the exchanges. Bybit's and Binance's matching engines are widely reported to run in AWS Singapore (`ap-southeast-1`) and Tokyo (`ap-northeast-1`) respectively. From your current machine we measured about 8 ms to Bybit and 50 ms to Binance.
  - A Tokyo VM should cut the Binance latency sharply.
  - A Singapore VM keeps Bybit fast.
  - For the latency study, two VMs (one each) are best. For recording alone, one is enough.
  - Check that the exchanges' public market data is reachable from the region you pick. Binance restricts some regions.
- **Size:** 2 vCPU, 2–4 GB RAM, 100 GB disk, Ubuntu 24.04. Recording uses about 1 GB a day. A 1 GB-RAM free-tier machine may struggle with Binance's ~650 messages per second. Check current pricing; a machine like this is usually tens of dollars a month or less.

## Setup

On the VM:

```bash
sudo apt update && sudo apt install -y python3 python3-venv rsync chrony
```

```bash
sudo systemctl enable --now chrony
```

From your laptop, copy the code (not the data):

```bash
rsync -av --exclude data --exclude .venv "/Users/mohnishrawat/Desktop/Techfest 2026/Perceptron Hackathon (Optiver)/" ubuntu@YOUR_VM:/opt/arbdata/
```

On the VM:

```bash
cd /opt/arbdata && python3 -m venv .venv && .venv/bin/pip install -e . websockets certifi numba
```

```bash
cd /opt/arbdata && .venv/bin/python -m arbdata record --minutes 1
```

That one-minute test should print message counts for each topic. Then start it for good:

```bash
sudo cp /opt/arbdata/deploy/arbdata-recorder.service /etc/systemd/system/ && sudo systemctl enable --now arbdata-recorder
```

```bash
journalctl -u arbdata-recorder -f
```

## Getting the data back

From your laptop, pull the recordings into the project. They land where the pipeline expects them:

```bash
rsync -av ubuntu@YOUR_VM:/opt/arbdata/data/raw/bybit_live/ "/Users/mohnishrawat/Desktop/Techfest 2026/Perceptron Hackathon (Optiver)/data/raw/bybit_live/"
```

```bash
rsync -av ubuntu@YOUR_VM:/opt/arbdata/data/raw/binance_live/ "/Users/mohnishrawat/Desktop/Techfest 2026/Perceptron Hackathon (Optiver)/data/raw/binance_live/"
```

Then stop the laptop recorder (`pkill -f "arbdata record"`), so you don't have two copies of the same hours with different receive clocks.

## Checks

- **Clock:** `chronyc tracking` should show an offset well under 1 ms. Receive timestamps are only as good as the clock.
- **Gaps:** disconnects are logged per day in `data/raw/*_live/*/*/*/<date>/events.jsonl`.
- **Feed latency:** `analysis/live_cross_check.py <date>` reports each venue's median and p99 feed latency, the first thing to compare between regions.
