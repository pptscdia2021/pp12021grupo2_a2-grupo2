import pandas as pd

def crearTablaComparacion(bolsaMadrid, investpy, yfinance):

#Filtrando y ordenando dataFrames
   bolsaMadrid = bolsaMadrid.loc[:, ['Nombre', 'Últ.']].sort_values(by='Nombre').reset_index(drop=True)
   investpy = investpy.loc[:, ['name', 'last']].sort_values(by='name').reset_index(drop=True)
   yfinance = yfinance.loc[:, ['ticker', 'Close']].sort_values(by='ticker').reset_index(drop=True)

#Uniendo Data Frame
   df = pd.concat([bolsaMadrid, investpy['last'], yfinance['Close']], axis=1)

#Renombrando Columnas
   df = df.rename({'Últ.': 'Bolsa Madrid (EUR)', 'last': 'InvestPY (EUR)', 'Close': 'Yahoo Finance (EUR)'}, axis=1)
   

   return df
   