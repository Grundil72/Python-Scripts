# Exercise 9: Design a function that takes a list of integers as parameters and returns the minimum and maximum values of this list.

import random

def generarListadoNum():

    lista = []
    x=0
    while x < 10:
        num = random.randint(0, 100)
        lista.append(num)
        x += 1

    for x in lista:
        print(x, end=", ")
    print()
    return lista

def Min_Max(listado):

    listado.sort()
    for x in listado:
        print(x, end=", ")
    
    print()
    print(f'El valor mínimo es: {listado[0]}')
    print(f'El valor máximo es: {listado[-1]}')
    



listado = generarListadoNum()
Min_Max(listado)