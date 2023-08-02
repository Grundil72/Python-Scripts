# Exercise 17: We have the vectors u=[1, 2, 3] and v=[4, 5, 6]. Calculate:

# Scalar product.
# Vector product.
# Combined product (each u_i * v_j).

import itertools as it
import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

print(f"Producto Escalar: {u@v}")
print(f"Producto Escalar: {u.dot(v)}")
print()

print(f"Producto de Vectores: {u@v}")
print(f"Producto de Vectores: {u.dot(v)}")
print()

print(f"Producto combinado:")
combinacion = it.product(u, v)
for i in combinacion:
    print(i)


