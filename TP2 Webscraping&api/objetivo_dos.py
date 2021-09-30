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
