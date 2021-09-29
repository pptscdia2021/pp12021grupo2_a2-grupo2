import yfinance as yf
import pandas as pd


def obtenerDatos(acciones):
   df_list = list()
   for ticker in acciones:
      data = yf.download(ticker, auto_adjust = True, prepost = True, period='1d')
      data['ticker'] = ticker  
      df_list.append(data)

   df = pd.concat(df_list)

   # save to csv
   df.to_csv('TP2 Webscraping&api\\csv\\yahoo_finance.csv')



def probando(tickers_list):
   tickers_data= {}
   for ticker in tickers_list:
      ticker_object = yf.Ticker(ticker)

      #convert info() output from dictionary to dataframe
      temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
      temp.reset_index(inplace=True)
      temp.columns = ["Attribute", "Recent"]
      
      # add (ticker, dataframe) to main dictionary
      tickers_data[ticker] = temp

   combined_data = pd.concat(tickers_data)
   combined_data = combined_data.reset_index()
   del combined_data["level_1"] # clean up unnecessary column
   combined_data.columns = ["Ticker", "Attribute", "Recent"] 
   
   combined_data
   df = combined_data

   # save to csv
   df.to_csv('TP2 Webscraping&api\\csv\\yahoo_finance.csv')

accionesAevaluar = ["ORI","BBVA.MC"]
print(probando(accionesAevaluar))