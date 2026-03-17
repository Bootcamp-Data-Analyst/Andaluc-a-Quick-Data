# Andalucía Quick Data

Librería Python que permite acceder de forma sencilla a datos espaciales y estadísticos públicos de la Junta de Andalucía.

## Características

- Acceso a fuentes oficiales: WFS del DERA y SIMA/IECA.
- Retorno de datos en formatos GeoDataFrame (GeoPandas) y DataFrame (Pandas).
- Visualización integrada con Folium y Plotly.
- Sistema de caché local para optimizar descargas.

## Instalación

```bash
pip install .
```

## Uso Rápido

```python
from quickdata import load_data, get_map, get_stats

# Cargar datos
df = load_data("municipios.csv")

# Obtener estadísticas
stats = get_stats(df, "poblacion")

# Visualizar
m = get_map()
```

## Requisitos

- Python >= 3.9
- pandas
- geopandas
- folium
- matplotlib
- plotly
