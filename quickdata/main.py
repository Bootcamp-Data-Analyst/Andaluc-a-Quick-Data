import catalogador
import extractor
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    # 1. Sincronización inicial
    catalogador.actualizar_diccionario_dera()
    
    # 2. Definición de tareas (CLAVE DEL JSON : NOMBRE ARCHIVO FINAL)
    # He corregido 'poblacion' y 'zonaverde' según el estándar de la Junta
    mapeo_descargas = {
        'g12_04_farmacia': 'farmacia.geojson',
        'g12_02_hospital_cae': 'hospital.geojson',
        'g12_01_centrosalud': 'resultados_salud.geojson',
        'g01_01_poblacion': 'poblaciones.geojson',
        'g05_01_zonaverde': 'zona_verde.geojson'
    }
    
    print("\n🚀 INICIANDO PROCESO DE EXTRACCIÓN...")
    
    for clave, archivo_destino in mapeo_descargas.items():
        extractor.descargar_capa(clave, archivo_salida=archivo_destino)
    
    print("\n✨ ¡Todo listo! Los archivos están en la carpeta /data")

if __name__ == "__main__":
    main()