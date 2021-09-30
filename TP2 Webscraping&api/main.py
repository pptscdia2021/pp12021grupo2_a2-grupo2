import investpy_spain as invest
import yahoofinance
import BolsaMadrid
import pandas as pd
import matplotlib.pyplot as plt

def obtenerGananciaPerdida(df, columna, cant):
  df = df.sort_values(by=columna, ascending = False)
  print("Acciones de mayor ganancia\n",df.head(cant))
  print("Acciones de mayor pérdida\n",df.tail(cant))

def graficarGananciaPerdida(df,x,y):
    df = df
    axis = df.plot.bar(x,y)
    print(axis)
    plt.title('Ganancia/pérdida de las acciones')
    plt.show()

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
   obtenerGananciaPerdida(df_investpy, 'G/P', 2)
   graficarGananciaPerdida(df_investpy, x='symbol', y='G/P')
   print('')
   print('2 ACCIONES DE MAYOR GANANCIA, MAYOR PERDIDA - BOLSA DE MADRID')
   obtenerGananciaPerdida(df_bolsaMadrid, '% Dif.', 2)
   graficarGananciaPerdida(df_bolsaMadrid, x='Nombre', y='% Dif.')