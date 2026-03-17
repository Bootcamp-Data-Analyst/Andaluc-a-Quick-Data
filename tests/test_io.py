import pytest
import pandas as pd
import os
from quickdata.io import load_data
from quickdata.stats import get_stats

def test_load_csv(tmp_path):
    """Prueba la carga de archivos CSV."""
    d = tmp_path / "test.csv"
    df_orig = pd.DataFrame({'municipio': ['Sevilla', 'Málaga'], 'poblacion': [681998, 578460]})
    df_orig.to_csv(d, index=False)
    
    df_loaded = load_data(str(d))
    assert df_loaded.shape == (2, 2)
    assert 'municipio' in df_loaded.columns

def test_load_invalid_extension():
    """Prueba que lanza error con extensiones no validas."""
    with pytest.raises(ValueError, match="Extensión no soportada"):
        load_data("archivo.txt")

def test_stats():
    """Prueba del cálculo de estadísticas."""
    df = pd.DataFrame({'dato': [10, 20, 30]})
    stats = get_stats(df, 'dato')
    assert stats['mean'] == 20
    assert stats['max'] == 30
    assert stats['min'] == 10
