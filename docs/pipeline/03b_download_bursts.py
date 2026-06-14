#!/usr/bin/env python
"""Descargar los productos HyP3 multi-burst (track 149, Hombre Muerto) por IDs.

Lee los job_id encolados por 02b_submit_bursts.py (burst_jobs.json), baja los
SUCCEEDED que falten a ./products149 y reporta estado. Idempotente.

    python 03b_download_bursts.py            # baja lo listo y muestra estado (1 pasada)
    python 03b_download_bursts.py --loop     # poll cada 20 min, baja a medida que terminan,
                                             # sale cuando no quedan PENDING/RUNNING
Requiere ~/.netrc con Earthdata.
"""
from __future__ import annotations

import argparse
import json
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import hyp3_sdk as sdk

HERE = Path(__file__).parent
IDS = HERE / "burst_jobs.json"
DEST = HERE / "products149"
# Fecha de encolado (para acotar find_jobs, que es paginado y rápido vs get_job_by_id x402)
SUBMIT_DAY = datetime(2026, 6, 14, tzinfo=timezone.utc)


def _already(job) -> bool:
    for f in job.files or []:
        stem = Path(f["filename"]).stem
        if (DEST / f["filename"]).exists() or (DEST / stem).is_dir():
            return True
    return False


def _refresh(hyp3, ids):
    idset = set(ids)
    jobs = hyp3.find_jobs(start=SUBMIT_DAY, job_type="INSAR_ISCE_MULTI_BURST")
    return sdk.Batch([j for j in jobs if j.job_id in idset])


def _download(jobs):
    DEST.mkdir(exist_ok=True)
    done = [j for j in jobs if j.succeeded()]
    pend = [j for j in done if not _already(j)]
    n = 0
    for j in pend:
        try:
            j.download_files(DEST)
            n += 1
            if n % 20 == 0:
                print(f"  {n}/{len(pend)} descargados…", flush=True)
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {j.job_id}: {exc}", flush=True)
    return n, len(done)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--loop", action="store_true", help="poll cada 20 min hasta terminar")
    args = ap.parse_args()

    ids = json.loads(IDS.read_text())
    hyp3 = sdk.HyP3()
    print(f"{len(ids)} jobs multi-burst (track 149).", flush=True)

    while True:
        jobs = _refresh(hyp3, ids)
        st = Counter(j.status_code for j in jobs)
        n, ndone = _download(jobs)
        print(f"estado: {dict(st)} · descargados nuevos: {n} · en ./products149: "
              f"{len(list(DEST.glob('*/*_unw_phase.tif'))) if DEST.exists() else 0}", flush=True)
        running = st.get("PENDING", 0) + st.get("RUNNING", 0)
        if not args.loop or running == 0:
            break
        print(f"  quedan {running} en proceso; reviso en 20 min…", flush=True)
        time.sleep(1200)

    print("Listo. Cuando estén todos, corré: smallbaselineApp.py salar149.cfg", flush=True)


if __name__ == "__main__":
    main()
