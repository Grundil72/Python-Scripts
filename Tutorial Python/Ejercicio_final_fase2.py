# Fase 2: Predicción de llamadas diarias por tipo de cita

# A continuación, vamos a predecir cuántas llamadas habrá de cada tipo de cliente por día en la próxima semana. 
# Para ello, contaremos cuántas llamadas hay de cada tipo de cliente cada día en el historial de llamadas. 
# Se encontrará la media y la desviación estándar de cada tipo de cliente por día. 
# Con esa media y desviación estándar encontraremos un número aleatorio siguiendo una distribución normal para predecir cuántas llamadas habrá por día y por tipo de paciente en los próximos 7 días.

import pandas as pd
import numpy as np

data = pd.read_csv('historico_citas.csv', encoding='utf-8', delimiter=';')     # Especificar la codificación al leer el archivo CSV
print(data)
'''Contar cuántas llamadas hay de cada tipo de cliente cada día en el historial de llamadas. '''
group = data.groupby(by= ["Fec. Alta", "Contrato"]).size()
print(group.head(20))

print("Min y MAX")
minCalls = group.groupby(by= ["Fec. Alta", "Contrato"]).min()
print(minCalls.head(20))
maxCalls= group.groupby(by= ["Fec. Alta", "Contrato"]).max()
print(maxCalls)


'''Hallar la media y la desviación estándar de cada tipo de cliente por día.'''
media =group.groupby('Fec. Alta').mean()
print(f"\nLa media es:")
print(media)

desv =group.groupby('Fec. Alta').std()
print(f"\nLa desviación estándar es: ")
print(desv)

'''Generar predicciones para los próximos 7 días'''
prediction_days = 7
last_date = data['Fec. Alta'].max()
prediction_dates = pd.date_range(last_date, periods=prediction_days+1, inclusive='right').date[1:]
predictions = []

for date in prediction_dates:
    for contract in data['Contrato'].unique():
        mean = media.get(date, 0)
        std = desv.get(date, 0)
        calls = np.random.normal(mean, std)
        predictions.append({'Fecha': date, 'Contrato': contract, 'Llamadas': calls})

# Crear DataFrame a partir de la lista de predicciones
predictions_df = pd.DataFrame(predictions)


predictions_df.to_excel("Resultados_fase2.xlsx", sheet_name='Hoja1', index=False)

# Mostrar las predicciones
print(predictions_df)
