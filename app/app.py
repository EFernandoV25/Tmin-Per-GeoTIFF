
import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Análisis Tmin y Políticas", layout="wide")

# Ruta relativa: desde app/ ir a assets/
REPO_ROOT = Path(__file__).resolve().parents[1]
ASSETS = REPO_ROOT /"assets "

# Archivos Hoja 1 (Path, no strings)
IMG_HIST   = "app/assets/hist_tmin_media.png"
IMG_MAPA   = ASSETS / "mapa_distritos_tmin_mean.png"
IMG_TOP_MIN = ASSETS / "Top_15_distritos_bajos.png"
IMG_TOP_MAX = ASSETS / "Top_15_distritos_altos.png"
CSV_TOP_MIN = ASSETS / "top15_tmin_baja_distritos.csv"
CSV_TOP_MAX = ASSETS / "top15_tmin_alta_distritos.csv"

# Archivos Hoja 2
P1_BOX = ASSETS / "pol1_boxplot_p10.png"
P1_CNT = ASSETS / "pol1_conteo_por_depto.png"
P1_MAP = ASSETS / "pol1_mapa_objetivo.png"

P2_SCT = ASSETS / "pol2_scatter_min_std.png"
P2_CNT = ASSETS / "pol2_conteo_por_depto.png"
P2_MAP = ASSETS / "pol2_mapa_objetivo.png"

P3_HIST = ASSETS / "pol3_hist_amazonia_tmin_media.png"
P3_CNT  = ASSETS / "pol3_conteo_por_depto.png"
P3_MAP  = ASSETS / "pol3_mapa_objetivo.png"

# ------------------------------
# HOJA 1
# ------------------------------
tab1, tab2 = st.tabs(["Hoja 1 · Análisis Tmin", "Hoja 2 · Políticas"])

with tab1:
    st.header("Análisis de temperatura mínima (Tmin)")

    c1, c2 = st.columns(2)
    with c1:
        st.image(IMG_HIST), caption="Distribución de Tmin media por distrito", use_column_width=True)
    with c2:
        st.image(str(IMG_MAPA), caption="Mapa de distritos según Tmin media", use_container_width=True)

    st.divider()
    st.subheader("Exploración: Top mínimos y máximos")

    opcion = st.radio(
        "Selecciona el ranking:",
        ["Top mínimo (distritos más fríos)", "Top máximo (distritos más cálidos)"],
        horizontal=True
    )

    if "mínimo" in opcion:
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.image(str(IMG_TOP_MIN), caption="Top 15 Tmin media más baja", use_container_width=True)
        with c2:
            if CSV_TOP_MIN.exists():
                df_min = pd.read_csv(CSV_TOP_MIN)
                st.dataframe(df_min, use_container_width=True)
            else:
                st.info("ℹ️ Falta 'top15_tmin_baja_distritos.csv'.")
    else:
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.image(str(IMG_TOP_MAX), caption="Top 15 Tmin media más alta", use_container_width=True)
        with c2:
            if CSV_TOP_MAX.exists():
                df_max = pd.read_csv(CSV_TOP_MAX)
                st.dataframe(df_max, use_container_width=True)
            else:
                st.info("ℹ️ Falta 'top15_tmin_alta_distritos.csv'.")

with tab2:
    st.header("Políticas públicas")

    st.markdown("""
### Política 1 · Viviendas térmicas + kits antiheladas (altoandinos)
**Objetivo.** −20% IRA en <5 años y −15% días escolares perdidos.  
**Focalización.** `tmin_banda5_percentile_10 ≤ −2 °C`.  
**Intervención.** ISUR + kits antiheladas + paquete escolar mínimo.  
**Costo.** S/ 6,000 hogar; S/ 2,500 aula.  
**KPI.** −20% IRA; −15% ausentismo; ≥90% viviendas con mejora térmica ≥ 2 °C.
""")
    c1, c2 = st.columns(2)
    with c1: st.image(str(P1_MAP), caption="Mapa · distritos objetivo", use_container_width=True)
    with c2: st.image(str(P1_CNT), caption="Distritos objetivo por departamento", use_container_width=True)
    st.image(str(P1_BOX), caption="Distribución de Tmin p10", use_container_width=True)

    st.markdown("""
---
### Política 2 · Refugios comunales para ganado + atención veterinaria
**Objetivo.** −25% mortalidad de crías; −10% pérdida de peso en hatos.  
**Focalización.** `tmin_banda5_percentile_10 ≤ −5 °C`.  
**Intervención.** Refugios + paquetes veterinarios + gestión de riesgo.  
**Costo.** S/ 15,000 refugio; S/ 500 kit/familia; S/ 3,000 forraje.  
**KPI.** −25% mortalidad; +10% fibra; ≥80% ocupación en noches críticas.
""")
    c1, c2 = st.columns(2)
    with c1: st.image(str(P2_SCT), caption="Riesgo térmico", use_container_width=True)
    with c2: st.image(str(P2_CNT), caption="Distritos objetivo por departamento", use_container_width=True)
    st.image(str(P2_MAP), caption="Mapa · distritos objetivo para refugios", use_container_width=True)

    st.markdown("""
---
### Política 3 · Adaptación a variabilidad térmica nocturna (Amazonía)
**Objetivo.** −15% consultas por IRA y −10% ausentismo escolar.  
**Focalización.** `tmin_banda5_mean ≤ 22 °C`.  
**Intervención.** Alertas comunitarias + kits ligeros + protocolos escolares/postas.  
**Costo.** S/ 250 kit/hogar; S/ 3,000 paquete escuela/posta; S/ 8,000 alertas/distrito·año.  
**KPI.** −15% consultas; −10% ausentismo; ≥90% protocolos activados.
""")
    c1, c2 = st.columns(2)
    with c1: st.image(str(P3_HIST), caption="Distribución de Tmin media", use_container_width=True)
    with c2: st.image(str(P3_CNT), caption="Distritos objetivo por departamento", use_container_width=True)
    st.image(str(P3_MAP), caption="Mapa · distritos amazónicos objetivo", use_container_width=True)
    





