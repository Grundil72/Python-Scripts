# Fase 4: Simulador.

# Vamos a simular las llamadas entrantes durante la semana siguiente.
# El simulador de llamadas se realizará de forma aleatoria. Es decir, calcularemos el número mínimo y máximo de llamadas por día independientemente del tipo de cita en 
# función del historial de llamadas, y calcularemos un número aleatorio dentro de ese rango durante 5 días. 
# Así sabremos cuántas llamadas se recibirán durante esos 5 días, por ejemplo: 01/01/2021: 41, 01/01/2021: 25, 01/01/2021: 32, 01/01/2021: 17, 01/01/2021:28. En otras palabras, si el día 1, 5 pacientes van a llamar, será del siguiente tipo: {P2, P1, P2, P3, P3}. Se colocarán por orden de salida.

# Es decir, si hemos simulado que el primer cliente que llama a P2, mostrará las ranuras que el optimizador ha reservado para ese tipo de cita, y lo colocará en la primera ranura.

# La agenda se actualizará, por lo que habrá una franja menos el día que hayas reservado la cita para ese tipo de cita. A su vez, se calculará la penalización, es decir, se restará el día que se ha asignado la cita del día que se ha convocado y si supera los días límite, es decir, 2 para P1, 3 para P2 y 4 para P3, se sumará 1 a las penalizaciones. Esto se hará sucesivamente.

# El resultado será el número total de penalizaciones, y las citas asignadas para cada convocatoria.

# Ya tenemos un optimizador de trabajo, y hemos simulado las citas durante una semana para realizar un seguimiento de su rendimiento.

import pandas as pd
import random
from datetime import timedelta, datetime

# Leer los datos desde el archivo "datos_filtrados.csv"
datos = pd.read_csv("datos_filtrados.csv", encoding='utf-8', delimiter=';')

# Convertir la columna 'Fec. Alta' a formato de fecha
datos['Fec. Alta'] = pd.to_datetime(datos['Fec. Alta'], dayfirst=True)

# Definir las sanciones en días para cada grupo
sanciones = {'P1': 2, 'P2': 3, 'P3': 4}

# Función para calcular la fecha límite sin penalización para cada llamada
def calcular_fecha_limite(fecha_alta, grupo):
    return fecha_alta + timedelta(days=sanciones.get(grupo, 0))

# Función para simular las llamadas entrantes durante una semana
def simular_llamadas_semana(datos, min_llamadas_por_dia, max_llamadas_por_dia):
    agenda = {}  # Calendario para la semana con los espacios disponibles por día y grupo
    penalizaciones = 0  # Contador de penalizaciones

    for i in range(5):  # Simular 5 días de la semana
        fecha_actual = datetime(2021, 1, 19) + timedelta(days=i)
        num_llamadas_dia = random.randint(min_llamadas_por_dia, max_llamadas_por_dia)

        for j in range(num_llamadas_dia):
            grupo_llamada = random.choice(['P1', 'P2', 'P3'])  # Elegir aleatoriamente el grupo de la llamada

            # Verificar si hay disponibilidad para el grupo en la fecha actual
            filtro_fecha = datos['Fec. Alta'].dt.date == fecha_actual.date()
            filtro_grupo = datos['Grupo'] == grupo_llamada
            citas_disponibles = datos[filtro_fecha & filtro_grupo]

            if not citas_disponibles.empty:
                cita_seleccionada = citas_disponibles.iloc[0]
                fecha_limite = calcular_fecha_limite(cita_seleccionada['Fec. Alta'], grupo_llamada)
                if fecha_limite >= fecha_actual:
                    # Reservar la cita
                    if fecha_actual not in agenda:
                        agenda[fecha_actual] = {'P1': 0, 'P2': 0, 'P3': 0}
                    agenda[fecha_actual][grupo_llamada] += 1
                else:
                    penalizaciones += 1
            else:
                penalizaciones += 1

    return penalizaciones, agenda

# Datos de entrada para la simulación (ajustar según tus necesidades)
min_llamadas_por_dia = 10
max_llamadas_por_dia = 50

# Ejecutar la simulación y obtener los resultados
penalizaciones_total, citas_asignadas = simular_llamadas_semana(datos, min_llamadas_por_dia, max_llamadas_por_dia)

# Mostrar el resultado
print(f"Total de penalizaciones: {penalizaciones_total}")
print("Citas asignadas:")
for fecha, espacios in citas_asignadas.items():
    print(f"{fecha.strftime('%d/%m/%Y')}: {espacios['P1']} P1, {espacios['P2']} P2, {espacios['P3']} P3.")
