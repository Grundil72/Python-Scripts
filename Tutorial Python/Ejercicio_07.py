# Exercise 7: Design an algorithm that performs the classical decomposition of a number into factors, in the classical way: start by dividing the original number by the smallest possible divisor (2), update the dividend and continue with that divisor or the next one, if necessary:

# 60|2
# 30|2
# 15|3
# 5|5
# 1|

num = int(input("Introduce un número: "))

divisor = 2

while num > 1:
    if num % divisor == 0:
        print(f'{num}|{divisor}')
        num //= divisor
    else:
        divisor += 1

    if num == 1:
        print(f'{num}|')

