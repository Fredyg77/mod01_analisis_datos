
import pandas as pd

def generar_IDS(df_name):
    # Verifica que el objeto recibido sea un DataFrame de pandas
    if not isinstance(df_name, pd.DataFrame):
        raise TypeError("Se esperaba un DataFrame, pero se recibió otro tipo de objeto.")

    # Lista de columnas necesarias para construir los identificadores
    required_columns = ["DIRECTORIO", "SECUENCIA_P", "SECUENCIA_ENCUESTA"]
    
    # Identifica si falta alguna de las columnas requeridas
    missing_columns = [col for col in required_columns if col not in df_name.columns]
    if missing_columns:
        raise ValueError(f"Faltan las siguientes columnas en el DataFrame: {', '.join(missing_columns)}")

    # Convierte las columnas a texto y aplica zfill para asegurar formato con ceros a la izquierda
    df_name["DIRECTORIO"] = df_name["DIRECTORIO"].astype(str)
    df_name["SECUENCIA_P"] = df_name["SECUENCIA_P"].astype(str).str.zfill(2)
    df_name["SECUENCIA_ENCUESTA"] = df_name["SECUENCIA_ENCUESTA"].astype(str).str.zfill(2)

    # Crea la columna ID2 concatenando DIRECTORIO y SECUENCIA_P
    df_name["ID2"] = df_name["DIRECTORIO"] + df_name["SECUENCIA_P"]

    # Crea la columna ID3 concatenando ID2 y SECUENCIA_ENCUESTA
    df_name["ID3"] = df_name["ID2"] + df_name["SECUENCIA_ENCUESTA"]

    # Reorganiza las columnas para que ID2 e ID3 aparezcan al principio
    columnas_reordenadas = ["ID3", "ID2"] + [col for col in df_name.columns if col not in ["ID2", "ID3"]]
    df_name = df_name[columnas_reordenadas]

    # Imprime información útil para verificar el resultado
    print("=" * 80)
    print("Procesado DataFrame con ID2 e ID3")
    print(f"Número de registros únicos en [DIRECTORIO]: {df_name['DIRECTORIO'].nunique()}")
    print(f"Número de registros únicos en [ID2 = DIRECTORIO + SECUENCIA_P]: {df_name['ID2'].nunique()}")
    print(f"Número de registros únicos en [ID3 = ID2 + SECUENCIA_ENCUESTA]: {df_name['ID3'].nunique()}")
    print("=" * 100)

    # Retorna el DataFrame modificado
    return df_name
