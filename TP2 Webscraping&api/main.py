import investpy_spain as invest
import pandas as pd

if __name__ == "__main__":
   #Obtener la tabla en tiempo real de la bolsa de españa
   invest.obtenerDatosInvestpy()

   #Guardar datos en csv
   invest.cargarTablaEnCsv()

   df = pd.read_csv('TP2 Webscraping&api\\investpy_spain.csv')
   print(df)




