
import pandas as pd

def resumen_bigotes_por_categoria(df, columna_categoria, columna_valores):
    """
    Calcula los cuartiles, el IQR, los límites teóricos y los bigotes reales para las diferentes categorías 
    que pertenecen a una variable categórica.

    Parámetros:
    df (DataFrame): El DataFrame original.
    columna_categoria (str): Nombre de la columna categórica.
    columna_valores (str): Nombre de la columna numérica.

    Retorna:
    DataFrame con Q1, Q3, IQR, límites teóricos y bigotes reales por categoría.
    """
    # Eliminar las filas que poseen valores nulos (NaN) en cualquiera de estas dos columnas:
    df_limpio = df.dropna(subset=[columna_categoria, columna_valores])
    resultados = []

    for categoria, grupo in df_limpio.groupby(columna_categoria):
        valores = grupo[columna_valores]      # Extrae solo la columna numérica de interés para ese grupo.
        q1 = valores.quantile(0.25)
        q3 = valores.quantile(0.75)
        iqr = q3 - q1
        lim_inf = q1 - 1.5 * iqr  
        lim_sup = q3 + 1.5 * iqr

        # Valores dentro del rango permitido (no outliers)
        dentro = valores[(valores >= lim_inf) & (valores <= lim_sup)]

        bigote_inf_real = dentro.min()
        bigote_sup_real = dentro.max()

        resultados.append({
            columna_categoria: categoria,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Lím. infer. teór.": lim_inf,
            "Lím. super. teór.": lim_sup,
            "Val. infer. real": bigote_inf_real,
            "Val. super. real": bigote_sup_real
        })

    return pd.DataFrame(resultados)
