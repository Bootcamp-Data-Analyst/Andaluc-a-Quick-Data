import folium
import plotly.express as px

def get_map(center=[37.3891, -5.9845], zoom=7):
    """
    Crea un mapa base de Andalucía centrado en Sevilla.
    """
    return folium.Map(location=center, zoom_start=zoom)

def plot_choropleth(gdf, column, title="Mapa Coroplético"):
    """
    Genera un mapa coroplético usando GeoPandas y Plotly.
    """
    # Implementación básica usando plotly para visualización rápida
    fig = px.choropleth(gdf, 
                        geojson=gdf.geometry, 
                        locations=gdf.index, 
                        color=column,
                        title=title)
    fig.update_geos(fitbounds="locations", visible=False)
    return fig
