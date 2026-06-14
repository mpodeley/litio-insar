# Resultados

Área: **Salar del Hombre Muerto** (operación Fénix); período **2014–2026**; **Sentinel-1 banda C**,
track **149 ascendente**, multi-burst (ver [Método](metodo.md)).

!!! danger "Primero: por qué la corrida original daba 'nulo' (y por qué estaba mal)"
    Una primera pasada con el **track 83 descendente** concluía "el salar decorrelaciona, no hay datos sobre
    los pozos (~16 % de coherencia, sólo en lomas)". **Era un artefacto de cobertura**: el track 83 **no cubre
    el salar** — su huella corta al sur de Fénix, y lo procesado era terreno al sur. Amplitud y coherencia
    daban **exactamente cero** sobre la operación porque **no había dato** ahí, no por la sal.

    <img src="../assets/cobertura_coherencia.png" alt="cobertura track 83" width="100%">

    *Track 83: el dato (verde/coherente) cubre sólo al sur de una diagonal recta (borde del frame). El salar y
    las piletas (contornos rojos) y Fénix (▲) quedan al norte, **sin dato**.*

## El track correcto (149 ascendente)

Re-pedimos los datos como **multi-burst** centrados en la operación. La huella del track 149 sí contiene el
salar y Fénix (verificado contra imagen satelital):

<img src="../assets/verif_operacion.png" alt="bursts track 149 sobre la operación" width="100%">

*Los 3 *bursts* IW2 (líneas de colores) y el AOI de análisis (verde) sobre el salar; piletas/concesión OSM
(blanco/magenta) sobre la sal.*

## El salar SÍ es coherente en banda C

| Métrica | Track 83 (mal ubicado) | **Track 149 (correcto)** |
|---|---|---|
| Cobertura del dato sobre el salar | ~0 (fuera del frame) | **completa** |
| Coherentes (coh. temporal > 0.7) | ~16 % (terreno al sur) | **~85 % del AOI** |
| Coherencia sobre la concesión de Fénix | 0 % (sin dato) | **100 %** (coh. 0.96) |
| Interferogramas / fechas | 136 / 88 | **399 / 135** (2014–2026) |

La hipótesis de partida se confirma: **halita árida → alta coherencia**. El problema nunca fue la banda C, era
el track.

## Velocidad media de deformación (2014–2026)

<img src="../assets/vel_smooth.png" alt="velocidad LOS suavizada" width="100%">

*Velocidad LOS suavizada (mm/año; convención MintPy: + hacia el satélite). El campo es **mayormente ruido
espacialmente correlacionado** (turbulencia atmosférica de la Puna a 4000 m): no hay una cubeta de subsidencia
ni un domo limpios a nivel velocidad/píxel. El piso de ruido es ~2 mm/año, del orden de la señal buscada.*

## La señal aparece al promediar: subsidencia acumulada vs producción

Promediando por zona y quitando el retardo atmosférico común (doble diferencia vs la mediana de la escena), sí
emerge una **tendencia coherente** sobre la operación:

<img src="../assets/serie_dd.png" alt="serie acumulada vs producción" width="100%">

*Desplazamiento LOS acumulado por zona (mm), 2014–2026, con la producción de litio (barras). Las tres zonas
(Fénix, hotspot NE, piletas E) acumulan **~15–30 mm** a lo largo del período, creciendo de forma sostenida
durante la era de producción.*

| Zona | Acumulado 2014–2026 | Tasa |
|---|---|---|
| Hotspot NE (−66.99, −25.37) | ~+25 mm | ~+2,5 mm/año |
| Piletas E (−66.9) | ~+17 mm | ~+1,3 mm/año |
| Concesión Fénix | ~+18 mm | ~+1,1 mm/año |

## Los caveats honestos

- **Señal en el piso de ruido**: ~1–2,5 mm/año es del orden del ruido atmosférico por píxel. Sólo se ve limpia
  **promediando por zona**; tomarla con pinzas hasta bajar el ruido.
- **Signo sin confirmar**: por convención de MintPy (+ = hacia el satélite) el valor positivo sería **uplift
  relativo**, no subsidencia; la convención de HyP3 es la opuesta. Hay que verificarlo antes de afirmar
  dirección (podría ser una mezcla: acumulación de sal en piletas = uplift, + extracción = subsidencia en otra
  subzona).
- **Cruce con producción preliminar**: la serie de producción (`produccion_litio.csv`) es escasa y sin
  verificar; el cruce es ilustrativo, no concluyente.

## Qué falta para una señal limpia

El cuello de botella ahora es **la atmósfera, no la coherencia**. Ver [estado y pendientes](index.md#estado-y-pendientes)
e [instructivo de pedidos](https://github.com/mpodeley/litio-insar/blob/main/docs/pipeline/COMO_PEDIR_DATOS.md):

1. **GACOS** — corrección troposférica más fina que ERA5 (gratis; pedido listo).
2. **Banda L (SAOCOM / NISAR)** — más coherencia y unwrapping robusto → mejor estimación del APS. La palanca
   de fondo (es lo que usó el grupo de Delgado en [Atacama](referencias.md)).
3. **Track descendente** — para descomponer vertical / este-oeste.
