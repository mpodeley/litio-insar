# Próximos pasos

## Fase 1 — Hombre Muerto (corrida hecha)

- [x] **Fijar track** (83 descendente) y AOI / punto Fénix.
- [x] **Correr la cadena** Sentinel-1 → HyP3 → MintPy (136 ifgs, ERA5) → **resultado: baja coherencia sobre el
  salar** (ver [Resultados](resultados.md)).
- [x] **Digitalizar piletas** de evaporación → `overlay.geojson` (OSM).
- [ ] **Capturar la deformación del wellfield** — la prioridad real, dado el resultado:
    - **Banda L: SAOCOM** (CONAE, argentino, cubre Hombre Muerto) o **ALOS-2** — mantienen coherencia sobre
      superficies cambiantes mucho mejor que la banda C (en Atacama, la L midió ~2,5 cm).
    - O reprocesar en **banda C** enfocando el **núcleo de halita** (otro track, umbrales, PSI) — Atacama
      muestra que se puede.
- [ ] **Cruce producción ↔ subsidencia** (curva de LCE ya lista) una vez que haya señal coherente sobre los pozos.

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
