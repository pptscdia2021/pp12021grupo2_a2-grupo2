import yfinance as yf
import pandas as pd

def obtenerDatos(acciones):
   df_list = list()
   for ticker in acciones:
      data = yf.download(ticker, group_by='ticker', period='1d')
      data['ticker'] = ticker  
      df_list.append(data)

   df = pd.concat(df_list)

   # save to csv
   df.to_csv('TP2 Webscraping&api\\csv\\yahoo_finance.csv')