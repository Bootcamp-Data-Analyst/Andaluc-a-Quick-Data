import json
import geopandas as gpd

def cargar_diccionario(ruta="diccionarios/capas_dera.json"):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ No se encontró el diccionario. Ejecuta el catalogador primero.")
        return None

def descargar_capa(nombre_amigable):
    diccionario = cargar_diccionario()
    
    if not diccionario or nombre_amigable not in diccionario:
        print(f"❌ La capa '{nombre_amigable}' no existe en el diccionario.")
        return None
        
    nombre_oficial = diccionario[nombre_amigable]
    print(f"📥 Descargando capa: {nombre_oficial}...")
    
    # Construimos la URL de petición de la capa exacta (GetFeature)
    url_base = "https://www.ideandalucia.es/services/DERA_g12_servicios/wfs"
    params = f"?service=wfs&version=2.0.0&request=GetFeature&typeNames={nombre_oficial}&outputFormat=application/json"
    url_completa = url_base + params
    
    try:
        # Usamos pyogrio para máxima velocidad
        gdf = gpd.read_file(url_completa, engine="pyogrio")
        print(f"✅ Descarga completada. {len(gdf)} registros obtenidos.")
        return gdf
    except Exception as e:
        print(f"❌ Error al descargar los datos: {e}")
        return None