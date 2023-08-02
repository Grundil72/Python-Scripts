# Exercise 11: Calculate the average of a list of numbers passed as parameters.

import random
import statistics

def generarListadoNum():

    lista = []
    i=0
    while i < 10:
        num = random.randint(0, 100)
        lista.append(num)
        i += 1
    
    for x in lista:
        print(x, end=", ")
    print()

    return lista


listado = generarListadoNum()

mean = statistics.mean(listado)
print(f"La media es: {mean}")