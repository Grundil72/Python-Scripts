# Exercise 15: We have the assert function to make sure that the requirements of a function are met. 
# Design a function with the assert instruction and exemptions to calculate the mcd of two numbers, thinking of a user who can give some non-integer, or null, or negative data...

def calcular_MCD(a, b):
    try:
       
        assert a is not None and b is not None, "Ambos inputs no deberían ser nulos."
        assert isinstance(a, int) and isinstance(b, int), "Ambos inputs deberían ser nº enteros" # para evitar que sean float u otro tipo
        assert a >= 0 and b >= 0, "Ambos inputs deberían ser positivos"

        # Calcular MCD usando el Algoritmo de Euclides
        while b != 0:
            a, b = b, a % b

        return a
        # Explicación bucle while: algoritmo de Euclides
        """1º => a = b """
        """2º => b = a(con el valor antes de asignarle b) % b"""
    except AssertionError as e:
        print("Error:", e)
        return None
    except Exception as e:
        print("Error:", e)
        return None

print(calcular_MCD(48, 18))    # Output: 6
print(calcular_MCD(18, 27))    # Output: 9
print(calcular_MCD(48, 0))     # Output: 48
print(calcular_MCD(0, 12))     # Output: 12
print(calcular_MCD(8, 23))     # Output: 1
print(calcular_MCD(48, -18))   # Output: Error: Ambos inputs deberían ser positivos. None
print(calcular_MCD(48, 2.5))   # Output: Error: Ambos inputs deberían ser nº enteros. None
print(calcular_MCD("48", 18))  # Output: Error: Ambos inputs deberían ser nº enteros. None
print(calcular_MCD(None, 18))  # Output: Error: Ambos inputs deberían ser nº enteros None