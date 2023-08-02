# A partir del conjunto de datos (cars.xlsx). Conjunto de datos de automóviles con características que incluyen marca, modelo, año, motor y otras propiedades del automóvil
# utilizadas para predecir su precio.

# Se solicita lo siguiente:

# Al cargar los datos en el marco de datos, asegúrese de que los datos sean correctos, si contiene caracteres especiales, cambie la codificación y, si esto no lo soluciona, 
# reemplace los caracteres especiales.
# Comprobación de los tipos de datos.
# Eliminar columnas irrelevantes.
# Cambiar el nombre de las columnas.
# Eliminar las filas duplicadas.
# Quitar los valores faltantes o nulos.
# Detección de valores atípicos.
# Trazar diferentes características entre sí (dispersión), contra frecuencia (histograma).

import matplotlib as mt
import numpy as np
import pandas as pd
import scipy as s
import sklearn as skl

# Lee el archivo "cars.xlsx" y carga los datos en un DataFrame
df = pd.read_excel("Onboarding_Fase1\cars_original.xlsx")

# Define una función para eliminar comas dentro de comillas utilizando una expresión regular
def remove_commas_inside_quotes(text):
    parts = text.split('"')
    for i in range(1, len(parts), 2):
        parts[i] = parts[i].replace(",", " ")
    return '"'.join(parts)


# Aplica la función a cada celda del DataFrame
df = df.applymap(remove_commas_inside_quotes)

# Elimina las comillas dobles de todas las celdas del DataFrame
df = df.applymap(lambda x: x.replace('"', ''))

# Guarda los cambios en un nuevo archivo "cars_modified.xlsx" con las comas eliminadas dentro de comillas
df.to_csv("Onboarding_Fase1\cars.csv", encoding='utf-8', index=False)


data = pd.read_csv("Onboarding_Fase1\cars.csv", encoding='utf-8', delimiter=',' )
print(data)

# Nota:   al abrir cars.csv en VSC se observa que cada fila está entre comillas.
#         Se abre el archivo y se guarda como CSV UTF-8(Delimitado por comas)