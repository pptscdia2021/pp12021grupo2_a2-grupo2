import investpy_spain as invest
import yahoofinance
import pandas as pd

def obtenerGananciaPerdida(df, columna, cant):
  df = df.sort_values(by=columna, ascending = False)
  print("Acciones de mayor ganancia\n",df.head(cant))
  print("Acciones de mayor pérdida\n",df.tail(cant))

if __name__ == "__main__":
   #Obtener la tabla en tiempo real de la bolsa de españa
   invest.obtenerDatosInvestpy()

   df_investpy = pd.read_csv('TP2 Webscraping&api\\csv\\investpy_spain.csv')
   accionesAevaluar = ['ANA', 'BBVA', 'GRLS', 'ELE', 'REP']
   print(df_investpy[df_investpy.symbol.isin(accionesAevaluar)])

   accionesAevaluar = ["ORI", "ANA.MC", "BBVA.MC", "GRF.MC", "ELE.MC"]
   yahoofinance.obtenerDatos(accionesAevaluar)
   df_yfinance = pd.read_csv('TP2 Webscraping&api\\csv\\yahoo_finance.csv')
   print (df_yfinance)

   #Objetivo 2
   obtenerGananciaPerdida(df_investpy, 'G/P', 2)