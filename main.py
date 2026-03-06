import geopandas as gpd
import logging

# Configuración básica de logs para monitorear la descarga
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def extraer_datos_wfs(url, capa):
    """Extrae el GeoDataFrame desde el servicio WFS."""
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

def limpiar_datos(gdf, tipo_capa):
    """Lógica de limpieza basada en tu archivo de referencia"""
    if gdf is None or gdf.empty:
        return None
    
    # Definición de columnas a borrar según el tipo de servicio
    columnas_eliminar = {
        'centros': ['gml_id', 'id_dera', 'nombre', 'direccion', 'telefono', 'web', 'localidad', 'cod_mun'],
        'hospitales': ['gml_id', 'id_dera', 'web', 'cod_mun'],
        'farmacias': ['gml_id', 'id_dera', 'telefono', 'cod_mun'] # Siguiendo el patrón de tu código
    }
    
    cols = columnas_eliminar.get(tipo_capa, [])
    # Solo borramos las columnas si existen en el GDF actual
    existentes = [c for c in cols if c in gdf.columns]
    
    logging.info(f"Limpiando {len(existentes)} columnas de la capa {tipo_capa}.")
    return gdf.drop(columns=existentes)

def main():
    url_base = "https://www.ideandalucia.es/services/DERA_g12_servicios/wfs?service=wfs&request=getcapabilities"
    
    # Mapeo de capas según tu notebook
    capas_a_procesar = {
        'centros': 'DERA_g12_servicios:g12_01_CentroSalud',
        'hospitales': 'DERA_g12_servicios:g12_02_Hospital_CAE',
        'farmacias': 'DERA_g12_servicios:g12_04_Farmacia'
    }
    
    resultados = {}

    for clave, nombre_capa in capas_a_procesar.items():
        # 1. Extracción
        gdf_raw = extraer_datos_wfs(url_base, nombre_capa)
        
        # 2. Limpieza
        if gdf_raw is not None:
            gdf_clean = limpiar_datos(gdf_raw, clave)
            resultados[clave] = gdf_clean
            print(f"--- Vista previa de {clave} ---")
            print(gdf_clean.head(), "\n")
    
    return resultados

if __name__ == "__main__":
    dict_datasets = main()