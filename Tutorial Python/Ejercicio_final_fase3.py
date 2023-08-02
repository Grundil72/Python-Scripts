# Fase 3: Optimizador

# Para desarrollar el optimizador y saber qué tan bien funciona calcularemos las penalizaciones, 
# por lo que nos aseguraremos de que los clientes reciban la atención a la que tienen derecho según su facturación.

# Asumiremos que el calendario de citas está abierto hasta 1 mes, es decir, la llamada se puede realizar hasta 1 mes después.

# Ordenaremos las llamadas predichas en el apartado anterior para colocarlas con la penalización más baja, lo abordaremos desde una perspectiva matemática. 
# El primer paso será poner el límite de días en el que no haya penalización.

# Las sanciones son:

#   P1: 2 días, es decir, si la cita se da antes de 2 días no hay penalización, de lo contrario se añade 1 punto a la penalización.
#   P2: 3 días, es decir, si la cita se da antes de 3 días no hay penalización, de lo contrario se añade 1 punto a la penalización.
#   P3: 4 días, es decir, si la cita se da antes de 4 días no hay penalización, de lo contrario se añade 1 punto a la penalización.

# Así que:
#   Si uno llama el 01/01/2021 y es P1 su fecha límite sin penalización sería: 03/01/2021.
#   Si uno llama el 01/01/2021 y es P2, su fecha límite sin penalización sería: 04/01/2021.
#   Si uno llama el 01/01/2021 y es P3, su fecha límite sin penalización sería: 05/01/2021.

# Una vez que tenemos la fecha límite de todas las llamadas, tenemos que ordenarlas por su fecha límite en orden ascendente. Independientemente del día en que hayan llamado y del tipo de paciente al que pertenezcan.
# A continuación, completaremos la agenda, supongamos que hay 70 espacios disponibles por día. Para rellenarlo elegiremos las llamadas que hayamos pedido. 
# Comenzaremos colocando el primero y así sucesivamente. Si hay una ranura al día siguiente, se coloca ese día y se resta una ranura disponible, de lo contrario se coloca al día siguiente, 
# y así sucesivamente. Tenga en cuenta que la llamada no se puede realizar el mismo día o el día anterior.
# Finalmente obtendremos todas las llamadas predichas colocadas en el calendario. El resultado será el siguiente en el formato que más le convenga: - 02/01/2021 hay 15 espacios reservados para P1, 8 para P2 y 7 para P3. - 03/01/2021 hay 20 espacios reservados para P1, 7 para P2 y 3 para P3. - 04/01/2021 hay 10 espacios reservados para P1, 10 para P2 y 10 para P3. - Así que durante 1 mes.


import pandas as pd
from datetime import timedelta

datos = pd.read_csv("datos_filtrados.csv", encoding='utf-8', delimiter=';')

'''Convertir la columna 'Fec. Alta' a formato de fecha'''
datos['Fec. Alta'] = pd.to_datetime(datos['Fec. Alta'], dayfirst=True)

'''Definir las sanciones en días para cada grupo'''
sanciones = {'': 0, 'P1': 2, 'P2': 3, 'P3': 4}

'''Calcular la fecha límite sin penalización para cada llamada'''
datos['Fecha Limite'] = datos.apply(lambda row: row['Fec. Alta'] + timedelta(days=sanciones.get(row['Grupo'], 0)), axis=1)

'''Ordenar las llamadas por fecha límite en orden ascendente'''
datos.sort_values(by='Fecha Limite', inplace=True)

'''Inicializar el calendario para el mes con 70 espacios disponibles por día'''
calendario = {}

'''Función para agregar una fecha al calendario con todos los grupos inicializados en cero'''
def agregar_fecha(fecha):
    if fecha not in calendario:
        calendario[fecha] = {'P1': 0, 'P2': 0, 'P3': 0}

'''Llenar el calendario con las llamadas predichas'''
for _, row in datos.iterrows():
    fecha_limite = row['Fecha Limite']
    grupo = row['Grupo']

    while True:
        agregar_fecha(fecha_limite)  # Asegurar que la fecha esté en el calendario
        espacios_reservados = calendario[fecha_limite][grupo]
        espacios_disponibles = 70 - espacios_reservados

        if espacios_disponibles > 0:
            # Agregar la llamada al calendario
            calendario[fecha_limite][grupo] = espacios_reservados + 1
            break
        else:
            # Buscar la siguiente fecha disponible
            fecha_limite += timedelta(days=1)

'''Mostrar el resultado'''
for fecha, espacios in calendario.items():
    print(f"{fecha.strftime('%d/%m/%Y')} hay {espacios['P1']} espacios reservados para P1, {espacios['P2']} para P2 y {espacios['P3']} para P3.")