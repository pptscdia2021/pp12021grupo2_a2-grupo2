import pandas as pd
import requests
from bs4 import BeautifulSoup

def obtenerDatos():
    #Hacemos la consulta a la pagina y guardamos el contenido en una variable soup
    url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
    page = requests.get(url_page).text 
    soup = BeautifulSoup(page, "lxml")

    #Buscamos la tabla de donde obtener los datos
    tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})

    #creamos una lista vacia que llenaremos con los datos de las tablas
    columnas = []

    #buscamos los encabezados de la tabla y los agregamos a la lista columnos (deberia ubicarse en la posicion 0)
    header = []
    for th in tabla.find_all('th'):
        header.append(th.text)
    columnas.append(header)

    for tr in tabla.find_all('tr'):
        fila = []
        for td in tr.find_all('td'):
            fila.append(td.text)
        if len(fila) > 0:
            columnas.append(fila)
            
    #creamos el dataframe usando la lista columnas,pasamos el contenido (de la posicion 1 en adelante), y lo encabezados en (posicion 0)
    df = pd.DataFrame(columnas[1:], columns=columnas[0])

    #Reemplazamos la , por un . y convertimos en float
    df["% Dif."] = df["% Dif."].str.replace(",", ".").astype(float)
    df["Máx."] = df["Máx."].str.replace(",", ".").astype(float)
    df["Mín."] = df["Mín."].str.replace(",", ".").astype(float)
    df["Últ."] = df["Últ."].str.replace(",", ".").astype(float)
    
    #Guardamos en el archivo csv

    df.to_csv('TP2 Webscraping&api\\csv\\bolsaMadrid.csv')


