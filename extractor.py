import json
import geopandas as gpd
import os

def cargar_diccionario(ruta="diccionarios/capas_dera.json"):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ No se encontró el diccionario. Ejecuta el catalogador primero.")
        return None

def descargar_capa(nombre_amigable, archivo_salida=None):
    diccionario = cargar_diccionario()
    
    if not diccionario or nombre_amigable not in diccionario:
        print(f"❌ La capa '{nombre_amigable}' no existe en el diccionario.")
        return None
        
    nombre_oficial = diccionario[nombre_amigable]
    print(f"📥 Descargando capa (en bruto): {nombre_oficial}...")
    
    url_base = "https://www.ideandalucia.es/services/DERA_g12_servicios/wfs"
    params = f"?service=wfs&version=2.0.0&request=GetFeature&typeNames={nombre_oficial}&outputFormat=application/json"
    url_completa = url_base + params
    
    try:
        gdf = gpd.read_file(url_completa, engine="pyogrio")
        print(f"✅ Descarga completada. {len(gdf)} registros obtenidos.")
        
        # Guardamos en la ruta esperada por Mapping si se indica el nombre de archivo
        if archivo_salida:
            os.makedirs('data/', exist_ok=True)
            ruta_completa = os.path.join('data/', archivo_salida)
            gdf.to_file(ruta_completa, driver='GeoJSON')
            print(f"💾 Guardado directo en: {ruta_completa}")
            
        return gdf
    except Exception as e:
        print(f"❌ Error al descargar los datos: {e}")
        return None