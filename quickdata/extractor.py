import json
import geopandas as gpd
import os

def cargar_diccionario(ruta="diccionarios/capas_dera.json"):
    if not os.path.exists(ruta):
        print("⚠️ El diccionario no existe. Ejecuta el catalogador.")
        return None
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def descargar_capa(nombre_amigable, archivo_salida=None):
    diccionario = cargar_diccionario()
    
    if not diccionario or nombre_amigable not in diccionario:
        print(f"❌ Error: La capa '{nombre_amigable}' no existe en el catálogo.")
        return None
        
    nombre_oficial = diccionario[nombre_amigable]
    
    # DINÁMICO: Extraemos el prefijo del servidor (ej: DERA_g01_servicios)
    servidor = nombre_oficial.split(':')[0]
    url_base = f"https://www.ideandalucia.es/services/{servidor}/wfs"
    
    params = (
        f"?service=wfs&version=2.0.0&request=GetFeature"
        f"&typeNames={nombre_oficial}&outputFormat=application/json"
    )
    
    try:
        print(f"📥 Descargando {nombre_amigable} desde {servidor}...")
        # Usamos pyogrio para mayor velocidad
        gdf = gpd.read_file(url_base + params, engine="pyogrio")
        
        if archivo_salida:
            os.makedirs('data/', exist_ok=True)
            ruta_final = os.path.join('data/', archivo_salida)
            gdf.to_file(ruta_final, driver='GeoJSON')
            print(f"💾 Guardado correctamente en: {ruta_final}")
            
        return gdf
    except Exception as e:
        print(f"❌ Error crítico en la descarga de {nombre_amigable}: {e}")
        return None