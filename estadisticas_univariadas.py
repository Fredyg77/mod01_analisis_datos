from scipy import stats
import numpy as np
import pandas as pd

def estadisticas_basicas(dataframe, variable, group_by=None):
    """
    Calcula un resumen de estadísticas univariadas para una variable numérica en un DataFrame.

    Si se especifica un grupo (group_by), calcula las estadísticas por cada grupo.
    Si no se especifica, calcula las estadísticas para toda la muestra.

    Estadísticas incluidas:
    - n obs.: número de observaciones no nulas
    - n faltantes: número de datos faltantes
    - Promedio
    - Desviación estándar
    - Coeficiente de variación
    - Máximo y mínimo
    - Moda (valor más frecuente)
    - Mediana
    - Cuartiles (Q1 y Q3)
    - Rango intercuartílico
    - Asimetría
    - Curtosis

    Parámetros:
    - dataframe (pd.DataFrame): conjunto de datos.
    - variable (str): nombre de la columna numérica a analizar.
    - group_by (str, opcional): nombre de la columna por la cual agrupar los resultados.

    Retorna:
    - pd.DataFrame: tabla de estadísticas, agrupadas si se especifica group_by.
    """

    if variable not in dataframe.columns:
        raise ValueError(f"La columna '{variable}' no está en el DataFrame.")
    elif not pd.api.types.is_numeric_dtype(dataframe[variable]):
        raise ValueError(f"La columna '{variable}' no es numérica.")
    elif group_by is not None and group_by not in dataframe.columns:
        raise ValueError(f"La columna '{group_by}' no está en el DataFrame.")

    def resumen(x):
        return pd.Series({
            'n obs.': x.count(),
            'n faltantes': x.isna().sum(),
            'Promedio': round(x.mean(), 2),
            'Desv. Std': '-' if x.count() == 1 else round(x.std(), 2),
            'C. variac.': '-' if x.count() == 1 else round((x.std() / x.mean()) * 100, 2),
            'Máximo': x.max(),
            'Mínimo': x.min(),
            'Modas': round(x.mode().iloc[0], 2) if not x.mode().empty else np.nan,
            'Mediana': round(x.median(), 2),
            'Q1(25%)': round(x.quantile(0.25), 2),
            'Q3(75%)': round(x.quantile(0.75), 2),
            'R. Interc.': round(x.quantile(0.75) - x.quantile(0.25), 2),
            'Asimetría': round(stats.skew(x, nan_policy='omit'), 2),
            'Curtosis': round(stats.kurtosis(x, nan_policy='omit'), 2)
        })

    if group_by:
        df_resumen = dataframe.groupby(group_by)[variable].apply(resumen).unstack()
    else:
        df_resumen = resumen(dataframe[variable])
        df_resumen = pd.DataFrame(df_resumen, columns=['Estadística']).rename(columns={'Estadística': variable})
        df_resumen.index.name = 'Estadística'

    return df_resumen
