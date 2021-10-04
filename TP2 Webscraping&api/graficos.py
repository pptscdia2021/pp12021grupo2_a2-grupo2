import pandas as pd
import matplotlib.pyplot as plt



def graficarMaxMin(df,x,max,min,nombre):
    fig, ax = plt.subplots()
    x = df[x]
    max = df[max]
    min = df[min]
    ax.plot(x, max, label ='Valor máximo')
    ax.plot(x, min, label ='Valor mínimo')
    ax.set_title('Valores máximos y mínimos de las acciones evaluadas', loc = "left", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
    plt.legend() 
    plt.savefig(nombre, bbox_inches='tight')
    plt.tight_layout();plt.show()

def graficarMaxMinTotal(df,x,max,min,nombre):
    fig, ax = plt.subplots()
    x = df[x]
    max = df[max]
    min = df[min]
    ax.plot(x, max, label ='Valor máximo')
    ax.plot(x, min, label ='Valor mínimo')
    ax.set_title('Valores máximos y mínimos',fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'#FE420F'})
    plt.xticks(rotation=90);plt.legend() 
    plt.savefig(nombre, bbox_inches='tight')
    plt.tight_layout();plt.show()
  
 