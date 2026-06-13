"""AOI y config — Salar del Hombre Muerto (Catamarca/Salta, Argentina), serie 2019–2026.

Subsidencia por extracción de salmuera de litio: el bombeo baja el nivel freático
más rápido que la recarga y el terreno se compacta (mismo mecanismo validado por
InSAR en el Salar de Atacama, Chile). Zona árida de halita → alta coherencia
interferométrica, caso favorable para Sentinel-1/SBAS.

NOTA: el bounding box y el punto de referencia son APROXIMADOS (centrados en el
salar y las piletas de evaporación de Fénix / Minera del Altiplano). Refinar tras
correr 01_search.py y mirar la imagen satelital. El track/frame queda en None
hasta elegirlo con 01_search.py (la búsqueda usa solo el polígono).
"""

from __future__ import annotations

# --- Bounding box (lon/lat) cubriendo el salar y las piletas de evaporación ---
WEST = -67.15
SOUTH = -25.65
EAST = -66.55
NORTH = -25.05

# --- Referencia (lat, lon): centroide del polígono "Proyecto Fenix" de OSM (overlay_osm.py) ---
FENIX = (-25.49, -67.10)

# --- Ventana temporal: serie larga hasta el presente ---
START = "2019-01-01"
END = "2026-06-30"

# --- Track / frame (01_search.py): track 83 DESCENDENTE, 433 escenas continuas 2019→2026
# (el de mayor cobertura sobre el salar). FRAME=None → todos los frames del track sobre el AOI. ---
RELATIVE_ORBIT: int | None = 83
FRAME: int | None = None

# Muestreo ~mensual (1 escena por mes) para acotar jobs/créditos en la serie larga.
MONTHLY = True

PRODUCTS_DIR = "products"


def polygon_wkt() -> str:
    return (
        f"POLYGON(({WEST} {SOUTH},{EAST} {SOUTH},"
        f"{EAST} {NORTH},{WEST} {NORTH},{WEST} {SOUTH}))"
    )


def center_lonlat() -> tuple[float, float]:
    return ((WEST + EAST) / 2.0, (SOUTH + NORTH) / 2.0)
