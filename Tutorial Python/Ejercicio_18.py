# Exercise 18:

# Create an integer array of zeros.
# Create an integer array of ones.
# Create an empty array.
# Create an array with randomly chosen elements.

import numpy as np


a = np.zeros(7)
print(f"Array de zeros: {a}")

b = np.ones(7)
print(f"Array de unos: {b}")

c = np.empty(3)
print(f"Array vacío: {c}")

d = np.random.random(7)
print(f"Array random: {d}")