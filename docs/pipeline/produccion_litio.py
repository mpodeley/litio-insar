#!/usr/bin/env python
"""Serie anual de producción de litio (LCE) de Fénix — para el cruce con subsidencia.

Lee produccion_litio.csv (anio, produccion_lce_t, verificado, fuente) y produce
produccion_litio.png: barras de carbonato de litio por año. Más adelante, cuando
exista la serie InSAR, se le superpone la subsidencia acumulada para el cruce
"producción ↔ deformación" (análogo al de Vaca Muerta).

    conda activate insar
    python produccion_litio.py

OJO: las cifras del CSV son PRELIMINARES (de reportes/SEC vía búsqueda) y deben
verificarse contra los filings primarios. La columna `verificado` lo marca.
"""

from __future__ import annotations

import csv
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "produccion_litio.csv"
OUT = HERE / "produccion_litio.png"


def main() -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    años, prod, verif = [], [], []
    for r in rows:
        if not r["produccion_lce_t"]:
            continue
        años.append(int(r["anio"]))
        prod.append(float(r["produccion_lce_t"]) / 1000.0)  # kt LCE
        verif.append(r["verificado"].strip().lower() == "si")

    any_prelim = not all(verif)
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(años, prod, edgecolor="#333", width=0.6)
    # azul lleno = verificado; celeste rayado = preliminar
    for b, v in zip(bars, verif):
        b.set_facecolor("#2166ac" if v else "#9ecae1")
        if not v:
            b.set_hatch("///")
    ax.set_xlabel("Año")
    ax.set_ylabel("Producción de carbonato de litio (kt LCE)")
    ax.set_title("Fénix (Salar del Hombre Muerto) — producción anual de litio",
                 weight="bold", pad=12)
    ax.set_xticks(años)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    if any_prelim:
        fig.text(0.5, 0.005,
                 "Cifras PRELIMINARES (rayadas) — verificar contra filings de la matriz.",
                 ha="center", va="bottom", fontsize=8.5, color="#a33")
        fig.subplots_adjust(bottom=0.13)
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    print(f"Listo → {OUT}  ({len(años)} años)")


if __name__ == "__main__":
    main()
