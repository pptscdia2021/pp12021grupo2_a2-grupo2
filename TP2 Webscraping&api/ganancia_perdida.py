import pandas as pd
import matplotlib.pyplot as plt


def obtenerGananciaPerdida(df, columna, cant):
  df = df.sort_values(by=columna, ascending = False)
  print("Acciones de mayor ganancia\n",df.head(cant))
  print("Acciones de mayor pérdida\n",df.tail(cant))

def graficarGananciaPerdida(df,x,y,kind,nombre):
    ax = df.plot(x,y,kind);print(ax)
    plt.title('Ganancia/pérdida de las acciones')
    plt.savefig(nombre, bbox_inches='tight')
    plt.tight_layout();plt.show()
    
