from scipy import stats
import numpy as np
import pandas as pd

def intervalo_confianza_xbar(dataframe, variable=None, confidence_coeff=0.95):
    """
    Calcula intervalos de confianza para variables numéricas en un DataFrame.
    Parámetros:
    - dataframe: pandas.DataFrame
        El conjunto de datos que contiene las variables numéricas a analizar.
    - variable: str o None (opcional)
        El nombre de la columna a analizar. Si se deja como None, se analizan todas las variables numéricas.
    - confidence_coeff: float (opcional, default=0.95)
        El coeficiente de confianza. Debe estar entre 0 y 1, sin incluir los extremos.

    Retorna:
    - pandas.DataFrame con estadísticas e intervalos de confianza para cada variable.
    """
    alpha = 1 - confidence_coeff
    
    def compute_ci(series):
        serie_limpia = series.dropna()
        n = len(serie_limpia)
        mean = np.mean(serie_limpia)
        std_error = stats.sem(serie_limpia, nan_policy="omit")
        t_crit = stats.t.ppf(1 - alpha / 2, df= n - 1)
        margin = t_crit * std_error

        return {"Variable": series.name,
                "Obs (n)": n,
                "Media": round(mean, 2),
                "IC Inf.": round(mean - margin, 2),
                "IC Sup.": round(mean + margin, 2),
                "t-crítico": round(t_crit, 4),
                "Confianza": f"{int(confidence_coeff * 100)}%"
                }

    resultados = []
    if variable is None:
        for col in dataframe.select_dtypes(include=[np.number]).columns:
            resultados.append(compute_ci(dataframe[col]))
    else:
        if variable not in dataframe.columns:
            raise ValueError(f"La columna '{variable}' no está en el DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[variable]):
            raise ValueError(f"La columna '{variable}' no es numérica.")
        resultados.append(compute_ci(dataframe[variable]))
    
    return pd.DataFrame(resultados)