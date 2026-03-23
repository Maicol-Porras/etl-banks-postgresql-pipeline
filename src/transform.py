from logger import log_progress


def transform_data(df):
    log_progress("Transform phase started")

    df.columns = df.columns.str.strip()

    # Mantener solo columnas necesarias
    df = df[["Bank", "Country", "Market_Cap_Billion_USD"]].copy()

    # Renombrar columnas para consistencia
    df.rename(columns={
        "Bank": "bank",
        "Country": "country",
        "Market_Cap_Billion_USD": "market_cap_usd"
    }, inplace=True)

    # Limpiar posibles nulos
    df.dropna(inplace=True)

    # Asegurar tipo numérico
    df["market_cap_usd"] = df["market_cap_usd"].astype(float)

    # Eliminar duplicados si existen
    df.drop_duplicates(inplace=True)

    log_progress("Transform phase completed")
    return df