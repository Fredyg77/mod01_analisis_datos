
import pandas as pd

def generar_IDS(data_frame):
    """
    Genera las columnas ID2 e ID3 en un DataFrame, usando las columnas 'DIRECTORIO', 'SECUENCIA_P', 
    y 'SECUENCIA_ENCUESTA'. Además, reorganiza las columnas y devuelve el DataFrame actualizado.

    Args:
    - data_frame (pd.DataFrame): El DataFrame de entrada con las columnas 'DIRECTORIO', 'SECUENCIA_P',
      y 'SECUENCIA_ENCUESTA'.

    Returns:
    - pd.DataFrame: El DataFrame con las columnas ID2, ID3 generadas y reorganizadas.
    """
    
    # Aseguramos que las columnas sean de tipo string
    data_frame['SECUENCIA_P'] = data_frame['SECUENCIA_P'].astype(str).str.zfill(2)
    data_frame['SECUENCIA_ENCUESTA'] = data_frame['SECUENCIA_ENCUESTA'].astype(str).str.zfill(2)
    
    # Generar las nuevas columnas ID2 e ID3
    data_frame["ID2"] = data_frame["DIRECTORIO"] + data_frame["SECUENCIA_P"]
    data_frame["ID3"] = data_frame["DIRECTORIO"] + data_frame["SECUENCIA_P"] + data_frame["SECUENCIA_ENCUESTA"]

    # Reordenar las columnas para poner ID2 y ID3 al principio
    columnas_reordenadas = ["ID3", "ID2"] + [col for col in data_frame.columns if col not in ["ID3", "ID2"]]
    data_frame = data_frame[columnas_reordenadas]
    
    # Imprimir el nombre del DataFrame junto con los registros únicos
    print("=" * 80)
    print(f"Análisis del DataFrame: {data_frame.name if hasattr(data_frame, 'name') else 'Desconocido'}")
    print(f"Número de registros únicos en [DIRECTORIO]: {data_frame['DIRECTORIO'].nunique()}")
    print(f"Número de registros únicos en [ID2 = DIRECTORIO + SECUENCIA_P]: {data_frame['ID2'].nunique()}")
    print(f"Número de registros únicos en [ID3 = DIRECTORIO + SECUENCIA_P + SECUENCIA_ENCUESTA]: {data_frame['ID3'].nunique()}")
    print("=" * 100)

    return data_frame
