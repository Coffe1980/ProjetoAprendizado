"""
import math
num = int(input("Escolha um numero: "))
raiz = math.sqrt(num)
print("A raiz quadada de {} é {:.2f}".format(num, raiz))
"""
import time, Aulas.bebidas as bebidas    
h = input ("Hola, seja muito bem vindo, Sabe que horas são ")
if h == "Sim":
    print ("São: {} {} {} ".format(time.strftime("%H:%M:%S")))
else:
    print ("Então, vá estudar, e volte quando souber as horas {}, {}".format(bebidas.doce(), bebidas.salgada()))

