import investpy_spain as invest
import yahoofinance
import BolsaMadrid
import pandas as pd
import matplotlib.pyplot as plt
import ganancia_perdida as gp
import graficos as g
import comparar


if __name__ == "__main__":
   #Obtener la tabla en tiempo real de la bolsa de españa
   invest.obtenerDatosInvestpy()
   BolsaMadrid.obtenerDatos()
   
   #Mostrar tabla en pantalla usando investpy
   print('TABLA DE DATOS BOLSA DE MADRID (USANDO investpy)')
   df_investpy_t = pd.read_csv('TP2 Webscraping&api\\csv\\investpy_spain.csv')
   accionesAevaluar = ['ANA', 'BBVA', 'GRLS', 'ELE', 'REP']
   df_investpy = df_investpy_t[df_investpy_t.symbol.isin(accionesAevaluar)].sort_values(by='symbol')
   print(df_investpy)
   g.graficarMaxMin(df_investpy, x='name', max='high', min='low', titulo='Investing.com (Bolsa de España). Valores máximos y mínimos', nombre='TP2 Webscraping&api\\Graficos\\maxMinInvestpy_accionesEvaluadas.png')
   
   #Mostrar tabla en pantalla usando BeautiFoul Soup
   print('')
   print('TABLA DE DATOS BOLSA DE MADRID (USANDO BS4)')
   df_bolsaMadrid_t = pd.read_csv('TP2 Webscraping&api\\csv\\bolsaMadrid.csv')
   accionesAevaluar = ['ACCIONA', 'BBVA', 'GRIFOLS CL.A', 'ENDESA', 'REPSOL']
   df_bolsaMadrid = df_bolsaMadrid_t[df_bolsaMadrid_t.Nombre.isin(accionesAevaluar)]
   print(df_bolsaMadrid)
   g.graficarMaxMin(df_bolsaMadrid, x='Nombre', max='Máx.', min='Mín.', titulo='Bolsa de Madrid. Valores máximos y mínimos', nombre='TP2 Webscraping&api\\Graficos\\maxMinBs4_accionesEvaluadas.png')

   #Mostrar tabla en pantalla usando yfinance (bolsa eeuu)
   print('')
   print('TABLA DE DATOS EEUU (USANDO YFINANCE)')
   accionesAevaluar = ["ANA.MC", "BBVA.MC", "GRF.MC", "ELE.MC","REP.MC"]
   yahoofinance.obtenerDatos(accionesAevaluar)
   df_yfinance = pd.read_csv('TP2 Webscraping&api\\csv\\yahoo_finance.csv')
   print (df_yfinance)
   g.graficarMaxMin(df_yfinance, x='ticker', max='High', min='Low', titulo='Yahoo Finance. Valores máximos y mínimos', nombre='TP2 Webscraping&api\\Graficos\\maxMinYfinance.png')

   #Comparando resultados
   tablaComparacion = comparar.crearTablaComparacion(bolsaMadrid=df_bolsaMadrid, investpy=df_investpy, yfinance=df_yfinance)
   print('')
   print('Tabla de comparacion del valor de las acciones evaluadas')
   print(tablaComparacion)
   g.graficarComparacion(tablaComparacion, x='Nombre', titulo='Comparación acciones evaluadas',nombre='TP2 Webscraping&api\\Graficos\\comparacionAccionesEvaluadas.png')


   #Ganancia o pérdida de las acciones
   print('')
   print('2 ACCIONES DE MAYOR GANANCIA, MAYOR PERDIDA - INVESTPY')
   gp.obtenerGananciaPerdida(df_investpy_t, 'G/P', 2)
   gp.graficarGananciaPerdida(df_investpy_t, x='symbol', y='G/P', kind='bar', titulo='Bolsa de España (Investing.com). Ganancia o pérdida de las acciones', nombre='TP2 Webscraping&api\\Graficos\\Ganan_perd_BolsaEspaña.png')
   print('')
   print('2 ACCIONES DE MAYOR GANANCIA, MAYOR PERDIDA - BOLSA DE MADRID')
   gp.obtenerGananciaPerdida(df_bolsaMadrid_t, '% Dif.', 2)
   gp.graficarGananciaPerdida(df_bolsaMadrid_t, x='Nombre', y='% Dif.', kind='bar', titulo='Bolsa de Madrid. Ganancia o pérdida de las acciones', nombre='TP2 Webscraping&api\\Graficos\\Ganan_perd_BolsaMadrid.png')

   print('')
   #Gráficos
   
   
   
   
   
   