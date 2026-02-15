import pandas as pd

def trf_control(df_rechazos):
    df_rechazos["MOTIVO_RECHAZO"] = df_rechazos.apply(
    lambda r: "monto no valido" if r["AMOUNT"] <= 0 else "cliente no valido",
    axis=1)
    df_rechazos = df_rechazos[["TRANSACTION_ID", "CUSTOMER_ID", "AMOUNT", "MOTIVO_RECHAZO"]]
    return df_rechazos