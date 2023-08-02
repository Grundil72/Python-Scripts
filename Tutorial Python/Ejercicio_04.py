# Exercise 4: A coin (loaded) lands on its head with a probability of 0.7. Design a random function that flips this coin, and answers "heads" or "tails" according to the given probabilities.

import random

def lanzarMoneda():
    """Random tiene un valor entre 0 - 1"""
    aleatorio = random.random()
    print(aleatorio)
    
    if aleatorio <0.7:
        return "cara"
    else:
        return "cruz"


print(lanzarMoneda())

