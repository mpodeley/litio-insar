# Cómo pedir datos para mejorar el InSAR del Salar del Hombre Muerto

Instructivo paso a paso para tramitar **todo lo que suma** sobre el caso Fénix / Salar del
Hombre Muerto. Estado actual: ya tenemos la serie Sentinel-1 (banda C, track 149 ASC,
2014–2026) con 85 % de coherencia, pero la señal de deformación (~1–2,5 mm/año) está en el
**piso de ruido atmosférico** de la Puna. Lo de abajo es para bajar ese piso (GACOS) y/o
sumar **banda L** (SAOCOM/NISAR/ALOS), que es la palanca de fondo.

Parámetros comunes del área (usalos en todos los pedidos):

| | valor |
|---|---|
| AOI (bbox) | **S −25.65 · N −25.05 · O −67.40 · E −66.70** |
| Punto Fénix | lat −25.49, lon −67.10 |
| Hora de paso Sentinel-1 (track 149 ASC) | **~23:08 UTC** |
| Período de interés | 2014 → 2026 (producción reciente: 2018→) |

---

## 1) GACOS — corrección atmosférica (gratis, lo más rápido) ⭐ empezar por acá

Mejora la corrección troposférica (ERA5 ~30 km → ECMWF HRES ~9 km + topografía). No arregla
la turbulencia <9 km pero baja el piso de ruido. **Es lo que da el mejor retorno inmediato.**

1. Entrá a **http://www.gacos.net/**.
2. Completá el formulario:
   - **Region**: South −25.65, North −25.05, West −67.40, East −66.70.
   - **Time (UTC)**: `23:08`.
   - **Dates**: pegá la lista de fechas (135) del archivo **`gacos_dates.txt`** (está en esta
     carpeta). Si el form pide rango, usá `2014-10-27` a `2026-05-03` con paso "use my dates".
   - **Email**: el tuyo.
3. Enviás y **te llegan por mail los `.ztd`** (un archivo por fecha) con un link de descarga
   (puede tardar de minutos a horas).
4. Descomprimís todo en `docs/pipeline/GACOS/`.
5. Avisame: yo configuro MintPy (`salar149_gacos.cfg`, ya preparada con
   `troposphericDelay.method = gacos`) y re-corro la serie. Comparamos vs ERA5.

> No requiere registro ni convenio. Es el primer paso lógico.

---

## 2) SAOCOM (CONAE) — banda L argentina ⭐ la palanca de fondo

L-band (λ≈24 cm): mucha más coherencia sobre sal/salmuera y unwrapping robusto. Es lo que usó
el grupo de Delgado en Atacama. Cubre **desde oct-2018** (1A) / ago-2020 (1B).

1. **Registrate** en el Registro de Usuarios CONAE:
   **https://registro.conae.gov.ar/registracion/view/**
2. Iniciá sesión y **aceptá la licencia** del ítem
   *"Acceso a Productos de Archivo SAOCOM 1 del Territorio Argentino"* (trámite online; abierto
   a usuarios de todo el mundo para territorio argentino — Hombre Muerto califica).
3. Entrá al **Catálogo SAOCOM**: **https://catalog.saocom.conae.gov.ar/catalog/#/**
4. Dibujá el **ROI** (la caja de arriba) y filtrá por fecha (2019→2026).
5. Elegí el producto correcto para InSAR:
   - **Nivel L1A — SLC** (Single Look Complex), dual-pol (VV/VH).
   - **Modo StripMap** (resolución fina; ideal interferometría). Evitar TOPSAR salvo cobertura.
   - **Mismo track/órbita y beam** para que los pares sean interferométricos. Juntá la mayor
     cantidad de fechas posible del mismo track.
6. **Descargá** los SLC.
   - ⚠️ Si la descarga/pedido te pide más permisos: para *descarga masiva / nuevas
     adquisiciones / procesamiento* CONAE exige **Convenio + permisos**. Para archivo sobre
     territorio argentino suele alcanzar con la licencia; si te frena, ver punto 2.b.
7. Pasame los SLC: proceso **SAOCOM SLC → interferogramas con ISCE** (hay flujo SAOCOM+ISCE) →
   MintPy, igual que ahora.

**2.b) Vía científica (si necesitás volumen / adquisiciones nuevas):** ESA/CONAE **PUMAS**
(Announcement of Opportunity) — acceso por **propuesta** evaluada por ESA y CONAE.
Buscar "ESA CONAE PUMAS SAOCOM Announcement of Opportunity".

> SAOCOM no tiene un servicio nube tipo HyP3: el procesamiento es manual (ISCE/GAMMA). Yo me
> encargo de eso; vos conseguí los SLC.

---

## 3) NISAR — banda L gratis y abierta (NASA/ISRO, desde 2025) ⭐ alternativa sin trámite

L-band abierta vía ASF, **sin registro especial** (igual que Sentinel). Lanzado jul-2025; datos
calibrados completos desde ~jul-2026. Es la opción L-band más fácil de conseguir a futuro.

1. Cuenta **Earthdata** (ya la tenés en `~/.netrc`).
2. Buscá en **ASF Vertex**: https://search.asf.alaska.edu/ → plataforma **NISAR**, o por
   `asf_search` (dataset NISAR) sobre la AOI.
3. Producto para InSAR: **L1 RSLC** (o los productos InSAR L2 GUNW cuando estén). Mismo track.
4. Cobertura temporal: solo **2025→** (no sirve para la era previa, pero sí para seguimiento).
5. Avisame y lo proceso (o uso los GUNW si ya vienen interferométricos).

---

## 4) ALOS-2 / ALOS-1 PALSAR — banda L histórica (opcional)

- **ALOS-1 PALSAR (2007–2011)**: L-band **gratis** vía ASF Vertex (Earthdata). Sirve para una
  foto L-band **anterior** a la expansión (línea de base histórica), pero baja densidad temporal.
- **ALOS-2 PALSAR-2 (2014→)**: L-band, **pago/restringido** (JAXA). Mejor cobertura pero no gratis.

Para ALOS-1: ASF Vertex → plataforma ALOS PALSAR → L1.1 SLC sobre la AOI.

---

## Prioridad sugerida

1. **GACOS** (hoy, gratis, sin trámite) — exprimir lo que ya tenemos.
2. **SAOCOM** (registro CONAE + licencia) — el salto de calidad real (banda L sobre el salar).
3. **NISAR** (cuando haya archivo, gratis) — seguimiento L-band a futuro.
4. ALOS-1 (gratis) — línea de base histórica opcional.

Cualquiera que consigas, traémelo y lo proceso e integro a la serie.
