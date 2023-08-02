# Exercise 14: Upload a file that does not exist, this will cause an error, fix it by handling this situation with an exception.

try:
    file = "fichero.txt"
    file_path = rf'C:\Users\a.a.munoz.martinez\{file}'
    with open(file_path, 'r') as file:
        contenido = file.read()

        print("Contenido del fichero: ")
        print(contenido)

except FileNotFoundError:
    print(f"El fichero \'{file}\' no existe")


