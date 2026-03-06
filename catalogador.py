import urllib.request
import xml.etree.ElementTree as ET
import json
import os

def actualizar_diccionario_dera(ruta_salida="diccionarios/capas_dera.json"):
    print("🔄 Conectando con la Junta de Andalucía para auditar capas...")
    
    # URL del servicio WFS de la Junta (GetCapabilities)
    url_wfs = "https://www.ideandalucia.es/services/DERA_g12_servicios/wfs?service=wfs&version=2.0.0&request=GetCapabilities"
    
    try:
        # Añadimos un User-Agent para evitar que el firewall nos bloquee por parecer un bot
        req = urllib.request.Request(url_wfs, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=15)
        
        # Parseamos el XML
        tree = ET.parse(response)
        root = tree.getroot()
        
        capas_disponibles = {}
        
        # Buscamos todas las etiquetas que contengan 'Name' (ignorando namespaces complicados)
        for elem in root.iter():
            if 'Name' in elem.tag and elem.text and 'g12' in elem.text:
                # Ejemplo de elem.text: 'DERA_g12_servicios:g12_01_CentroSalud'
                nombre_crudo = elem.text
                # Creamos un nombre amigable para nuestro diccionario
                nombre_amigable = nombre_crudo.split(':')[-1].lower()
                capas_disponibles[nombre_amigable] = nombre_crudo

        # Guardamos el resultado en un JSON
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(capas_disponibles, f, indent=4)
            
        print(f"✅ Diccionario actualizado con {len(capas_disponibles)} capas vigentes.")
        return capas_disponibles

    except Exception as e:
        print(f"❌ Error al auditar el servicio WFS: {e}")
        return None