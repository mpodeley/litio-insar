# Caso opaco (China)

El segundo acto del experimento: aplicar **exactamente el mismo método** a un salar donde **no hay datos
operativos públicos finos** (caudales de bombeo, ubicación de pozos, producción por sitio). Ahí el satélite
deja de ser una verificación del dato oficial y pasa a ser **la única fuente independiente**: la huella de
subsidencia revela la intensidad de la extracción que el reporte no transparenta.

## Candidatos

| Salar | Ubicación | Notas |
|---|---|---|
| **Qarhan / Golmud** | Qinghai, China | Uno de los mayores polos de litio de salmuera; nuevas plantas en producción (2025). Piletas de evaporación de escala enorme. |
| **Zabuye** | Tíbet (Shigatse), China | Reservas entre las mayores del mundo; producción de carbonato de litio iniciada formalmente en 2025. |

La producción se anuncia por **medios estatales y notas de empresas** (p. ej. Qinghai CITIC Guoan, Tibet
Mineral Development), pero **sin** caudales ni pozos a nivel de sitio. Tampoco hay catastro de concesiones
público comparable al argentino.

## Cómo se adapta el método

- **Pipeline InSAR idéntico**: solo cambian el bounding box y el track en `aoi.py` y el subset en `salar.cfg`.
  La cadena Sentinel-1 → HyP3 → MintPy es agnóstica al lugar.
- **Sin concesiones**: en lugar de polígonos oficiales, se digitalizan las **piletas de evaporación** desde
  Sentinel-2 (muy visibles) → `pipeline/overlay.geojson`. Son el proxy de la huella operativa.
- **Sin producción por sitio**: se usan solo **cifras agregadas** (capacidad anunciada por provincia/empresa)
  como contexto. El peso del análisis recae en la **deformación medida** y en la **expansión de piletas**
  vista en óptico.

## Estado

!!! warning "Fase 2 del proyecto"
    Este caso arranca **después** de validar el pipeline end-to-end en
    [Hombre Muerto](salar-publico.md). Tareas previstas:

    - [ ] Elegir un salar y su AOI (Qarhan/Golmud o Zabuye).
    - [ ] Correr la cadena InSAR (mismo `pipeline/`).
    - [ ] Digitalizar piletas y datar su expansión con Sentinel-2.
    - [ ] Comparar la magnitud y evolución de la subsidencia con el caso público.
