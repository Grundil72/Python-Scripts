# Exercise 13: Starting from the text of Don Quixote above:

# Parte 1: You are asked to extract the slab of the words that are in that file.
# Parte 2: Now we are asked to extract the whole, that is, with the words but without repetition.
# Parte 3: We also want to count the number of times that each word appears in the file.
# Parte 4:Finally, we want to build a dictionary whose keys are frequencies and whose values are set of words: frecs = {1: {words with frequency 1}. ...}.

Quijote = ["En un lugar de la Mancha, de cuyo nombre no quiero acordarme, ", "no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, ", 
           "adarga antigua, rocín flaco y galgo corredor. ", "Una olla de algo más vaca que carnero, salpicón las más noches, ", 
           "duelos y quebrantos los sábados, lantejas los viernes, algún palomino ", "de añadidura los domingos, consumían las tres partes de su hacienda. ", 
           "El resto della concluían sayo de velarte, calzas de velludo para las ", "fiestas, con sus pantuflos de lo mesmo, y los días de entresemana ", 
           "se honraba con su vellorí de lo más fino. Tenía en su casa una ama que ", "pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y ", 
           "un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera. ", "Frisaba la edad de nuestro hidalgo con los cincuenta años "]

# Parte 1:
lista =[]
palabra=""

for i in range(len(Quijote)):
    for j in Quijote[i]:
        if j != "," and j != " ":
            palabra += j
        else:
            if palabra != "":
                lista.append(palabra)
                palabra=""

print(lista)
print()

# Parte 2:
conjunto = set(lista)
print(conjunto)
print()

# Parte3: 
dict = {}

for i in lista:
    num = lista.count(i)
    print(f"{i} = {num}")
    dict[i] = num # Se añade al diccionario

print(dict)
print()

# Parte 4

dict_frecuencia = {}

for palabra in lista:
    num = lista.count(palabra)

    if num in dict_frecuencia:
        if palabra not in dict_frecuencia[num]:
            dict_frecuencia[num].append(palabra)
    else: 
        dict_frecuencia[num] = [palabra]



print("La frecuencia es: ")
print(dict_frecuencia)
print()


dict_ordenado = sorted(dict_frecuencia.items())
print("La frecuencia ordenada es: ")
print(dict_ordenado)
print()



