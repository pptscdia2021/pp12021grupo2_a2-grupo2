
def suma(a,b): 
   return(a+b)

def sumabs(a,b): 
   return abs(a+b)

from resta import resta
import division

if __name__ == "__main__":
   print("Principal")
   print("La resta es:  ", str(resta(125,25)))
   print("La suma es:  ", str(suma(6,9)))
   print("La division es:  ", str(division.dividir(10,2)))
   print("El valor absoluto de la suma es: ", sumabs(5,-8))
