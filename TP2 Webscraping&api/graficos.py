import pandas as pd
import matplotlib.pyplot as plt



def graficarMaxMin(df,x,max,min,titulo,nombre):
    plt.style.use('Solarize_Light2')
    fig, ax = plt.subplots()
    #fig.set_size_inches(7,12)
    x = df[x]
    max = df[max]
    min = df[min]
    ax.plot(x, max, label ='Valor máximo', color="#04D8B2")
    ax.plot(x, min, label ='Valor mínimo', linestyle = 'dashed', color="#FA8072")
    ax.set_title(titulo, loc = "left", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
    plt.legend() 
    plt.savefig(nombre, bbox_inches='tight')
    plt.tight_layout();plt.show()

def graficarComparacion(df,x,titulo,nombre):
    plt.style.use('seaborn')
    df.set_index(x).plot.bar(rot=0, title=titulo, figsize=(6,6), fontsize=12)
    plt.savefig(nombre, bbox_inches='tight')
    plt.tight_layout();plt.show()
 