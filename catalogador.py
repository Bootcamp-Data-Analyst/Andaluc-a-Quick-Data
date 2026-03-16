import urllib.request
import xml.etree.ElementTree as ET
import json
import os

def actualizar_diccionario_dera(ruta_salida="diccionarios/capas_dera.json"):
    print("🔄 Conectando con la Junta de Andalucía para auditar capas...")
    
    # URL base para obtener capacidades (usamos g12 como base, pero el extractor será multiserver)
    url_wfs = "https://www.ideandalucia.es/services/DERA_g12_servicios/wfs?service=wfs&version=2.0.0&request=GetCapabilities"
    
    try:
        req = urllib.request.Request(url_wfs, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=15)
        tree = ET.parse(response)
        root = tree.getroot()
        
        capas_disponibles = {}
        # El namespace suele variar, iteramos por todos los elementos con 'Name'
        for elem in root.iter():
            if 'Name' in elem.tag and elem.text and ':' in elem.text:
                nombre_completo = elem.text # Ej: DERA_g12_servicios:g12_04_Farmacia
                # Creamos una clave simple: g12_04_farmacia
                clave_amigable = nombre_completo.split(':')[-1].lower()
                capas_disponibles[clave_amigable] = nombre_completo

        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(capas_disponibles, f, indent=4, ensure_ascii=False)
            
        print(f"✅ Diccionario actualizado: {len(capas_disponibles)} capas en '{ruta_salida}'")
        return capas_disponibles

    except Exception as e:
        print(f"❌ Error al auditar el servicio: {e}")
        return None