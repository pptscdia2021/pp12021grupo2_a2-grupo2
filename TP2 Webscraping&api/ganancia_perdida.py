import pandas as pd
import matplotlib.pyplot as plt


def obtenerGananciaPerdida(df, columna, cant):
  #ordeno las columnas según el % de ganancia o pérdida de forma descendente          
  df = df.sort_values(by=columna, ascending = False)
  print("Acciones de mayor ganancia\n",df.head(cant))
  print("Acciones de mayor pérdida\n",df.tail(cant))


def graficarGananciaPerdida(df,x,y,titulo,nombre):
    #vamos a graficar los valores positivos de un color y los negativos de otro color
    dfPositivos = df[df[y]>=0].rename({y: 'Ganancia'}, axis=1)#filtramos las acciones con ganancia
    dfNegativos = df[df[y]<0 ].rename({y: 'Pérdida'}, axis=1)#filtramos las acciones con pérdida
    df = pd.concat([dfPositivos,dfNegativos]).sort_values(by=x)   #unimos las tablas ordenadas por el nombre
    #armamos el gráfico 
    plt.style.use('seaborn') #estilo grafico
    df[[x, 'Ganancia', 'Pérdida']].plot(x, kind="bar", width=1, color=["#04D8B2","#EF4026"]) #parámetros: columnas, tipo de gráfico, ancho de las barras, colores de las barras
    plt.title(titulo) #título del grafico
    plt.xlabel('Acciones') #título del eje de las x
    plt.savefig(nombre, bbox_inches='tight') #guardamos el gráfico, 'tight' para guardarlo completo [parámetro: nombre]
    plt.tight_layout();plt.show() #mostramos el gráfico de manera completa
