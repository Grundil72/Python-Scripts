# En el ejercicio final revisaremos todo lo anterior. Para ello tendremos que crear un sencillo sistema inteligente de citación para una clínica sanitaria. 
# Actualmente el método que siguen para dar citas a los pacientes es un proceso manual y no muy óptimo, 
# con un poco de orden esta situación mejorará y la satisfacción del paciente aumentará significativamente.

# El proceso consta de 4 partes: clasificación, predicción, optimizador y, simulador. 
# En primer lugar, se clasificarán los pacientes para predecir cuántas llamadas de cada tipo de paciente llegarán cada día, 
# de forma que con el optimizador podremos reservar un número determinado de ranuras para cada tipo para obtener la menor penalización posible. 
# Una vez tengamos la clasificación de pacientes, la predicción de llamadas y el optimizador desarrollado, vamos a simular que llega una llamada de un paciente para pedir cita, 
# la clasificaremos y le mostraremos las ranuras que el optimizador ha reservado para ese tipo, elegirá la primera ranura, y se actualizará la agenda mostrando una ranura menos disponible.

# Suposiciones:

# Para hacerlo más simple, supongamos que las citas también se pueden asignar los fines de semana.
# El escenario será con un horario vacío para simplificar el problema. Es decir, no hay cita dada.
# El simulador elige la primera cita que se muestra.


# Fase 1: Clasificación de los tipos de citas
#   En primer lugar, debes descargar el csv histórico y el csv de facturación en el siguiente enlace.

#   Comenzaremos con el análisis y predicción de llamadas. Tenemos una mesa con los clientes y su facturación, y otra con las citas del último mes. 
#   Vamos a clasificar a los clientes por su facturación:

#   P1 -> +4000€ P2 -> 3000€-4000€ P3 -> -3000€

import pandas as pd

data = pd.read_csv('contrato_facturacion.csv', encoding='utf-8', delimiter=';')     # Especificar la codificación al leer el archivo CSV
print(data)

data['Facturación'] = data['Facturación'].astype(float).round(2)
print(data.head(10))

# Agrupar los datos según los patrones especificados
def agrupar_patrones(valor):
    if valor > 4000:
        return 'P1'
    elif 3000 <= valor <= 4000:
        return 'P2'
    else: # valor < 3000:
        return 'P3'

data['Grupo'] = data['Facturación'].apply(agrupar_patrones)
data = data.rename(columns={'Unnamed: 0': 'Index'})


data.to_csv("Resultados_fase1.csv", index=False, encoding='utf-8', sep=';')
print(data)

'''Incorporar la columna Grupo de Resultados_fase1.csv a historico_citas.csv '''
archivo_1 = pd.read_csv("Resultados_fase1.csv", encoding='utf-8', delimiter=';')
archivo_2 = pd.read_csv("historico_citas.csv", encoding='utf-8', delimiter=';')
archivo_2['Fec. Alta'] = pd.to_datetime(archivo_2['Fec. Alta'])
# Convierte la columna 'Fec. Alta' al formato de fecha
archivo_2['Fec. Alta'] = pd.to_datetime(archivo_2['Fec. Alta'])

# Extrae solo la fecha (sin la parte de la hora)
archivo_2['Fec. Alta'] = archivo_2['Fec. Alta'].dt.strftime('%d/%m/%Y')

combinar_datos = pd.merge(archivo_2, archivo_1[['Contrato', 'Grupo']], on='Contrato', how='left', )
combinar_datos = combinar_datos.rename(columns={'Unnamed: 0': 'Index'})
combinar_datos.to_csv("HistoricoCitas_Grupos.csv", index=False, encoding='utf-8', sep=';')


# Leer el archivo CSV
file_path = "HistoricoCitas_Grupos.csv" 
df = pd.read_csv(file_path, sep=";")

# Filtrar las filas que contienen un valor en la columna "Grupo"
df = df.dropna(subset=["Grupo"])

# Ordenar y Guardar las filas filtradas en un nuevo archivo CSV
df['Fec. Alta'] = pd.to_datetime(df['Fec. Alta'], format='%d/%m/%Y')
df = df.sort_values(by=['Fec. Alta'])
df.to_csv("datos_filtrados.csv", encoding='utf-8', index=False, sep=";")
