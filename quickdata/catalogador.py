import urllib.request
import xml.etree.ElementTree as ET
import json
import os

def actualizar_diccionario_dera(ruta_salida="diccionarios/capas_dera.json"):
    print("🔄 Conectando con la Junta de Andalucía para auditar capas...")
    
    # URL del servicio WFS de la Junta (GetCapabilities)
    url_wfs = "https://www.ideandalucia.es/services/DERA_g12_servicios/wfs?service=wfs&version=2.0.0&request=GetCapabilities"
    
    try:
        req = urllib.request.Request(url_wfs, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=15)
        
        tree = ET.parse(response)
        root = tree.getroot()
        
        capas_disponibles = {}
        
        for elem in root.iter():
            # Eliminamos la restricción de 'g12' para poder capturar otras categorías si es necesario
            if 'Name' in elem.tag and elem.text:
                nombre_crudo = elem.text
                nombre_amigable = nombre_crudo.split(':')[-1].lower()
                capas_disponibles[nombre_amigable] = nombre_crudo

        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(capas_disponibles, f, indent=4)
            
        print(f"✅ Diccionario actualizado con {len(capas_disponibles)} capas vigentes.")
        return capas_disponibles

    except Exception as e:
        print(f"❌ Error al auditar el servicio WFS: {e}")
        return None