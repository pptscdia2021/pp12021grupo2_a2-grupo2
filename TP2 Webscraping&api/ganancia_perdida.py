import pandas as pd
import matplotlib.pyplot as plt


def obtenerGananciaPerdida(df, columna, cant):
  #ordeno las columnas según el % de ganancia o pérdida de forma descendente          
  df = df.sort_values(by=columna, ascending = False)
  print("Acciones de mayor ganancia\n",df.head(cant))
  print("Acciones de mayor pérdida\n",df.tail(cant))


def graficarGananciaPerdida(df,x,y,titulo,nombre):
    #vamos a graficar los valores positivos de un color y los negativos de otro color
    #seleccionamos los valores positivos
    dfMas=df[y]>=0
    dfPositivos = df[dfMas]
    #renombramos la columna como Ganancia
    dfPositivos = dfPositivos.rename({y: 'Ganancia'}, axis=1)
    #seleccionamos los valores negativos
    dfMenos=df[y]<0
    dfNegativos = df[dfMenos]
    #renombramos la columna como Pérdida
    dfNegativos = dfNegativos.rename({y: 'Pérdida'}, axis=1)
    #unimos las tablas ordenadas por el nombre
    df = pd.concat([dfPositivos,dfNegativos]).sort_values(by=x)

    #armamos el gráfico 
    #parámetros: columnas, tipo de gráfico, ancho de las barras, colores de las barras
    df[[x, 'Ganancia', 'Pérdida']].plot(x, kind="bar", width=1, color=["#04D8B2","#EF4026"])
    #título del grafico
    plt.title(titulo)
    #título del eje de las x
    plt.xlabel('Acciones')
    #guardamos el gráfico, 'tight' s para que se guarde el gráfico de manera completa
    #parámetro: nombre
    plt.savefig(nombre, bbox_inches='tight')
    #mostramos el gráfico de manera completa
    plt.tight_layout();plt.show()
    
