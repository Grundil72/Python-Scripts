import pandas as pd

data = pd.read_csv("datos_filtrados.csv", encoding='utf-8', delimiter=';')
print(data)

total = data.groupby(by= ["Fec. Alta", "Contrato"]).size()
print(total.head(20))

# Primero, agrupamos por la primera parte del índice jerárquico "Fec. Alta"
grouped_data = total.groupby(level=0)

# Luego, obtenemos el mínimo y máximo para cada fecha
min_values = grouped_data.min()
max_values = grouped_data.max()

# Finalmente, mostramos los resultados
print("Valores mínimos por fecha:")
print(min_values)

print("\nValores máximos por fecha:")
print(max_values)


