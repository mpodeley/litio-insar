"""AOI y config — Salar del Hombre Muerto (Catamarca/Salta, Argentina), serie 2019–2026.

Subsidencia por extracción de salmuera de litio: el bombeo baja el nivel freático
más rápido que la recarga y el terreno se compacta (mismo mecanismo validado por
InSAR en el Salar de Atacama, Chile). Zona árida de halita → alta coherencia
interferométrica, caso favorable para Sentinel-1/SBAS.

NOTA: el AOI está ACOTADO a la subcuenca OCCIDENTAL del salar — la que opera Fénix
(wellfield + piletas al sur + lomas estables al SO que sirven de referencia). La
caja ancha previa (lon −67.15…−66.55) quedaba descentrada: su centro caía sobre la
playa abierta y la subcuenca oriental (lado Sal de Vida), dejando la operación de
Fénix pegada al borde oeste y casi todos los píxeles fuera del objetivo. El bombeo
ocurre cerca del centro de la subcuenca occidental (0–40 m) y las piletas ~13 km al
sur del centro de la playa. El track/frame se fijó con 01_search.py.
"""

from __future__ import annotations

# --- Bounding box (lon/lat) acotado a la subcuenca occidental de Fénix ---
WEST = -67.20
SOUTH = -25.55
EAST = -66.95
NORTH = -25.30

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
