#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)

hora = datetime.now().strftime('%H:%M:%S')
print(hora)

