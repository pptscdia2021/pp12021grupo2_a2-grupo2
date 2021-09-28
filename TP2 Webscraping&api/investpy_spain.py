import investpy
import pandas as pd


#Obtener la tabla en tiempo real de la bolsa de españa

def obtenerDatosInvestpy():
   return investpy.stocks.get_stocks_overview(country='spain', as_json = False , n_results = 35)
        
df = obtenerDatosInvestpy()

#Guardar datos en csv
def cargarTablaEnCsv():
  df.to_csv("TP2 Webscraping&api\\csv\\investpy_spain.csv")

#Cambiar el porcentaje de canbio a valor numérico
#Ordenar la tabla de mayor a menor según el porcentaje de cambio
def porcentajeCambio():
  df = pd.read_csv('TP2 Webscraping&api\\csv\\investpy_spain.csv')
  df = df.join(df['change_percentage'].str.partition('%')[[0, 1]]).rename({0: 'G/P', 1: '%'}, axis=1)
  df["G/P"] = df["G/P"].apply(pd.to_numeric)
  return df.sort_values(by='G/P', ascending = False)
  
df_cambioPorcentaje = porcentajeCambio()

#print(df_cambioPorcentaje.head())
#print("Mayor ganancia",df_cambioPorcentaje['G/P'].max())
#print("Menor ganancia",df_cambioPorcentaje['G/P'].min())

#Mostrar las dos acciones de mayor ganancia/pérdida
def gananciaPerdida():
  print("Acciones de mayor ganancia\n",df_cambioPorcentaje.head(2))
  print("Acciones de mayor pérdida\n",df_cambioPorcentaje.tail(2))

print(df_cambioPorcentaje)
GP2=gananciaPerdida()

