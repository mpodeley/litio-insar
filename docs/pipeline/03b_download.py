#!/usr/bin/env python
"""Descargar los productos HyP3 ya procesados, sin depender del watch del paso 2.

02_submit_hyp3.py encola y espera (watch, 6 h). Si la cola de ASF está saturada y
el watch se agota, los jobs SIGUEN procesándose (viven 14 días en ASF). Este script
busca los jobs por nombre, descarga los SUCCEEDED que falten en ./products y reporta
el estado. Es idempotente: corrélo cuantas veces quieras hasta tener los 177.

    python 03b_download.py            # baja lo que esté listo y muestra el estado
    python 03b_download.py --watch    # espera hasta que terminen y baja todo

Requiere ~/.netrc con Earthdata. Mismo name que 02_submit_hyp3.py.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import hyp3_sdk as sdk

import aoi

NAME = "hombre-muerto-sbas"
DEST = Path(aoi.PRODUCTS_DIR)


def _already(job) -> bool:
    """¿Ya está descargado/expandido este job? (zip o carpeta con el unw)."""
    for f in job.files or []:
        stem = Path(f["filename"]).stem
        if (DEST / f["filename"]).exists() or (DEST / stem).is_dir():
            return True
    return False


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--watch", action="store_true",
                    help="esperar a que terminen todos antes de descargar")
    args = ap.parse_args()

    hyp3 = sdk.HyP3()
    jobs = hyp3.find_jobs(name=NAME)
    print(f"{len(jobs)} jobs '{NAME}': {dict(Counter(j.status_code for j in jobs))}")

    if args.watch:
        print("Esperando a que terminen (puede tardar)…")
        jobs = hyp3.watch(jobs)

    done = jobs.filter_jobs(succeeded=True, running=False, pending=False, failed=False)
    DEST.mkdir(exist_ok=True)
    pend = [j for j in done if not _already(j)]
    print(f"SUCCEEDED: {len(done)} · ya bajados: {len(done) - len(pend)} · a bajar: {len(pend)}")

    n = 0
    for j in pend:
        try:
            j.download_files(DEST)
            n += 1
            if n % 10 == 0:
                print(f"  {n}/{len(pend)} descargados…")
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {j.job_id}: {exc}")
    print(f"Listo: {n} nuevos zips en ./{DEST}. "
          f"Cuando estén los 177, corré 03_timeseries.sh.")


if __name__ == "__main__":
    main()
