import investpy_spain as invest
import yahoofinance
import pandas as pd

if __name__ == "__main__":
   #Obtener la tabla en tiempo real de la bolsa de españa
   invest.obtenerDatosInvestpy()

   #Guardar datos en csv
   invest.cargarTablaEnCsv()

   df_investpy = pd.read_csv('TP2 Webscraping&api\\csv\\investpy_spain.csv')
   accionesAevaluar = ['ANA', 'BBVA', 'GRLS', 'ELE', 'REP']
   print(df_investpy[df_investpy.symbol.isin(accionesAevaluar)])

   accionesAevaluar = ["ORI", "ANA.MC", "BBVA.MC", "GRF.MC", "ELE.MC"]
   yahoofinance.obtenerDatos(accionesAevaluar)
   df_yfinance = pd.read_csv('TP2 Webscraping&api\\csv\\yahoo_finance.csv')
   print (df_yfinance)
