# Exercise 16: Define the object "car", which can only be oriented according to the directions of the cardinal points, N, S, E, W, and whose velocities are natural numbers, 
# with the following initial state...

# ignition_engine: False
# velocity: 0
# direction: "N ... and the following methods:
# start_engine()
# turn_engine_off(), which only works if the speed is zero. accelerate(), decelerate(), brake(), right_turn(), left_turn(). Write operation, to operate with print.


class Car:

    def __init__(self):
        self.puntosCardinales =  ["Norte","Este", "Sur", "Oeste"]
        self.orientacion = self.puntosCardinales[0]
        self.ignition_engine = False
        self.velocidad = 0
        self.printInfo()
       
    def start_engine(self):
        print("\nSe arranca el vehículo")
        self.ignition_engine = True
    

    def turn_engine_Off(self):
        if self.velocidad == 0 and self.ignition_engine:
            print("\nSe apaga el vehículo")
            self.ignition_engine = False
    

    def accelerate(self, tiempo):
        if not self.ignition_engine: self.start_engine()

        assert tiempo >= 0 and isinstance(tiempo, int), "El tiempo debe ser un numero entero positivo"
        print("\nACELERAR")
        print(f"Velocidad inicial= {self.velocidad}")

        for i in range(1, tiempo+1):
            self.velocidad += i

        print(f"Has acelerado durante {tiempo}s. Tu velocidad actual es: {self.velocidad} km/h")
    

    def decelerate(self, tiempo):
        assert tiempo >= 0 and isinstance(tiempo, int), "El tiempo debe ser un numero entero positivo"
        
        print("\nDECELERAR")
        print(f"Velocidad inicial= {self.velocidad}")

        for i in range(1, tiempo+1): 
            if self.velocidad <= 0:
                self.velocidad = 0
                self.turn_engine_Off()
                break
            else:
                self.velocidad -= i
                if self.velocidad < 0: self.velocidad = 0    

        print(f"Has decelerado durante {i}s. Tu velocidad actual es: {self.velocidad} km/h")
        if self.velocidad==0: self.turn_engine_Off()
    

    def brake(self, tiempo):
        assert tiempo >= 0 and isinstance(tiempo, int), "El tiempo debe ser un numero entero positivo"

        print("\nFRENAR")
        print(f"Velocidad inicial= {self.velocidad}")

        for i in range(1, tiempo+1):
            if self.velocidad <= 0:
                self.velocidad = 0
                self.turn_engine_Off()
                break
            else:
                self.velocidad -= i*i # math.pow(i,2) aunque el valor queda como decimal
                if self.velocidad < 0: self.velocidad = 0    
    
        print(f"Has frenado durante {i}s. Tu velocidad actual es: {self.velocidad} km/h")
        if self.velocidad==0: self.turn_engine_Off()

    def right_turn(self):
        if self.ignition_engine:
            indice_actual = self.puntosCardinales.index(self.orientacion)
            nuevo_indice = (indice_actual+1) % len(self.puntosCardinales)
            self.orientacion = self.puntosCardinales[nuevo_indice]
            print(f"\nHas girado hacia la DERECHA. Tu orientación es {self.orientacion}")
        else:
            print("\nNo puedes girar a la derecha si tienes el vehículo parado")


    def left_turn(self):
        if self.ignition_engine:
            indice_actual = self.puntosCardinales.index(self.orientacion)
            nuevo_indice = (indice_actual-1) % len(self.puntosCardinales)
            self.orientacion = self.puntosCardinales[nuevo_indice]
            print(f"\nHas girado hacia la IZQUIERDA. Tu orientación es {self.orientacion}")
        else:
            print("\nNo puedes girar a la izquierda si tienes el vehículo parado")

    def printInfo(self):
        print("\n*** Información vehíchulo ***")
        print(f"Orientación: {self.orientacion}")
        print(f"¿Motor encendido? {'Si' if self.ignition_engine else 'No'}")
        print(f"Velocidad: {self.velocidad} km/h")
pass


coche = Car()
coche
coche.accelerate(13)
coche.printInfo()
coche.decelerate(54)
coche.printInfo()
coche.brake(4)
coche.accelerate(4)
coche.brake(3)
coche.right_turn()
coche.left_turn()
coche.printInfo()
coche.decelerate(5)
coche.accelerate(15)
coche.right_turn()
coche.brake(4)
coche.left_turn(), coche.left_turn()
coche.printInfo()
coche.decelerate(3)
coche.brake(5)
coche.left_turn(), coche.left_turn(), coche.left_turn(), coche.left_turn(), coche.left_turn()
coche.right_turn()
coche.printInfo()
coche.decelerate(8)
coche.printInfo()

