# Próximos pasos

## Fase 1 — Hombre Muerto

- [x] **Corregir el track**: el 83 descendente **no cubre el salar** → se usa el **149 ascendente** (ver
  [Resultados](resultados.md)).
- [x] **Re-pedir multi-burst** centrado en la operación (402 ifgs, 2014–2026) → MintPy + ERA5:
  **~85 % de coherencia**, 100 % sobre Fénix.
- [x] **Digitalizar piletas** de evaporación → `overlay.geojson` (OSM).
- [x] **Extraer la señal acumulada** por zona (~15–30 mm 2014–2026) — emerge tras doble diferencia.
- [ ] **Bajar el piso de ruido atmosférico** (es el límite actual, no la coherencia):
    - **GACOS** — corrección troposférica más fina que ERA5 (gratis; pedido y config listos —
      `salar149_gacos.cfg`).
    - **Banda L: SAOCOM** (CONAE, argentino) o **NISAR** (NASA, abierto desde 2025) — la palanca de fondo.
    - Pasos para conseguir cada dato: **[`COMO_PEDIR_DATOS.md`](https://github.com/mpodeley/litio-insar/blob/main/docs/pipeline/COMO_PEDIR_DATOS.md)**.
- [ ] **Confirmar el signo** (subsidencia vs uplift relativo) y separar subzonas (extracción vs piletas).
- [ ] **Cruce producción ↔ deformación** (curva de LCE) — completar/verificar la serie de producción.

## Fase 2 — Salar opaco (China)

- [ ] Replicar el pipeline en Qarhan/Golmud o Zabuye y **comparar** magnitud/evolución con el caso público.

## Mejoras metodológicas

- **Descomposición vertical / E-O**: sumar un track de la **órbita opuesta** (ascendente + descendente) para
  separar el hundimiento vertical del desplazamiento horizontal.
- **Validación de campo**: comparar con **GNSS** o nivelación si hubiera datos públicos en la zona.
- **Dato hidrogeológico**: niveles **piezométricos** para confirmar la caída del nivel freático (requiere
  datos institucionales, habitualmente no públicos).
- **Filtrado de APS**: tras GACOS, evaluar filtrado espacio-temporal del retardo turbulento residual.

## Spinoff hermano: open-pit por DEM-differencing

El volumen de material removido en una **mina a cielo abierto** **no** se mide bien con InSAR (la mina activa
decorrelaciona la fase y los cambios son de decenas de metros). Ese caso se aborda en un **repo aparte**
(`mineria-dem`) con **diferencia de modelos de elevación (DEM)** entre fechas → m³ excavados, reutilizando
la estructura de sitio y la narrativa de este proyecto pero **no** la cadena HyP3/MintPy.
