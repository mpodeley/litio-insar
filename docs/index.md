# ¿Se puede ver hundirse un salar de litio desde el espacio?

Este sitio documenta un **experimento técnico**: medir la **deformación del suelo**
(*subsidencia*, hundimiento de milímetros a centímetros por año) en salares donde se
extrae **salmuera de litio**, usando **únicamente datos satelitales públicos y gratuitos**
(Sentinel-1, radar de apertura sintética).

La pregunta no es comercial sino metodológica:

> **¿Se observa la subsidencia por bombeo de salmuera con InSAR satelital, y qué dice el dato
> cuando lo cruzamos con la actividad de la mina?**

El caso piloto es el **[Salar del Hombre Muerto](salar-publico.md)** (Catamarca/Salta, Argentina),
operado por Minera del Altiplano (Fénix; Livent → Arcadium → **Rio Tinto** desde 2025). Luego la idea es
**replicar el mismo método en un salar opaco** —donde casi no hay datos operativos públicos— como los del
**[altiplano de Qinghai/Tíbet, China](salar-opaco.md)**, para mostrar qué revela el satélite cuando el dato
oficial no transparenta los caudales.

!!! info "Por qué esperamos ver señal"
    Hay **precedente publicado**: en el **Salar de Atacama** (Chile), InSAR con Sentinel-1 detectó
    **~1 cm/año de subsidencia** en una zona de ~8 km junto a los pozos de salmuera (2019–2022), atribuida a
    una caída de ~10 m del nivel freático por un bombeo más rápido que la recarga. El mecanismo es el mismo
    que esperamos en Hombre Muerto. Ver [Referencias](referencias.md).

## Resultado corto (spoiler)

Un giro instructivo, en dos actos:

1. **Primera corrida (resultado nulo) → era un error de cobertura.** Una primera pasada con el **track 83
   descendente** dio "el salar decorrelaciona, no hay datos sobre los pozos". Resultó **falso**: ese track
   **no cubre el salar** — su huella (el rectángulo inclinado de la pasada) corta justo al sur de la
   operación, así que lo que mirábamos era **terreno al sur del salar**, no Fénix. Amplitud y coherencia daban
   cero ahí simplemente porque **no había dato**, no porque la sal "rompa" la banda C.
2. **Con el track correcto (149 ascendente) la banda C SÍ ve el salar.** Re-pedimos los datos como
   **multi-burst** centrado en la operación: **~85 % del AOI coherente** (y **100 % sobre la concesión de
   Fénix**). Aparece una **señal de deformación acumulada de ~15–30 mm entre 2014 y 2026** sobre la operación,
   que crece de forma sostenida durante la era de producción.

El honesto matiz: esa señal es **chica (~1–2,5 mm/año) y está cerca del piso de ruido atmosférico** de la Puna
(4000 m), así que sólo emerge limpia al **promediar por zona** y quitar el retardo común. Afinarla (corrección
**GACOS**, o **banda L** vía SAOCOM/NISAR) es el siguiente paso. Detalle en [Resultados](resultados.md).

## La lección (qué pasó y qué aprendimos)

- **La hipótesis** sigue en pie: zona árida de halita → alta coherencia (¡se confirmó: 85 %!), y señal de
  mm/año por bombeo (como [Atacama](referencias.md)).
- **La trampa**: el primer "resultado nulo" no era física sino **el track equivocado**. Lección dura de InSAR:
  antes de interpretar coherencia, **verificar que la huella del dato cubra el objetivo** (lo chequeamos
  contra imagen satelital).
- **Lo que tenemos ahora**: serie 2014–2026 con buena coherencia sobre el salar, lista para cruzar con la
  **producción de litio** una vez bajado el ruido atmosférico (ver [estado y pendientes](#estado-y-pendientes)).

## Qué vas a encontrar acá

- **[Método paso a paso](metodo.md)** — de la descarga de imágenes al mapa final, reproducible y con fuentes.
- **[Resultados](resultados.md)** — visualizaciones interactivas (mapa de velocidad + slider temporal).
- **[Interpretación](interpretacion.md)** — el mecanismo (bombeo > recarga) y los *caveats*.
- **[Salar del Hombre Muerto](salar-publico.md)** — el caso público: operación, producción de litio y cruce
  con la deformación.
- **[Caso opaco (China)](salar-opaco.md)** — replicar el método donde el dato operativo no es público.

!!! note "Honestidad metodológica"
    InSAR mide **correlación espacio-temporal**, no causalidad. Este es un piloto de viabilidad con datos
    gratuitos; no reemplaza un estudio con validación de campo (GNSS) ni distingue por sí solo el mecanismo
    de la deformación. Se usó **Claude (Anthropic)** para asistir en el procesamiento, el análisis y la
    redacción; los resultados y conclusiones fueron revisados por el autor.

## Estado y pendientes

!!! note "Estado actual (jun-2026): el salar SÍ se mide; afinando la señal"
    El sitio nace como **spinoff** del proyecto [Subsidencia en Vaca Muerta con
    InSAR](https://mpodeley.github.io/vaca-muerta-insar/).

    **Hecho:**

    - [x] Detectado y corregido el error de track (83 desc. no cubría el salar → **149 asc.**).
    - [x] Re-pedido **multi-burst** a HyP3 centrado en la operación (402 interferogramas, 2014–2026, banda C).
    - [x] Serie SBAS + ERA5 corrida: **~85 % de coherencia** sobre el salar, 100 % sobre Fénix.
    - [x] Señal de deformación acumulada (~15–30 mm, 2014–2026) extraída por zona.

    **Pendiente:**

    - [ ] **Corrección atmosférica GACOS** para bajar el piso de ruido de la Puna (pedido listo).
    - [ ] **Banda L (SAOCOM / NISAR)** — la palanca de fondo para una señal limpia sobre la sal.
    - [ ] Confirmar el **signo** (subsidencia vs uplift relativo) y separar subzonas (extracción vs piletas).
    - [ ] Completar/verificar la serie de **producción de litio** y hacer el cruce final.
    - [ ] [Caso opaco en China](salar-opaco.md) (trabajo futuro).
