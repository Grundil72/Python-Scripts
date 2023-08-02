# Exercise 3: Write the currency exchange exercise (exercise 1) as a function.

x, y, z = 1, 5, 25

importe = int(input("Ingresa importe: "))

def cambio (importe):
    moneda25 = importe//z
    resto = importe%z

    moneda5 = resto//y
    resto = importe%y

    moneda1 = resto 

    return moneda1, moneda5, moneda25


moneda1, moneda5, moneda25 = cambio(importe);
print("El importe " + str(importe) + " consta de:" )
print(str(moneda25) + " moneda/s de 25U")
print(str(moneda5) + " moneda/s de 5U")
print(str(moneda1) + " moneda/s de 1U")