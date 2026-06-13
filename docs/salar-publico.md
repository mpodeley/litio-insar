# Salar del Hombre Muerto (Argentina)

El caso **público** del experimento: un salar donde el operador cotiza y publica datos de producción, y
donde el catastro minero permite ubicar la concesión. La tesis es cruzar la **deformación InSAR** con la
**actividad declarada** y ver si coinciden en espacio y tiempo.

## La operación

| Dato | Valor |
|---|---|
| Ubicación | Salar del Hombre Muerto, Catamarca / Salta (Puna argentina, ~4.000 m s.n.m.) |
| Proyecto | **Fénix**, operado por **Minera del Altiplano S.A.** |
| Matriz | Livent → **Arcadium Lithium** (ene-2024) → **Rio Tinto** (mar-2025) |
| Método | bombeo de salmuera + **piletas de evaporación** solar → carbonato de litio |
| Capacidad reportada | ~40 ktpy LCE (meta 2023) con expansión hacia ~60 ktpy LCE | 

*Cifras de capacidad según reportes públicos del operador/medios; a verificar contra los filings de la matriz.*

!!! note "Por qué este salar"
    Es una operación **madura y en expansión** (más de dos décadas), con producción **declarada** por una
    empresa que cotiza, y vecina a otros proyectos de la Puna. Eso permite contrastar el satélite contra el
    dato oficial — lo opuesto al [caso opaco](salar-opaco.md).

## Datos públicos a cruzar

- **Producción de litio (LCE) por año** — de los reportes de la matriz (Livent/Arcadium/Rio Tinto) y de la
  Secretaría de Minería de la Nación. Sirve para la curva "producción ↔ subsidencia" análoga a la de
  producción de Vaca Muerta.
- **Concesión / pertenencias mineras** — catastro minero nacional (SEGEMAR) y provincial (Catamarca).
  **Disponibilidad de polígonos a verificar**; si no hay GeoJSON público, se digitalizan las **piletas de
  evaporación** desde imágenes Sentinel-2 (son enormes y de borde nítido) y se cargan en
  `pipeline/overlay.geojson`.
- **Imagen óptica (Sentinel-2)** — para datar la **expansión de las piletas** en el tiempo y compararla con
  el avance del bowl de subsidencia.

## Estado del análisis

!!! warning "Pendiente de la primera corrida"
    Falta correr la cadena InSAR sobre el AOI (ver [Método](metodo.md)) y completar:

    - [ ] Elegir el track Sentinel-1 con `01_search.py` y fijarlo en `aoi.py`.
    - [ ] Verificar el bounding box y el punto de referencia Fénix contra la imagen satelital.
    - [ ] Generar el mapa de velocidad y el slider ([Resultados](resultados.md)).
    - [ ] Digitalizar las piletas de evaporación → `pipeline/overlay.geojson`.
    - [ ] Armar la serie anual de producción de litio y cruzarla con la subsidencia.
