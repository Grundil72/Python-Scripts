# Exercise 1: A country has 1U, 5U and 25U coins. If we have a certain amount of money in a variable, design formulas to give the optimal change in the currencies described.

x = 1
y = 5
z = 25
# x, y, z = 1, 5, 25

importe = int(input("Ingresa importe: "))

moneda25 = importe//z
resto = importe%z

moneda5 = resto//y
resto = importe%y

moneda1 = resto 

print("El importe " + str(importe) + " consta de:" )
print(str(moneda25) + " moneda/s de 25U")
print(str(moneda5) + " moneda/s de 5U")
print(str(moneda1) + " moneda/s de 1U")

