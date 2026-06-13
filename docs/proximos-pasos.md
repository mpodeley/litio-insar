# Próximos pasos

## Fase 1 — Hombre Muerto (en curso)

- [ ] **Fijar track** con `01_search.py` y refinar el bounding box / punto Fénix contra imagen satelital.
- [ ] **Correr la cadena** Sentinel-1 → HyP3 → MintPy y publicar el mapa de velocidad + slider.
- [ ] **Digitalizar piletas** de evaporación → `pipeline/overlay.geojson`.
- [ ] **Cruce producción ↔ subsidencia**: serie anual de LCE (reportes de la matriz / Secretaría de Minería)
  contra la evolución del bowl.

## Fase 2 — Salar opaco (China)

- [ ] Replicar el pipeline en Qarhan/Golmud o Zabuye y **comparar** magnitud/evolución con el caso público.

## Mejoras metodológicas

- **Descomposición vertical / E-O**: sumar un track de la **órbita opuesta** (ascendente + descendente) para
  separar el hundimiento vertical del desplazamiento horizontal.
- **Validación de campo**: comparar con **GNSS** o nivelación si hubiera datos públicos en la zona.
- **Dato hidrogeológico**: niveles **piezométricos** para confirmar la caída del nivel freático (requiere
  datos institucionales, habitualmente no públicos).
- **Serie más larga**: extender hacia 2017–2018 (inicio de Sentinel-1) para capturar más expansión.

## Spinoff hermano: open-pit por DEM-differencing

El volumen de material removido en una **mina a cielo abierto** **no** se mide bien con InSAR (la mina activa
decorrelaciona la fase y los cambios son de decenas de metros). Ese caso se aborda en un **repo aparte**
(`mineria-dem`) con **diferencia de modelos de elevación (DEM)** entre fechas → m³ excavados, reutilizando
la estructura de sitio y la narrativa de este proyecto pero **no** la cadena HyP3/MintPy.
