# Resultados

Dos formas de mirar el mismo dato: el **mapa de velocidad** (cuánto se mueve cada punto por año) y la
**evolución temporal** (cómo se fue moviendo en el período). Área: **Salar del Hombre Muerto**;
período **2019–2026**.

!!! danger "Resultado principal: el salar decorrelaciona — el InSAR gratis no ve el piso del salar"
    Corrimos la cadena completa (track 83 descendente, **136 interferogramas**, 88 fechas, corrección ERA5).
    El hallazgo no es una cubeta de subsidencia, sino una **limitación física**: en banda C, la superficie
    **húmeda del salar (salmuera + costra de halita que cambia)** pierde coherencia, así que solo el **16 %**
    del AOI tiene datos confiables, **concentrados en las lomas/aluvión al SO** — no sobre las piletas ni los
    pozos. Donde hay datos, el terreno está **esencialmente estable**. Es un resultado honesto e informativo:
    marca el **límite del método** para este tipo de salar (ver abajo y [Método](metodo.md)).

## Velocidad media de deformación (2019–2026)

<iframe src="../assets/demo_subsidencia.html" width="100%" height="520" style="border:1px solid #ccc;border-radius:6px"></iframe>

*Overlay interactivo sobre imagen satelital. Rojo = subsidencia, azul = uplift (mm/año). Zoom y arrastre
habilitados.*

## Deformación acumulada en el tiempo (slider)

<iframe src="../assets/demo_acumulado_slider.html" width="100%" height="560" style="border:1px solid #ccc;border-radius:6px"></iframe>

*Arrastrá el slider: cada paso es un trimestre y muestra cuánto se hundió (rojo) o levantó (azul) cada punto
respecto a la primera fecha. Con suavizado temporal para atenuar el ruido atmosférico.*

## Los números

| Métrica | Valor |
|---|---|
| Interferogramas / fechas | 136 / 88 (SBAS, track 83 desc.) |
| Píxeles confiables (coherencia temporal > 0.7) | **92.045 (~16 % del AOI)** |
| Velocidad **mediana** | **−0.1 mm/año** (estable) |
| Percentil 1 / 5 | −2.7 / −1.8 mm/año |
| Percentil 95 / 99 | +1.6 / +2.8 mm/año |
| Mínimo (más negativo) | −8.0 mm/año (1 píxel aislado) |

Compará con el piloto hermano de **Vaca Muerta** (estepa árida): ahí la coherencia cubría **~74 %** del área
y había cubetas de hasta −12 mm/año. Acá la diferencia no es la deformación sino el **terreno**: el salar es
una superficie cambiante (salmuera, costra, piletas activas) que **rompe la coherencia** en banda C.

## Por qué pasa esto (y qué haría falta)

- **Sentinel-1 es banda C (λ≈5,6 cm)**: muy sensible a cambios de la superficie. Sobre la **halita húmeda y
  las piletas** la fase se decorrelaciona entre pasadas → esos píxeles quedan enmascarados.
- El precedente de **Atacama** que detectó ~1 cm/año usó en buena parte **PAZ/TerraSAR-X (banda X, alta
  resolución)** sobre el núcleo de halita, además de Sentinel-1. Para Hombre Muerto, capturar la deformación
  del piso del salar probablemente requiera **banda X** o técnicas de **dispersores persistentes (PSI)** sobre
  estructuras estables, no el SBAS C-band gratuito.
- También ayudaría sumar el **track ascendente** (más geometría) y acotar el AOI al wellfield.

## La lección metodológica

Dos, en realidad: (1) **la atmósfera importa** —la serie larga + corrección **ERA5** evita "ver" subsidencia
donde solo hay retardo atmosférico—; y (2) **el terreno define la viabilidad**: el mismo pipeline que funciona
de diez en la estepa de Vaca Muerta **choca con la física** sobre un salar húmedo. Reportar esto es parte del
experimento.
