import pandas as pd
import pathlib
import os

CACHE_DIR = pathlib.Path(".aqd_cache")

def load_data(file_path):
    """
    Carga un archivo CSV o Excel basado en su extensión.
    """
    path = pathlib.Path(file_path)
    
    # Comprobar caché (ejemplo de implementación pedida)
    cache_file = CACHE_DIR / f"cached_{path.name}"
    if cache_file.exists():
        print(f"Cargando desde caché: {cache_file}")
        # Lógica de carga desde caché...
    
    if path.suffix == '.csv':
        return pd.read_csv(file_path)
    elif path.suffix in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Extensión no soportada: {path.suffix}")

def clear_cache():
    """Limpia la caché local."""
    if CACHE_DIR.exists():
        for f in CACHE_DIR.iterdir():
            if f.is_file():
                f.unlink()
        print("Caché limpiada.")
