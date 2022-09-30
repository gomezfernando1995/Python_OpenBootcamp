from abc import ABC, abstractmethod

class Vehiculo(ABC):
        color=""
        ruedas=4
        puertas=0

class Coche(Vehiculo):
        Velocidad=0
        Cilindrada=0

v =  Vehiculo()
print(v.ruedas)