# Exercise 6: Imagine the letters of the alphabet arranged in a circle. 
# That is, to the right of A is B, then C and so on, up to Z, and to the right of Z is A again. 
# We define a function that encodes a character c according to an offset k, moving that character c, k positions to the right. Define it and use it to encode a sentence.

def encode_character(c, k):
    if not c.isalpha():  # Verificar si el carácter no es una letra del alfabeto
        return c  # Devolver caracteres no alfabéticos tal como están

    # Convertir el carácter a mayúscula para facilitar la manipulación
    c = c.upper()

    # Obtener el valor ASCII del carácter y restarle el valor ASCII de 'A'
    position = ord(c) - ord('A')

    # Calcular la nueva posición sumando el desplazamiento y usando el módulo para mantenerlo en el rango de 0 a 25
    new_position = (position + k) % 26

    # Convertir la nueva posición a carácter sumando el valor ASCII de 'A'
    encoded_character = chr(new_position + ord('A'))

    # Devolver el carácter codificado respetando el caso original
    if c.islower():
        return encoded_character.lower()
    else:
        return encoded_character


def encode_sentence(sentence, k):
    encoded_sentence = ""
    
    # Iterar sobre cada carácter en la oración
    for c in sentence:
        # Codificar el carácter usando la función encode_character
        encoded_character = encode_character(c, k)
        
        # Agregar el carácter codificado a la oración codificada
        encoded_sentence += encoded_character

    return encoded_sentence


# Ejemplo de uso
sentence = "Buenos dias, amig@s"
offset = 2 # compensar (es decir, nº de posiciones a avanzar)

encoded_sentence = encode_sentence(sentence, offset)
print(encoded_sentence)  
