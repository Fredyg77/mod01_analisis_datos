import pandas as pd

def generar_IDS(df_name):
    # Verificar si las columnas necesarias existen en el DataFrame
    required_columns = ["DIRECTORIO", "SECUENCIA_P", "SECUENCIA_ENCUESTA"]
    missing_columns = [col for col in required_columns if col not in df_name.columns]
    
    if missing_columns:
        raise ValueError(f"Faltan las siguientes columnas en el DataFrame: {', '.join(missing_columns)}")
    
    # Convertir las columnas a tipo string y aplicar zfill cuando sea necesario
    df_name["DIRECTORIO"] = df_name["DIRECTORIO"].astype(str)
    df_name["SECUENCIA_P"] = df_name["SECUENCIA_P"].apply(lambda x: str(x).zfill(2))
    df_name["SECUENCIA_ENCUESTA"] = df_name["SECUENCIA_ENCUESTA"].apply(lambda x: str(x).zfill(2))
    
    # Crear las columnas ID2 y ID3
    df_name["ID2"] = df_name["DIRECTORIO"] + df_name["SECUENCIA_P"]
    df_name["ID3"] = df_name["DIRECTORIO"] + df_name["SECUENCIA_P"] + df_name["SECUENCIA_ENCUESTA"]
    
    # Reordenar las columnas para poner ID2 y ID3 al principio
    columnas_reordenadas = ["ID3", "ID2"] + [col for col in df_name.columns if col not in ["ID3", "ID2"]]
    df_name = df_name[columnas_reordenadas]
    
    # Impresión informativa con el nombre del DataFrame
    print("=" * 80)
    print(f"Procesado DataFrame: {df_name}")
    print(f"Número de registros únicos en [DIRECTORIO]: {df_name['DIRECTORIO'].nunique()}")
    print(f"Número de registros únicos en [ID2 = DIRECTORIO + SECUENCIA_P]: {df_name['ID2'].nunique()}")
    print(f"Número de registros únicos en [ID3 = DIRECTORIO + SECUENCIA_P + SECUENCIA_ENCUESTA]: {df_name['ID3'].nunique()}")
    print("=" * 100)
    
    return df_name
