import pandas as pd

def car_csv(df_filter):
    df_filter.to_csv(
        "salida.csv",
        index=False,
        sep=";",
        encoding="utf-8"
    )
    return

def rechazos_csv(df_rechazos):
    df_rechazos.to_csv(
        "rechazos.csv",
        index=False,
        sep=";",
        encoding="utf-8"
    )
    return