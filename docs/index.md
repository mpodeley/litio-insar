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

Corrimos la cadena completa sobre Hombre Muerto y el resultado es **honesto e instructivo**: con
**Sentinel-1 gratuito (banda C)** el **piso del salar decorrelaciona** (salmuera + halita húmeda + piletas
activas), así que solo el **~16 %** del AOI —las lomas al SO, no los pozos— tiene datos confiables, y ahí el
terreno está **estable**. No aparece la cubeta de subsidencia. **No es un fracaso**: es el **límite físico**
del método para salares húmedos, y contrasta con el éxito del piloto en la estepa seca de Vaca Muerta
(~74 % de cobertura). Capturar el bowl probablemente exija **banda X** (TerraSAR-X/PAZ, como en Atacama) o
**PSI**. Detalle en [Resultados](resultados.md).

## Qué se esperaba (y qué falló)

- **La hipótesis**: zona árida de halita → alta coherencia, y señal de cm/año por bombeo (como
  [Atacama](referencias.md)).
- **Lo que pasó**: la halita **húmeda** y las piletas activas cambian entre pasadas → la banda C pierde la
  fase. La aridez no alcanza si la superficie es agua salada cambiante.
- **Lo que sí quedó útil**: las **piletas de evaporación** (overlay OSM) y la **producción de litio**
  declarada, listas para cruzar con cualquier deformación que un sensor de banda X sí pueda medir.

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

!!! note "Estado: corrida completa, resultado tipo 'límite del método'"
    El sitio nace como **spinoff** del proyecto [Subsidencia en Vaca Muerta con
    InSAR](https://mpodeley.github.io/vaca-muerta-insar/). La cadena Sentinel-1 → HyP3 → MintPy se corrió
    completa (136 interferogramas, ERA5); el resultado es la **limitación de coherencia** descrita arriba, no
    una cubeta de subsidencia. El [caso opaco en China](salar-opaco.md) queda como trabajo futuro.
