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

## Por qué los salares son un buen caso para InSAR

- **Zona árida, suelo de halita, sin vegetación** → alta **coherencia** interferométrica (poco ruido).
- **Señal localizada y de magnitud cm/año** → bien dentro de lo que mide Sentinel-1.
- **Huella muy visible**: las **piletas de evaporación** son enormes y se digitalizan fácil desde imágenes
  ópticas, lo que da un overlay para cruzar con el bowl de subsidencia.

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

!!! warning "Estado: experimento en curso"
    El sitio nace como **spinoff** del proyecto [Subsidencia en Vaca Muerta con
    InSAR](https://mpodeley.github.io/vaca-muerta-insar/). El método y el pipeline están listos; los
    **resultados sobre Hombre Muerto se completan** al correr la cadena Sentinel-1 → HyP3 → MintPy
    (ver [Método](metodo.md)).
