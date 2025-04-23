
import pandas as pd

def resumen_variables(df, formatear_numeros=True):
    """
    Genera una tabla resumen con el número de observaciones, valores faltantes y valores únicos por variable.

    Parámetros:
    - df: DataFrame de entrada.
    - formatear_numeros: Si True, formatea los números con comas (ej. 1,000).

    Retorna:
    - DataFrame resumen.
    """
    resumen = pd.DataFrame({
        "Variable": df.columns,
        "No. Observaciones": df.notnull().sum().values,
        "No. Faltantes": df.isnull().sum().values,
        "No. Únicos": df.nunique().values
    })

    if formatear_numeros:
        resumen_format = resumen.copy()
        columnas_a_formatear = ["No. Observaciones", "No. Faltantes", "No. Únicos"]
        resumen_format[columnas_a_formatear] = resumen[columnas_a_formatear].applymap(lambda x: f"{x:,}")
        return resumen_format
    else:
        return resumen
