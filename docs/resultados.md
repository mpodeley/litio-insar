# Resultados

Dos formas de mirar el mismo dato: el **mapa de velocidad** (cuánto se mueve cada punto por año) y la
**evolución temporal** (cómo se fue moviendo en el período). Área: **Salar del Hombre Muerto**;
período **2019–2026**.

!!! danger "Resultado principal: el salar decorrelaciona — el InSAR gratis no ve el piso del salar"
    Corrimos la cadena completa (track 83 descendente, **136 interferogramas**, 88 fechas, corrección ERA5).
    El hallazgo no es una cubeta de subsidencia, sino una **limitación de coherencia**: la superficie
    **húmeda/cambiante del salar (salmuera + piletas activas)** pierde coherencia, así que solo el **16 %**
    del AOI tiene datos confiables, **concentrados en las lomas/aluvión al SO** — no sobre las piletas ni los
    pozos. Donde hay datos, el terreno está **esencialmente estable**. **No es un límite físico de la banda C**
    (en Atacama, Sentinel-1 sí midió la subsidencia sobre el núcleo de halita estable): es dónde **esta corrida
    gratuita** se queda corta, y por qué (ver abajo y [Método](metodo.md)).

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
  las piletas activas** la fase se decorrelaciona entre pasadas → esos píxeles quedan enmascarados.
- **Importante (corrección honesta)**: en **Atacama**, la banda C **sí funcionó** — Sentinel-1 detectó ~4 cm
  de subsidencia LOS sobre el **núcleo de halita seca y estable** (Delgado et al.; el estudio sumó además
  **ALOS-2 y SAOCOM en banda L** y **PAZ en banda X**). O sea, la banda C **no es** el problema de fondo.
- Entonces nuestro resultado nulo es **específico de esta corrida/salar**: acá los píxeles coherentes cayeron
  en los **márgenes**, no en el núcleo. Las palancas reales para mejorarlo: **banda L** (SAOCOM —argentino,
  cubre el salar— o ALOS-2), que mantiene coherencia sobre superficies cambiantes mucho mejor que la C;
  procesar enfocando el **núcleo de halita** con otro track / umbrales; y **PSI** sobre estructuras estables.
- También ayudaría sumar el **track ascendente** (más geometría) y acotar el AOI al wellfield.

## La lección metodológica

Dos, en realidad: (1) **la atmósfera importa** —la serie larga + corrección **ERA5** evita "ver" subsidencia
donde solo hay retardo atmosférico—; y (2) **el sensor y la superficie importan tanto como el pipeline**: el
mismo flujo que funciona de diez en la estepa seca de Vaca Muerta **se queda corto** sobre las partes
húmedas/cambiantes de este salar. No porque la banda C no sirva (en Atacama sí midió), sino porque acá la
coherencia no cayó donde está la señal — algo mejorable con **banda L** o mejor procesamiento. Reportar el
resultado nulo y por qué es parte del experimento.
