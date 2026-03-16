import catalogador
import extractor
import logging

# Configuración de logs para ver qué pasa en consola
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    # 1. PASO OBLIGATORIO: Actualizar el catálogo para mapear nombres oficiales
    catalogador.actualizar_diccionario_dera()
    
    # 2. Definir qué queremos descargar y cómo llamarlo en la carpeta /data
    # Las claves deben coincidir con las del JSON (minúsculas)
    
    # 2. Definir qué queremos descargar (Nombres corregidos para el catálogo)
    mapeo_descargas = {
        'g12_04_farmacia': 'farmacia.geojson',
        'g12_02_hospital_cae': 'hospital.geojson',
        'g12_01_centrosalud': 'resultados_salud.geojson',
        'g01_01_poblacion': 'poblaciones.geojson', # Cambiado 'poblaciones' -> 'poblacion'
        'g05_01_zonaverde': 'zona_verde.geojson'   # Cambiado 'zona_verde' -> 'zonaverde'
    }
    print("\n--- Iniciando Procesamiento de Datos Geográficos ---")
    
    for clave, nombre_archivo in mapeo_descargas.items():
        extractor.descargar_capa(clave, archivo_salida=nombre_archivo)
    
    print("\n✅ Proceso completado. Todos los archivos están en la carpeta /data")

if __name__ == "__main__":
    main()