import investpy
import pandas as pd

def cargarTablaEnCsv():
   #Obtener la tabla en tiempo real de la bolsa de españa
   df = investpy.stocks.get_stocks_overview(country='spain', as_json = False , n_results = 35)

   #Guardar datps en csv
   df.to_csv("TP2 Webscraping&api\\investpy_spain.csv")

