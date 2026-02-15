import pandas as pd

def trf_transactions(df_transactions,df_customers):
    df_resultado = pd.merge(df_transactions,df_customers,how="left",on="CUSTOMER_ID")
    
    df_filter = df_resultado[(df_resultado["CUSTOMER_NAME"].notna()) & (df_resultado["AMOUNT"] > 0)]
    df_rechazos = df_resultado[~((df_resultado["CUSTOMER_NAME"].notna()) & (df_resultado["AMOUNT"] > 0))]
    
    return df_filter, df_rechazos