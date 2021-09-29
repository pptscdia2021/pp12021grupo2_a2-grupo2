{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ada2f4ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "#Hacemos la consulta a la pagina y guardamos el contenido en una variable soup\n",
    "url_page = 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'\n",
    "page = requests.get(url_page).text \n",
    "soup = BeautifulSoup(page, \"lxml\")\n",
    "\n",
    "#Buscamos la tabla de donde obtener los datos\n",
    "tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'})\n",
    "\n",
    "#creamos una lista vacia que llenaremos con los datos de las tablas\n",
    "columnas = []\n",
    "\n",
    "#buscamos los encabezados de la tabla y los agregamos a la lista columnos (deberia ubicarse en la posicion 0)\n",
    "header = []\n",
    "for th in tabla.find_all('th'):\n",
    "    header.append(th.text)\n",
    "columnas.append(header)\n",
    "\n",
    "for tr in tabla.find_all('tr'):\n",
    "    fila = []\n",
    "    for td in tr.find_all('td'):\n",
    "        fila.append(td.text)\n",
    "    if len(fila) > 0:\n",
    "        columnas.append(fila)\n",
    "        \n",
    "#creamos el dataframe usando la lista columnas,pasamos el contenido (de la posicion 1 en adelante), y lo encabezados en (posicion 0)\n",
    "df = pd.DataFrame(columnas[1:], columns=columnas[0])\n",
    "\n",
    "#Guardamos en el archivo csv\n",
    "\n",
    "df.to_csv('csv\\\\bolsaMadrid.csv')\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
