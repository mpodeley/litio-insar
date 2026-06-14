#!/usr/bin/env python
"""Paso 2b — Encolar interferogramas SBAS a HyP3 por MULTI-BURST (track 149 ASC).

Por qué multi-burst y no el track/escena anterior: el track 83 descendente que se
había procesado NO cubre el Salar del Hombre Muerto (su huella corta al sur de
Fénix). El track **149 ascendente** sí cubre el salar + la operación. Para traer
solo el salar (no la escena entera) pedimos 3 bursts IW2 contiguos mergeados:
  149_319881_IW2 (Fénix) · 149_319882_IW2 (centro) · 149_319883_IW2 (playa norte)

Costo: INSAR_ISCE_MULTI_BURST 20x4 con 3 bursts = 1 crédito/par. apply_water_mask
queda en False a propósito (no enmascarar la sal). El plan (fechas mensuales
2014-2026 + pares SBAS + nombres de gránulos) está en burst_plan.json (lo arma
01b_search_bursts / la sesión).

    conda activate insar
    cd docs/pipeline
    python 02b_submit_bursts.py            # dry-run (cuenta pares/créditos)
    python 02b_submit_bursts.py --submit   # encola de verdad (gasta créditos)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import hyp3_sdk as sdk

HERE = Path(__file__).parent
PLAN = HERE / "burst_plan.json"
BATCH_OUT = HERE / "burst_jobs.json"   # IDs de los jobs encolados (para descargar luego)
LOOKS = "20x4"                          # 80 m, 1 crédito/par con 3 bursts
NAME = "shm149"


def prepared_jobs(plan: dict) -> list[dict]:
    bursts = plan["bursts"]
    gr = plan["granules"]
    jobs = []
    for d1, d2 in plan["pairs"]:
        ref = [gr[d1][b] for b in bursts]   # mismo orden de bursts en ref y sec
        sec = [gr[d2][b] for b in bursts]
        jobs.append(
            sdk.HyP3.prepare_insar_isce_multi_burst_job(
                reference=ref, secondary=sec,
                name=f"{NAME}_{d1}_{d2}".replace("-", ""),
                apply_water_mask=False, looks=LOOKS,
            )
        )
    return jobs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--submit", action="store_true", help="encolar de verdad")
    ap.add_argument("--test", type=int, default=2, help="cuántos pares de prueba primero")
    args = ap.parse_args()

    plan = json.loads(PLAN.read_text())
    jobs = prepared_jobs(plan)
    print(f"fechas: {len(plan['dates'])} | pares: {len(plan['pairs'])} | "
          f"looks {LOOKS} | créditos estimados: {len(jobs)}")

    if not args.submit:
        print("dry-run (sin encolar). Agregá --submit para enviar.")
        return

    h = sdk.HyP3()
    print(f"créditos disponibles: {h.check_credits()}")

    # 1) lote de prueba (validación de aceptación inmediata)
    test = jobs[: args.test]
    print(f"==> encolando {len(test)} pares de prueba…")
    b_test = h.submit_prepared_jobs(test)
    print(f"    aceptados: {len(b_test)} (ej. {b_test[0].job_id})")

    # 2) el resto, en chunks de 200
    rest = jobs[args.test:]
    batch = b_test
    for i in range(0, len(rest), 200):
        chunk = rest[i:i + 200]
        print(f"==> encolando {len(chunk)} (resto {i}+)…")
        batch += h.submit_prepared_jobs(chunk)
    print(f"TOTAL encolados: {len(batch)}")

    BATCH_OUT.write_text(json.dumps([j.job_id for j in batch]))
    print(f"IDs guardados en {BATCH_OUT.name}. Descargá con 03b_download.py cuando terminen.")


if __name__ == "__main__":
    main()
