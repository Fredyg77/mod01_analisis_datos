def generar_ids(df, directorio_col="DIRECTORIO", secuencia_p_col="SECUENCIA_P", secuencia_encuesta_col="SECUENCIA_ENCUESTA", verbose=True, nombre_df="DataFrame"):
    """
    Genera los IDs ID2 e ID3 a partir de las columnas del DataFrame.
    
    Args:
    df (DataFrame): El DataFrame donde se encuentran las columnas necesarias.
    directorio_col (str): El nombre de la columna 'DIRECTORIO'. Por defecto es "DIRECTORIO".
    secuencia_p_col (str): El nombre de la columna 'SECUENCIA_P'. Por defecto es "SECUENCIA_P".
    secuencia_encuesta_col (str): El nombre de la columna 'SECUENCIA_ENCUESTA'. Por defecto es "SECUENCIA_ENCUESTA".
    verbose (bool): Si True, imprime información sobre los registros y los IDs generados.
    nombre_df (str): Nombre del DataFrame a mostrar en la impresión. Por defecto es "DataFrame".
    
    Returns:
    DataFrame: El DataFrame con las columnas ID2 e ID3 agregadas.
    """
    # Verificar si las columnas necesarias existen en el DataFrame
    required_columns = [directorio_col, secuencia_p_col, secuencia_encuesta_col]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        raise ValueError(f"Faltan las siguientes columnas en el DataFrame: {', '.join(missing_columns)}")
    
    # Convertir las columnas a tipo string y aplicar zfill cuando sea necesario
    df[directorio_col] = df[directorio_col].astype(str)
    df[secuencia_p_col] = df[secuencia_p_col].astype(str).str.zfill(2)
    df[secuencia_encuesta_col] = df[secuencia_encuesta_col].astype(str).str.zfill(2)
    
    # Crear las columnas ID2 y ID3
    df["ID2"] = df[directorio_col] + df[secuencia_p_col]
    df["ID3"] = df[directorio_col] + df[secuencia_p_col] + df[secuencia_encuesta_col]
    
    # Reordenar las columnas para colocar ID3 e ID2 al principio
    columnas_reordenadas = ["ID3", "ID2"] + [col for col in df.columns if col not in ["ID3", "ID2"]]
    df = df[columnas_reordenadas]
    
    # Impresión informativa
    if verbose:
        print(f"Procesado {nombre_df}: {df.shape[0]} registros")
        print("=" * 100)
        print(f"Número de registros únicos en [{directorio_col}]: {df[directorio_col].nunique()}")
        print(f"Número de registros únicos en [ID2 = {directorio_col} + {secuencia_p_col}]: {df['ID2'].nunique()}")
        print(f"Número de registros únicos en [ID3 = {directorio_col} + {secuencia_p_col} + {secuencia_encuesta_col}]: {df['ID3'].nunique()}")
        print("=" * 100)
    
    return df