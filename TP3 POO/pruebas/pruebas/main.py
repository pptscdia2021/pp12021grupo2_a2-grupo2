import pandas as pd
import requests
import yfinance as yf
import investpy
from bs4 import BeautifulSoup
from pymongo import MongoClient
import matplotlib.pyplot as plt
from datetime import datetime
from os import remove
from bson.json_util import dumps, loads
import clases


""" Objetivo 1: Leer los datos, guardarlos en la base y luego leerlos y
mostrarlos en pantalla """ 

#Nombramos las acciones que queremos buscar
listaAcciones =[
    'BBVA', "BBVA.MC",
    'ELE', "ELE.MC", 'ENDESA',
    'GRLS', "GRF.MC", 'GRIFOLS CL.A',
    'INDRA A', 'IDR',"IDR.MC",
    "REP.MC", 'REP','REPSOL'
    ]

accionesBolsaMadrid = BolsaDeMadrid()
accionesInvesting = Investing()
accionesYFinance = YahooFinance(listaAcciones)

mercados = [accionesBolsaMadrid, accionesInvesting, accionesYFinance]

for mercado in mercados:
    mercado.imprimirDF()
    
""" Objetivo 2: Identificar las 2 acciones de mayor ganancia y de mayor perdida """

for mercado in mercados:
    if mercado != accionesYFinance:
        mercado.imprimirMayorGanancia(2)
        mercado.imprimirMayorPerdida(2)
        mercado.graficarGananciaPerdida()



""" Objetivo 3: Comparativa de precios de cotización entre los orígenes de datos. """
comparacion = Cotizaciones(listaAcciones, mercados)
print(comparacion.juntarDBS())
comparacion.graficarComparacion('Última cotización de las acciones según mercado', 'comparacionMercados.png')
comparacion.graficarComparacion2('Última cotización de las acciones según mercado', 'comparacionMercados.png')


""" 2. Datos historicos yahoo finance """
accionesYFinance.obtenerDatos(periodo='30d')

accionesYFinance.graficarAcciones('BBVA.MC')


accionesYFinance.graficarAcciones('ELE.MC')

accionesYFinance.graficarAcciones('GRF.MC')


accionesYFinance.graficarAcciones('IDR.MC')

accionesYFinance.graficarAcciones('REP.MC')

