# Referencias

## Subsidencia por extracción de salmuera de litio (caso análogo clave)

- **[Atacama / brine InSAR]** *Land Subsidence and Lithium Brine Pumping: Deformation Analysis Using InSAR
  Time Series in the Salar de Atacama Basin, Chile* (Delgado et al.) — AGU Fall Meeting 2023. Subsidencia junto
  a los pozos de salmuera, asociada a una caída de ~10 m del nivel freático. **Multi-sensor**: Sentinel-1
  (banda C, ~4 cm LOS), ALOS-2 y SAOCOM (banda L, ~2,5 cm) y PAZ (banda X, ~1,5 cm) — es decir, **la banda C
  detectó la señal** sobre el núcleo de halita estable.
  [agu.confex.com](https://agu.confex.com/agu/fm23/meetingapp.cgi/Paper/1373511) ·
  [Delgado, research](https://fdelgadodelapuente.github.io/research/h2o/)
- **[PAZ / ESA]** *PAZ reveals how lithium extraction causes sinking land* — ESA Earth Online (resumen
  divulgativo del caso Atacama). [earth.esa.int](https://earth.esa.int/eogateway/success-story/paz-reveals-how-lithium-extraction-causes-sinking-land)

## Subsidencia por extracción de agua subterránea (InSAR)

- **[Fenhe 2025]** Land subsidence in the Fenhe River Basin (China), Sentinel-1: hasta 81 mm/año, ciclos
  estacionales sincrónicos con el nivel freático. [Springer](https://link.springer.com/article/10.1007/s11069-025-07582-9)
- **[Ardabil 2022]** Land subsidence by groundwater withdrawal, Ardabil Plain (Irán), Sentinel-1.
  [Scientific Reports](https://www.nature.com/articles/s41598-022-17438-y)
- **[Aguascalientes 2021]** Structurally-controlled subsidence by groundwater exploitation, Aguascalientes
  Valley (México). [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0034425720306271)

## Software y procesamiento

- **[Yunjun 2019]** Yunjun, Fattahi & Amelung (2019), *Computers & Geosciences* — **MintPy**, software de
  series de tiempo InSAR. [doi:10.1016/j.cageo.2019.104331](https://doi.org/10.1016/j.cageo.2019.104331)
- **[Morishita 2020]** Morishita et al. (2020), *Remote Sensing* 12(3):424 — **LiCSBAS** (open-source).
  [mdpi.com](https://www.mdpi.com/2072-4292/12/3/424)
- **ASF HyP3** — procesamiento Sentinel-1 InSAR on-demand en la nube. [hyp3-docs.asf.alaska.edu](https://hyp3-docs.asf.alaska.edu)
- **PyAPS / ERA5** — corrección troposférica con reanálisis ECMWF. [Copernicus CDS](https://cds.climate.copernicus.eu)

## Datos satelitales

- **Sentinel-1** (ESA Copernicus), distribuido por **Alaska Satellite Facility (ASF)**.
- **Sentinel-2** (óptico) — digitalización y datación de las piletas de evaporación.

## Operación, producción y catastro (Hombre Muerto)

- **Operador**: Minera del Altiplano S.A. (proyecto **Fénix**); matriz Livent → **Arcadium Lithium** (2024) →
  **Rio Tinto** (2025). Producción en los reportes públicos de la matriz.
- **Mining Data Online / NS Energy** — fichas técnicas del proyecto Fénix (capacidad, método).
  [miningdataonline.com](https://miningdataonline.com/property/2113/Fenix-Salar-del-Hombre-Muerto-Mine.aspx)
- **Secretaría de Minería de la Nación** (Argentina) y **catastro minero** (SEGEMAR / Catamarca) — concesiones
  y producción declarada (disponibilidad de polígonos a verificar).

## Caso opaco (China)

- Cobertura de prensa/empresas sobre producción en **Qarhan/Golmud (Qinghai)** y **Zabuye (Tíbet)**: cifras
  agregadas anunciadas por medios estatales (p. ej. Qinghai CITIC Guoan, Tibet Mineral Development), sin
  caudales ni pozos por sitio.

---

!!! note
    El caso de Atacama es **precedente revisado** de que la subsidencia por bombeo de salmuera es detectable
    con Sentinel-1; sostiene la viabilidad de este experimento en Hombre Muerto. Cualquier afirmación de
    **causalidad** requiere el cruce con datos hidrológicos ([próximos pasos](proximos-pasos.md)).
