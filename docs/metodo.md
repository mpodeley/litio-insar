# Método paso a paso

Todo el procesamiento usa **software libre** y **datos gratuitos**. El pipeline está pensado para correr
en una máquina local (Linux). Los scripts están en
[`docs/pipeline/`](https://github.com/mpodeley/litio-insar/tree/main/docs/pipeline) y son los mismos del
proyecto Vaca Muerta, reparametrizados al salar.

## Qué es InSAR (en una línea)

El **InSAR** (interferometría radar de apertura sintética) compara la **fase** de dos imágenes de radar
tomadas en fechas distintas desde la misma órbita: el desfasaje revela cuánto se movió el suelo en la
**línea de vista** del satélite (LOS), con precisión de **milímetros**. Apilando decenas de imágenes
(*time-series* SBAS) se separa la deformación del ruido. Es la técnica de referencia para subsidencia fina.

## 0. Datos y herramientas

| Pieza | Qué | Fuente |
|---|---|---|
| Imágenes | **Sentinel-1** SLC, banda C, ~revisita 6–12 d | ESA Copernicus / ASF |
| Interferogramas | **ASF HyP3** (procesamiento en la nube, gratis) | [hyp3-docs.asf.alaska.edu](https://hyp3-docs.asf.alaska.edu) |
| Serie de tiempo | **MintPy** (SBAS) | [Yunjun et al. 2019] |
| Atmósfera | **ERA5** (ECMWF) vía PyAPS | Copernicus CDS |
| Búsqueda | `asf_search` | ASF |
| Piletas / concesión | digitalización óptica (Sentinel-2 / OSM) | — |

## 1. Área y track

El AOI cubre el **Salar del Hombre Muerto** y sus piletas de evaporación (bounding box aproximado
lon −67.15 a −66.55, lat −25.65 a −25.05). `01_search.py` lista la cobertura 2019–2026: sobre esta zona hay
**896 escenas SLC**, y el track elegido es el **83 descendente** (433 escenas, cobertura **continua
2019→2026**, la mayor de todas). Ventana **2019–2026** con muestreo **~mensual** para una serie larga a costo
acotado. → `01_search.py`, `aoi.py`.

!!! info "Caso favorable"
    El salar es una superficie de **halita árida sin vegetación**: la coherencia interferométrica es alta y
    el terreno es de los mejores para InSAR. Combinar un track ascendente con uno descendente permitiría
    además **descomponer** la deformación en vertical y este-oeste (ver [próximos pasos](proximos-pasos.md)).

## 2. Interferogramas en la nube (HyP3)

Se arma una **red SBAS** (*Small BAseline Subset*): cada fecha mensual se conecta con las siguientes.
Los pares resultantes se encargan a **HyP3**, que genera los interferogramas gratis en la nube de ASF
(~10 créditos por par, de 8.000/mes gratuitos). → `02_submit_hyp3.py`.

## 3. Serie de tiempo con MintPy

Con los productos descargados, **MintPy** invierte la red SBAS a una serie de tiempo de desplazamiento y una
**velocidad media** (mm/año). Pasos clave (config en `salar.cfg`):

1. **Carga** del stack y recorte al AOI del salar.
2. **Red por coherencia**: se descartan pares de baja coherencia.
3. **Punto de referencia** automático en zona de máxima coherencia.
4. **Inversión SBAS** → serie de tiempo.
5. **Corrección troposférica con ERA5** (PyAPS): quita el retardo atmosférico, el principal ruido en InSAR.
6. **Deramp** + **corrección de error de DEM** + **velocidad**.

→ `03_timeseries.sh`, `salar.cfg`.

## 4. Máscara de calidad

Se conservan solo los pixels con **coherencia temporal alta** (> 0.7). En un salar árido se espera una
cobertura muy buena; las propias piletas con agua/salmuera (que cambian) quedan enmascaradas, lo cual está
bien: la señal de compactación está en el **terreno alrededor** de los pozos.

## 5. Visualización

- `04_export_visual.py` → GeoTIFF de velocidad + overlay sobre satélite (folium) + heatmap.
- `05_timeseries_slider.py` → *slider* temporal de deformación acumulada (Leaflet + base64), con suavizado
  temporal Gaussiano para atenuar el ruido atmosférico residual.
- `point_timeseries.py` → series temporales por zona (subsidencia vs referencia estable) para la
  [interpretación](interpretacion.md).
- Overlay opcional: colocar un `pipeline/overlay.geojson` con las **piletas de evaporación** o la concesión
  para que aparezca sobre los mapas.

!!! warning "Nota técnica (reproducibilidad)"
    Con MintPy 1.6.2 + numpy 2.x hay un bug en la inversión pixel-a-pixel
    (`setting an array element with a sequence`). Se corrige con un patch de una línea
    (`np.asarray(x).item()`) en `ifgram_inversion.py` y `dem_error.py`. Alternativa: `numpy<2`.

## Reproducir

```bash
mamba env create -f pipeline/environment.yml && mamba activate insar
# credenciales: cuenta NASA Earthdata (~/.netrc) + token CDS (~/.cdsapirc)
python pipeline/01_search.py            # elegir track/frame → fijarlo en aoi.py
python pipeline/02_submit_hyp3.py --neighbors 2 --submit
bash   pipeline/03_timeseries.sh        # → velocity.h5
python pipeline/04_export_visual.py
python pipeline/05_timeseries_slider.py
```
