import oracledb
from Ext.ext import ext_transactions, ext_customers
from Trf.trf import trf_transactions
from Car.car import car_csv, rechazos_csv
from Control.trf_control import trf_control


def seq_ext():
    df_transactions = ext_transactions()
    df_customers = ext_customers()
    return df_transactions, df_customers

def seq_trf():
    df_filter, df_rechazos = trf_transactions(*seq_ext())
    return df_filter, df_rechazos

def seq_car():
    df_filter, df_rechazos = seq_trf()
    car_csv(df_filter)
    rechazos_csv(trf_control(df_rechazos))
    return

seq_car()

