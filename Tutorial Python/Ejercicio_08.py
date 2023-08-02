# Exercise 8: We have the following text from Don Quixote.

# Quijote = ["En un lugar de la Mancha, de cuyo nombre no quiero acordarme, ", "no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, ", 
# "adarga antigua, rocín flaco y galgo corredor. ", "Una olla de algo más vaca que carnero, salpicón las más noches, ", "duelos y quebrantos los sábados, lantejas los viernes, algún palomino ", 
# "de añadidura los domingos, consumían las tres partes de su hacienda. ", "El resto della concluían sayo de velarte, calzas de velludo para las ", 
# "fiestas, con sus pantuflos de lo mesmo, y los días de entresemana ", "se honraba con su vellorí de lo más fino. Tenía en su casa una ama que ", 
# "pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y ", "un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera. ", 
# "Frisaba la edad de nuestro hidalgo con los cincuenta años; "]

# We are going to design a function that selects words of a certain length. 
# For simplicity at this point, we consider a word to be a string of non-banked characters, separated from the rest by whitespace. 
# We will (exceptionally) admit other characters such as full stops and commas.

Quijote = ["En un lugar de la Mancha, de cuyo nombre no quiero acordarme, ", "no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, ", "adarga antigua, rocín flaco y galgo corredor. ", "Una olla de algo más vaca que carnero, salpicón las más noches, ", "duelos y quebrantos los sábados, lantejas los viernes, algún palomino ", "de añadidura los domingos, consumían las tres partes de su hacienda. ", "El resto della concluían sayo de velarte, calzas de velludo para las ", "fiestas, con sus pantuflos de lo mesmo, y los días de entresemana ", "se honraba con su vellorí de lo más fino. Tenía en su casa una ama que ", "pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y ", "un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera. ", "Frisaba la edad de nuestro hidalgo con los cincuenta años; "]

def mismaLongitud(longitud):
    
    for x in Quijote:
        print(len(x), end=" ")
    
    print('\n')

    for text in Quijote:
        if len(text) == longitud:
            print(f"El siguiente texto tiene una longitud de {longitud} y se encuentra en la posición {Quijote.index(text)}")
            print(text)


longitud = 69
mismaLongitud(longitud)

