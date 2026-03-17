import pytest
import pandas as pd
import geopandas as gpd
import folium
import matplotlib
import quickdata

def test_libraries_installed():
    """Verifica que las librerías principales de análisis están disponibles."""
    assert pd.__version__ is not None
    assert gpd.__version__ is not None
    assert folium.__name__ == 'folium'
    assert matplotlib.__name__ == 'matplotlib'

def test_package_discoverable():
    """Verifica que el paquete del proyecto se puede importar correctamente."""
    assert quickdata.__name__ == "quickdata"

def test_pandas_basic():
    """Verifica que pandas funciona correctamente con una operación básica."""
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    assert df.shape == (2, 2)
    assert df['a'].sum() == 3

def test_geopandas_basic():
    """Verifica que geopandas esta listo para manejar datos espaciales."""
    from shapely.geometry import Point
    d = {'col1': ['name1'], 'geometry': [Point(1, 2)]}
    gdf = gpd.GeoDataFrame(d, crs="EPSG:4326")
    assert gdf.crs.to_string() == "EPSG:4326"
