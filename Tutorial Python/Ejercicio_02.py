# Exercise 2: A proper noun must be written with the first letter capitalised. Design instructions to fix it in case it is written with a lower case letter.

nombre = input("Introduce tu nombre: ")

inicial = nombre[0].upper()

"""Poniendo nº 1, solo reemplaza en 1 ocurrencia. Si no pongo el nº remplaza en todas las ocurrencias. Ejemplo: AnA"""
x= nombre.replace(nombre[0], inicial, 1) 

print("Tu nombre es: " + x)

name = "alberto"
print(name.capitalize())
