# Tmin-Per-GeoTIFF
Tmin-Per-GeoTIFF/
├─ app/app.py                 # Código de la app Streamlit
├─ assets/                    # Gráficas (PNG) y tablas (CSV) generadas
├─ data/shape_file/           # Shapefile de distritos del Perú
├─ tmin_raster.tif            # Raster GeoTIFF de Tmin
├─ notebooks/task_3.ipynb     # Notebook de cálculo/visualización
├─ requirements.txt           # Dependencias
└─ README.md

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
