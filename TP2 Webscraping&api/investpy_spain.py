import investpy
import pandas as pd


#Obtener la tabla en tiempo real de la bolsa de españa
#parámetros: país, as_jon(true/false) para devolver una tabla o no (opcional), n_results para cantidad de acciones)

def obtenerDatosInvestpy():
    df = investpy.stocks.get_stocks_overview(country='spain', as_json = False , n_results = 35)
        
    df = porcentajeCambio(df)
    #cambiar la columna a numérica
    df['GP'] = df['GP'].apply(pd.to_numeric)
    df.to_csv("TP2 Webscraping&api\\csv\\investpy_spain.csv")

#quitar el carácter '%' de change:percentage y renombrar la columna ocmo GP
def porcentajeCambio(df):
    return df.join(df['change_percentage'].str.partition('%')[[0, 1]]).rename({0: 'GP', 1: '%'}, axis=1)



