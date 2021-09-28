import investpy
import pandas as pd


#Obtener la tabla en tiempo real de la bolsa de españa

def obtenerDatosInvestpy():
    df = investpy.stocks.get_stocks_overview(country='spain', as_json = False , n_results = 35)
        
    df = porcentajeCambio(df)
    df['G/P'] = df['G/P'].apply(pd.to_numeric)
    df.to_csv("TP2 Webscraping&api\\csv\\investpy_spain.csv")

def porcentajeCambio(df):
    return df.join(df['change_percentage'].str.partition('%')[[0, 1]]).rename({0: 'G/P', 1: '%'}, axis=1)



