from pymongo import MongoClient
import matplotlib.pyplot as plt
from datetime import datetime
from os import remove
from bson.json_util import dumps, loads
import pandas as pd

""" Entidad Cotizaciones: Unifica las cotizaciones de los 3 mercados y grafica la comparación de la última cotización de 
los mismos """
class Cotizaciones():

    def __init__(self, acciones, mercados):
        self.acciones = acciones
        self.mercados = mercados
       
    def juntarDBS(self):
        df = pd.DataFrame()
        for mercado in self.mercados:
            df = pd.concat([df, mercado.buscarPorNombre(self.acciones)], axis=0).sort_values(by='symbol') 
        print(df)
        return df
    
    def graficarComparacion(self,titulo,nombre):
        df = self.juntarDBS()
        comparar = df.groupby(['symbol', 'origen']).mean()["ult"] #agrupamos según el mercado y mostramos la última cotización
        comparar.plot(kind="bar",width=0.9, color=["#06C2A6","#FF7960","#DBB40C"], figsize=(8,8)) #genera el gráfico de barras
        plt.style.use('seaborn') #estilo de gráfico    
        plt.title(titulo) #título del grafico 
        plt.xlabel('Acciones') #título del eje de las x
        plt.savefig(nombre, bbox_inches='tight') #guardamos el gráfico, 'tight' para guardarlo completo [parámetro: nombre]
        plt.tight_layout();plt.show() #mostramos el gráfico de manera completa