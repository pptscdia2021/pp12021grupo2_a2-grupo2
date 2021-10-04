import investpy_spain as invest
import yahoofinance
import BolsaMadrid
import pandas as pd
import matplotlib.pyplot as plt
import ganancia_perdida as gp
import graficos as g


if __name__ == "__main__":
   #Obtener la tabla en tiempo real de la bolsa de españa
   invest.obtenerDatosInvestpy()
   BolsaMadrid.obtenerDatos()
   
   #Mostrar tabla en pantalla usando investpy
   print('TABLA DE DATOS BOLSA DE MADRID (USANDO investpy)')
   df_investpy = pd.read_csv('TP2 Webscraping&api\\csv\\investpy_spain.csv')
   accionesAevaluarI = ['ANA', 'BBVA', 'GRLS', 'ELE', 'REP']
   print(df_investpy[df_investpy.symbol.isin(accionesAevaluarI)].sort_values(by='symbol'))
   
   #Mostrar tabla en pantalla usando BeautiFoul Soup
   print('')
   print('TABLA DE DATOS BOLSA DE MADRID (USANDO BS4)')
   df_bolsaMadrid = pd.read_csv('TP2 Webscraping&api\\csv\\bolsaMadrid.csv')
   accionesAevaluarB = ['ACCIONA', 'BBVA', 'GRIFOLS CL.A', 'ENDESA', 'REPSOL']
   print(df_bolsaMadrid[df_bolsaMadrid.Nombre.isin(accionesAevaluarB)])

   #Mostrar tabla en pantalla usando yfinance (bolsa eeuu)
   print('')
   print('TABLA DE DATOS EEUU (USANDO YFINANCE)')
   accionesAevaluar = ["ANA.MC", "BBVA.MC", "GRF.MC", "ELE.MC","REP.MC"]
   yahoofinance.obtenerDatos(accionesAevaluar)
   df_yfinance = pd.read_csv('TP2 Webscraping&api\\csv\\yahoo_finance.csv')
   print (df_yfinance)

   #Objetivo 2
   print('2 ACCIONES DE MAYOR GANANCIA, MAYOR PERDIDA - INVESTPY')
   gp.obtenerGananciaPerdida(df_investpy, 'G/P', 2)
   gp.graficarGananciaPerdida(df_investpy, x='symbol', y='G/P', kind='bar', nombre='TP2 Webscraping&api\\Graficos\\Ganan_perd_BolsaEspaña.png')
   print('')
   print('2 ACCIONES DE MAYOR GANANCIA, MAYOR PERDIDA - BOLSA DE MADRID')
   gp.obtenerGananciaPerdida(df_bolsaMadrid, '% Dif.', 2)
   gp.graficarGananciaPerdida(df_bolsaMadrid, x='Nombre', y='% Dif.', kind='bar', nombre='TP2 Webscraping&api\\Graficos\\Ganan_perd_BolsaMadrid.png')

   print('')
   #Gráficos
   dfI = df_investpy[df_investpy.symbol.isin(accionesAevaluarI)].sort_values(by='symbol')
   dfB = df_bolsaMadrid[df_bolsaMadrid.Nombre.isin(accionesAevaluarB)]
   g.graficarMaxMin(df_yfinance, x='ticker', max='High', min='Low', nombre='TP2 Webscraping&api\\Graficos\\maxMinYfinance.png')
   g.graficarMaxMin(dfI, x='symbol', max='high', min='low', nombre='TP2 Webscraping&api\\Graficos\\maxMinInvestpy_accionesEvaluadas.png')
   g.graficarMaxMin(dfB, x='Nombre', max='Máx.', min='Mín.', nombre='TP2 Webscraping&api\\Graficos\\maxMinBs4_accionesEvaluadas.png')
   g.graficarMaxMinTotal(df_investpy, x='symbol', max='high', min='low', nombre='TP2 Webscraping&api\\Graficos\\maxMinInvestpy_totalAcciones.png')
   g.graficarMaxMinTotal(df_bolsaMadrid, x='Nombre', max='Máx.', min='Mín.', nombre='TP2 Webscraping&api\\Graficos\\maxMinBs4_totalAcciones.png')
   
   

