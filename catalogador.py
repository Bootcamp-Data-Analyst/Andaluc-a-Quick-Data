import urllib.request
import xml.etree.ElementTree as ET
import json
import os

def actualizar_diccionario_dera(ruta_salida="diccionarios/capas_dera.json"):
    print("🔄 Audidatando servidores de la Junta (g01, g05, g12)...")
    
    # Lista de servidores para cubrir Salud, Población y Medio Ambiente
    servidores = ["DERA_g01_servicios", "DERA_g05_servicios", "DERA_g12_servicios"]
    capas_disponibles = {}

    for serv in servidores:
        url_wfs = f"https://www.ideandalucia.es/services/{serv}/wfs?service=wfs&version=2.0.0&request=GetCapabilities"
        try:
            req = urllib.request.Request(url_wfs, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=15)
            tree = ET.parse(response)
            root = tree.getroot()
            
            for elem in root.iter():
                # Buscamos elementos que contengan el nombre técnico de la capa
                if 'Name' in elem.tag and elem.text and ':' in elem.text:
                    nombre_completo = elem.text
                    # Creamos la clave amigable (ej: g01_01_poblacion)
                    clave_amigable = nombre_completo.split(':')[-1].lower()
                    capas_disponibles[clave_amigable] = nombre_completo
            print(f"✅ Servidor {serv} auditado con éxito.")
        except Exception as e:
            print(f"⚠️ Error al acceder al servidor {serv}: {e}")

    # Guardar el diccionario unificado
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(capas_disponibles, f, indent=4, ensure_ascii=False)
    
    print(f"📂 Catálogo final guardado con {len(capas_disponibles)} capas.")