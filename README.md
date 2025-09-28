## 📁 Estructura del repositorio
"""Tmin-Per-GeoTIFF/
├─ app/app.py
├─ assets/
│ ├─ hist_tmin_media.png
│ ├─ mapa_distritos_tmin_mean.png
│ ├─ Top_15_distritos_bajos.png
│ ├─ Top_15_distritos_altos.png
│ ├─ top15_tmin_baja_distritos.csv
│ ├─ top15_tmin_alta_distritos.csv
│ ├─ pol1_boxplot_p10.png
│ ├─ pol1_conteo_por_depto.png
│ ├─ pol1_mapa_objetivo.png
│ ├─ pol2_scatter_min_std.png
│ ├─ pol2_conteo_por_depto.png
│ ├─ pol2_mapa_objetivo.png
│ ├─ pol3_hist_amazonia_tmin_media.png
│ ├─ pol3_conteo_por_depto.png
│ └─ pol3_mapa_objetivo.png
├─ data/shape_file/DISTRITOS.shp (+dbf, prj, shx…)
├─ tmin_raster.tif
├─ notebooks/task_3.ipynb
├─ requirements.txt
└─ README.md"""

# Requisitos
streamlit
pandas
numpy
geopandas
rasterio
rasterstats
matplotlib
seaborn
# Instalación local:
pip install -r requirements.txt
# App Streamlit (2 hojas)
streamlit run app/app.py
## Deploy
https://tmin-per-geotiff-ybctkrul9aedbe2ycnrbag.streamlit.app/ 
