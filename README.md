Estructura del proyecto:

catalogador.py: Se conecta al servicio WFS de la Junta de Andalucía (DERA) para auditar las capas disponibles. Extrae los nombres oficiales y amigables de las capas y los guarda en un diccionario JSON (diccionarios/capas_dera.json). Es el primer paso para conocer qué datos hay disponibles.

extractor.py: Módulo auxiliar que lee el diccionario generado por el catalogador y proporciona una función (descargar_capa) para descargar los datos en bruto de una capa específica en formato GeoJSON utilizando la librería geopandas.

main.py: Es el script orquestador para la descarga automatizada. Define un mapeo de las 5 capas principales de interés (farmacias, hospitales, salud, poblaciones y zonas verdes) y las descarga en la carpeta data/.

Cleaning.ipynb: Cuaderno de Jupyter encargado de la transformación de datos (ETL). Descarga directamente las capas desde el WFS, limpia las tablas eliminando columnas innecesarias (como gml_id, id_dera, web, teléfonos, etc.) para aligerar los archivos, y exporta los resultados limpios a la carpeta data/ en formato GeoJSON.

Mapping.ipynb: Cuaderno de Jupyter dedicado a la visualización. Carga los archivos GeoJSON limpios, unifica el sistema de coordenadas (CRS EPSG:4326), calcula el centro del mapa dinámicamente y utiliza folium para generar un mapa interactivo en HTML (map/mapa_andalucia.html). Incluye controles de capas y marcadores de colores según el tipo de infraestructura.

Este proyecto extrae, limpia y visualiza datos geoespaciales públicos de la Junta de Andalucía a través de su servicio WFS (Web Feature Service). El objetivo principal es obtener información sobre infraestructuras clave (centros de salud, hospitales, farmacias, zonas verdes y poblaciones), procesarla para eliminar datos redundantes, y finalmente representarla en un mapa interactivo.


