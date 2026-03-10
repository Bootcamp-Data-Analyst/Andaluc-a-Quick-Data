import geopandas as gpd
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def extraer_datos_wfs(url, capa):
    """Extrae el GeoDataFrame desde el servicio WFS en bruto."""
    try:
        logging.info(f"Descargando capa: {capa}...")
        gdf = gpd.read_file(
            url, 
            layer=capa, 
            engine="pyogrio", 
            encoding="utf-8"
        )
        return gdf
    except Exception as e:
        logging.error(f"Error al conectar con el servicio para {capa}: {e}")
        return None

def main():
    url_base = "https://www.ideandalucia.es/services/DERA_g12_servicios/wfs?service=wfs&request=getcapabilities"
    
    # Mapeo de los servicios WFS a los 5 datasets del Mapping
    
    capas_a_procesar = {
        'farmacias': 'DERA_g12_servicios:g12_04_Farmacia',
        'hospitales': 'DERA_g12_servicios:g12_02_Hospital_CAE',
        'salud': 'DERA_g12_servicios:g12_01_CentroSalud',
        'poblaciones': 'DERA_g01_servicios:g01_01_Poblacion', 
        'zonas_verdes': 'DERA_g05_servicios:g05_01_ZonaVerde' 
    }
    
    # Nombres exactos que espera el archivo 'Mapping'
    archivos_salida = {
        'farmacias': 'farmacia.geojson',
        'hospitales': 'hospital.geojson',
        'poblaciones': 'poblaciones.geojson',
        'salud': 'resultados_salud.geojson',
        'zonas_verdes': 'zona_verde.geojson'
    }
    
    # Creamos el directorio 'data/' que usa Mapping si no existe
    os.makedirs('data/', exist_ok=True)
    resultados = {}

    for clave, nombre_capa in capas_a_procesar.items():
        # 1. Extracción pura
        gdf_raw = extraer_datos_wfs(url_base, nombre_capa)
        
        # 2. Guardado sin alteraciones
        if gdf_raw is not None:
            resultados[clave] = gdf_raw
            ruta_destino = os.path.join('data/', archivos_salida[clave])
            
            # Guardamos como GeoJSON para que 'Mapping' lo consuma directamente
            gdf_raw.to_file(ruta_destino, driver="GeoJSON")
            logging.info(f"Guardado exitosamente -> {ruta_destino}")
            
    return resultados

if __name__ == "__main__":
    dict_datasets = main()