import pandas as pd

def get_stats(df, column_name):
    """
    Calcula estadísticas básicas de una columna específica.
    """
    if df is None or column_name not in df.columns:
        return {}
        
    return {
        'mean': df[column_name].mean(),
        'max': df[column_name].max(),
        'min': df[column_name].min(),
        'count': len(df)
    }
