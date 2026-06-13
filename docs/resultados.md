# Resultados

Dos formas de mirar el mismo dato: el **mapa de velocidad** (cuánto se mueve cada punto por año) y la
**evolución temporal** (cómo se fue moviendo en el período). Área: **Salar del Hombre Muerto**;
período **2019–2026**.

!!! warning "Resultados pendientes de la primera corrida"
    El método y los visuales están listos, pero los mapas de abajo son **placeholders** hasta correr la
    cadena Sentinel-1 → HyP3 → MintPy sobre el salar (ver [Método](metodo.md)). Cuando `04_export_visual.py`
    y `05_timeseries_slider.py` generen los HTML reales, reemplazarán a estos automáticamente.

## Velocidad media de deformación (2019–2026)

<iframe src="../assets/demo_subsidencia.html" width="100%" height="520" style="border:1px solid #ccc;border-radius:6px"></iframe>

*Overlay interactivo sobre imagen satelital. Rojo = subsidencia, azul = uplift (mm/año). Zoom y arrastre
habilitados.*

## Deformación acumulada en el tiempo (slider)

<iframe src="../assets/demo_acumulado_slider.html" width="100%" height="560" style="border:1px solid #ccc;border-radius:6px"></iframe>

*Arrastrá el slider: cada paso es un trimestre y muestra cuánto se hundió (rojo) o levantó (azul) cada punto
respecto a la primera fecha. Con suavizado temporal para atenuar el ruido atmosférico.*

## Qué buscamos confirmar

1. **Cobertura alta** (coherencia temporal > 0.7 sobre buena parte del AOI) — esperable en halita árida.
2. **Una cubeta de subsidencia localizada** sobre o junto a las piletas / pozos de salmuera, no un sesgo
   global.
3. **Orden de magnitud cm/año**, comparable al precedente de Atacama.
4. **Coincidencia espacial** entre el bowl de subsidencia y la huella operativa (ver
   [Salar del Hombre Muerto](salar-publico.md)).

## La lección metodológica: la atmósfera importa

En InSAR **el preprocesamiento define la conclusión**: con series cortas y sin corrección troposférica es
fácil "ver" subsidencia donde solo hay retardo atmosférico. Por eso la serie es larga (2019–2026) y se
corrige con **ERA5** antes de leer cualquier número.
