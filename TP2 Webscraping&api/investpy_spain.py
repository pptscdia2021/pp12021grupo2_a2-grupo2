import investpy
import pandas as pd


#Obtener la tabla en tiempo real de la bolsa de españa

def obtenerDatosInvestpy():
   return investpy.stocks.get_stocks_overview(country='spain', as_json = False , n_results = 35)
        
df = obtenerDatosInvestpy()

#Guardar datos en csv
def cargarTablaEnCsv():
  df.to_csv("TP2 Webscraping&api\\csv\\investpy_spain.csv")

#guardar = cargarTablaEnCsv()
