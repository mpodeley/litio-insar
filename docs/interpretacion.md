# Interpretación

!!! danger "Lo primero: qué se pudo y qué no medir"
    La corrida sobre Hombre Muerto **no** mostró una cubeta de subsidencia, sino una **limitación de
    coherencia**: el piso húmedo del salar decorrelaciona en banda C y queda sin datos (ver
    [Resultados](resultados.md)). Por eso lo de abajo es el **mecanismo esperado** (la hipótesis), no algo que
    hayamos confirmado acá. Sigue siendo el marco correcto para cuando se mida con un sensor adecuado
    (banda X / PSI).

## El mecanismo: bombeo más rápido que la recarga

La extracción de litio por salmuera **bombea agua salada desde el acuífero del salar** hacia las piletas de
evaporación. Cuando la tasa de bombeo supera a la de recarga natural, el **nivel freático baja**, cae la
presión de poro y los sedimentos del salar **se compactan**: el terreno se hunde. Es el mismo proceso de
subsidencia por extracción de fluidos que en acuíferos y campos de hidrocarburos, y el que InSAR midió en el
**Salar de Atacama** (~1 cm/año sobre ~8 km, asociado a una caída de ~10 m del nivel freático).

## Qué señal esperamos y cómo se ve

- **Cubeta localizada** de subsidencia centrada en/junto a los **pozos de extracción**, no un hundimiento
  homogéneo de todo el salar.
- **Tendencia sostenida** (monótona) a lo largo de los años, que crece a medida que se expande la operación
  — distinta de una **oscilación estacional**.
- Las **piletas** en sí suelen quedar **enmascaradas** (su superficie de salmuera cambia y decorrelaciona);
  la firma de compactación se lee en el terreno **alrededor**.

## Qué NO es (los caveats)

!!! warning "Lo que InSAR no resuelve solo"
    - **Oscilación por lluvia / halita**: los salares se **inflan y desinflan** con las precipitaciones y el
      crecimiento de la costra de halita. Una serie larga (2019–2026) y la corrección ERA5 ayudan a separar
      la **tendencia** (extracción) del **ciclo** (clima), pero no lo garantizan sin dato de campo.
    - **Causalidad**: una coincidencia espacial entre subsidencia y pozos es **correlación**. Atribuirla al
      bombeo requiere descartar otras causas (tectónica, carga sedimentaria) y, idealmente, datos
      piezométricos.
    - **Una sola línea de vista**: con un track no se separa el movimiento vertical del horizontal. La
      descomposición ascendente+descendente queda para [próximos pasos](proximos-pasos.md).

## Cómo lo testeamos en el dato

`point_timeseries.py` compara dos zonas: una de **subsidencia** (pixels con velocidad muy negativa, sobre los
pozos) y una de **referencia estable** (lejos de la operación). Si la zona de subsidencia muestra una caída
**sostenida** mientras la referencia se mantiene plana, el patrón es consistente con extracción; si ambas
oscilan en fase con las lluvias, domina el clima.
