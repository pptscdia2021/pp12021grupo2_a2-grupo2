import investpy_spain as invest
import yahoofinance
import BolsaMadrid
import pandas as pd
import matplotlib.pyplot as plt
import objetivo_dos as odos


if __name__ == "__main__":
   #Obtener la tabla en tiempo real de la bolsa de españa
   invest.obtenerDatosInvestpy()
   BolsaMadrid.obtenerDatos()
   
   #Mostrar tabla en pantalla usando investpy
   print('TABLA DE DATOS BOLSA DE MADRID (USANDO investpy)')
   df_investpy = pd.read_csv('TP2 Webscraping&api\\csv\\investpy_spain.csv')
   accionesAevaluar = ['ANA', 'BBVA', 'GRLS', 'ELE', 'REP']
   print(df_investpy[df_investpy.symbol.isin(accionesAevaluar)])

   #Mostrar tabla en pantalla usando BeautiFoul Soup
   print('')
   print('TABLA DE DATOS BOLSA DE MADRID (USANDO BS4)')
   df_bolsaMadrid = pd.read_csv('TP2 Webscraping&api\\csv\\bolsaMadrid.csv')
   accionesAevaluar = ['ACCIONA', 'BBVA', 'GRIFOLS CL.A', 'ENDESA', 'REPSOL']
   print(df_bolsaMadrid[df_bolsaMadrid.Nombre.isin(accionesAevaluar)])

   #Mostrar tabla en pantalla usando yfinance (bolsa eeuu)
   print('')
   print('TABLA DE DATOS EEUU (USANDO YFINANCE)')
   accionesAevaluar = ["ORI", "ANA.MC", "BBVA.MC", "GRF.MC", "ELE.MC"]
   yahoofinance.obtenerDatos(accionesAevaluar)
   df_yfinance = pd.read_csv('TP2 Webscraping&api\\csv\\yahoo_finance.csv')
   print (df_yfinance)

   #Objetivo 2
   print('2 ACCIONES DE MAYOR GANANCIA, MAYOR PERDIDA - INVESTPY')
   odos.obtenerGananciaPerdida(df_investpy, 'G/P', 2)
   odos.graficarGananciaPerdida(df_investpy, x='symbol', y='G/P', nombre='TP2 Webscraping&api\\Graficos\\Ganan_perd_BolsaEspaña.png')
   print('')
   print('2 ACCIONES DE MAYOR GANANCIA, MAYOR PERDIDA - BOLSA DE MADRID')
   odos.obtenerGananciaPerdida(df_bolsaMadrid, '% Dif.', 2)
   odos.graficarGananciaPerdida(df_bolsaMadrid, x='Nombre', y='% Dif.', nombre='TP2 Webscraping&api\\Graficos\\Ganan_perd_BolsaMadrid.png')