def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Solicitamos los números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Calculamos el MCD usando la función que definimos
mcd = calcular_mcd(numero1, numero2)

# Mostrar resultados
print(f"El MCD de {numero1} y {numero2} es: {mcd}")
print("*** ¡Fin del programa! ***")

