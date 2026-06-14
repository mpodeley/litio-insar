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

El AOI cubre el **Salar del Hombre Muerto** y la operación de Fénix (bounding box lon −67.25 a −66.85,
lat −25.50 a −25.12). El **track** correcto es el **149 ascendente** (frames 1093/1094): su huella contiene el
salar y la operación, con archivo Sentinel-1 **desde 2014-10 hasta 2026** (447 fechas). → `aoi.py`,
`02b_submit_bursts.py`.

!!! danger "La trampa del track (corregida)"
    Una primera corrida usó el **track 83 descendente** — y dio "resultado nulo". Pero el 83 **no cubre el
    salar**: su huella (paralelogramo inclinado de la pasada) corta al sur de Fénix, así que lo procesado era
    **terreno al sur del salar**. La coherencia/amplitud daban exactamente cero sobre la operación porque
    **no había dato** ahí, no por decorrelación. Se había elegido el 83 por maximizar cobertura de un AOI
    previo demasiado extendido al sur. **Lección**: verificar que la huella del dato cubra el objetivo
    (lo confirmamos contra imagen satelital) antes de interpretar.

!!! info "Multi-burst: traer sólo el salar"
    En vez de la escena entera, se pidieron **3 *bursts* IW2 contiguos mergeados** (HyP3
    `INSAR_ISCE_MULTI_BURST`, sin water-mask, 80 m, 1 crédito/par) que cubren salar + Fénix. Serie **mensual
    2014–2026**, red SBAS. El salar es **halita árida**: con el track correcto la coherencia C-band es alta
    (~85 %). Sumar el track descendente permitiría **descomponer** vertical/este-oeste
    (ver [próximos pasos](proximos-pasos.md)).

## 2. Interferogramas en la nube (HyP3)

Se arma una **red SBAS** (*Small BAseline Subset*): cada fecha mensual se conecta con las siguientes.
Los pares resultantes se encargan a **HyP3**, que genera los interferogramas gratis en la nube de ASF
(~10 créditos por par, de 8.000/mes gratuitos). → `02_submit_hyp3.py`.

## 3. Serie de tiempo con MintPy

Con los productos descargados, **MintPy** invierte la red SBAS a una serie de tiempo de desplazamiento y una
**velocidad media** (mm/año). Pasos clave (config en `salar149.cfg`):

1. **Carga** del stack y recorte geográfico al AOI del salar (los multi-burst varían unos píxeles de tamaño
   entre fechas; un subset por lon/lat los pone en grilla común).
2. **Red por coherencia**: se descartan pares de baja coherencia.
3. **Punto de referencia** automático en zona de máxima coherencia.
4. **Inversión SBAS** → serie de tiempo.
5. **Corrección troposférica con ERA5** (PyAPS): quita el retardo atmosférico, el principal ruido en InSAR.
6. **Deramp** + **corrección de error de DEM** + **velocidad**.

→ `03_timeseries.sh`, `salar.cfg`.

## 4. Máscara de calidad

Se conservan solo los pixels con **coherencia temporal alta** (> 0.7). **Resultado real (track 149)**: la
coherencia cubre **~85 %** del AOI, incluido **100 % de la concesión de Fénix** — comparable a la estepa seca
de Vaca Muerta. El salar de halita árida es buen terreno para banda C cuando el dato realmente lo cubre. El
límite ahora **no es la coherencia sino la atmósfera** (turbulencia troposférica de la Puna), que pone un piso
de ruido de ~2 mm/año a la velocidad por píxel (ver [Resultados](resultados.md)).

## 5. Visualización

- `04_export_visual.py` → GeoTIFF de velocidad + overlay sobre satélite (folium) + heatmap.
- `05_timeseries_slider.py` → *slider* temporal de deformación acumulada (Leaflet + base64), con suavizado
  temporal Gaussiano para atenuar el ruido atmosférico residual.
- `point_timeseries.py` → series temporales por zona (subsidencia vs referencia estable) para la
  [interpretación](interpretacion.md).
- `overlay_osm.py` → arma `pipeline/overlay.geojson` con las **piletas / cuerpos de agua / industria** desde
  OpenStreetMap (Overpass) para dibujarlas sobre los mapas. Punto de partida; revisar contra Sentinel-2.
- `produccion_litio.py` → grafica la **producción anual de litio** (`produccion_litio.csv`) para el cruce
  producción ↔ subsidencia.

!!! warning "Nota técnica (reproducibilidad)"
    Con MintPy 1.6.2 + numpy 2.x hay un bug en la inversión pixel-a-pixel
    (`setting an array element with a sequence`). Se corrige con un patch de una línea
    (`np.asarray(x).item()`) en `ifgram_inversion.py` y `dem_error.py`. Alternativa: `numpy<2`.

## Reproducir

```bash
mamba env create -f pipeline/environment.yml && mamba activate insar
# credenciales: cuenta NASA Earthdata (~/.netrc) + token CDS (~/.cdsapirc)
# Flujo multi-burst (track 149 asc, el correcto sobre el salar):
python pipeline/02b_submit_bursts.py --submit     # encola 402 pares multi-burst a HyP3
python pipeline/03b_download_bursts.py --loop      # baja a products149/ cuando terminan
cd pipeline && for z in products149/*.zip; do unzip -nq "$z" -d products149/; done
smallbaselineApp.py salar149.cfg                   # → velocity.h5 (serie 2014–2026)
```

> El flujo viejo (`01_search.py` / `02_submit_hyp3.py` / `03_timeseries.sh` / `salar.cfg`) corresponde al
> track 83 descendente, que **no cubre el salar** — se conserva sólo como referencia del error.
