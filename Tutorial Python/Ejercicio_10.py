# Exercise 10: Design a function that filters the words in a list, keeping those that are written in lower case.

def filtrar_PalabrasMinusculas(palabras):
    palabrasFiltradas = []
    for x in palabras:
        if x.islower():
            palabrasFiltradas.append(x)
    
    return palabrasFiltradas



palabras = ["Peras", "manzanas", "melones", "Sandías", "cerezas", "Melocotones"]
filtrarPalabras = filtrar_PalabrasMinusculas(palabras)
print(filtrarPalabras)