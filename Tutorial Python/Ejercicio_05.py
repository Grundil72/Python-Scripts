# Exercise 5: Design a function that gives the grade ("Fail", ..., "Honours") corresponding to a grade, requiring the input to be a real number between 0 and 10.


def calcularNota_1(num):

    if num<5 :
        print("Suspenso")
    elif num >= 5 and num <6:
        print("Suficiente")
    elif num >= 6 and num <7:
        print("Bien")
    elif num >= 7 and num <9:
        print("Notable")
    else:
        print("sobresaliente")
    
def calcularNota_2(num):
    if num < 5:
        print("Suspenso")
    elif 5 <= num < 6:
        print("Suficiente")
    elif 6 <= num < 7:
        print("Bien")
    elif 7 <= num < 9:
        print("Notable")
    else:
        print("Sobresaliente")

num = int(input("Introduce nota: "))

calcularNota_1(num)
calcularNota_2(num)
