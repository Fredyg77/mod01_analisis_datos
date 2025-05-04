
import inspect

def generar_IDS(df_name):
    # Obtener el nombre real del DataFrame como string
    nombre_df = [name for name, val in inspect.currentframe().f_back.f_locals.items() if val is df_name]
    nombre_df = nombre_df[0] if nombre_df else "DataFrame"

    # Crear copias seguras de columnas y generar ID2 y ID3
    d_frame = df_name.copy()
    d_frame["DIRECTORIO"] = d_frame["DIRECTORIO"].astype(str)
    d_frame["SECUENCIA_P"] = d_frame["SECUENCIA_P"].astype(str).zfill(2)
    d_frame["SECUENCIA_ENCUESTA"] = d_frame["SECUENCIA_ENCUESTA"].astype(str).zfill(2)
    d_frame["ID2"] = d_frame["DIRECTORIO"] + d_frame["SECUENCIA_P"]
    d_frame["ID3"] = d_frame["DIRECTORIO"] + d_frame["SECUENCIA_P"] + d_frame["SECUENCIA_ENCUESTA"]

    # Reordenar columnas
    columnas = ["ID3", "ID2"] + [col for col in d_frame.columns if col not in ["ID2", "ID3"]]
    d_frame = d_frame[columnas]

    # Impresión informativa automática
    print("=" * 80)
    print(f"Resumen de IDs generados en [{nombre_df}]:")
    print(f"- Registros únicos en [DIRECTORIO]: {d_frame['DIRECTORIO'].nunique()}")
    print(f"- Registros únicos en [ID2 = DIRECTORIO + SECUENCIA_P]: {d_frame['ID2'].nunique()}")
    print(f"- Registros únicos en [ID3 = DIRECTORIO + SECUENCIA_P + SECUENCIA_ENCUESTA]: {d_frame['ID3'].nunique()}")
    print("=" * 80)

    return d_frame
