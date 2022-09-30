# En este segundo ejercicio, tendréis
# que crear un programa que tenga una clase llamada Alumno que tenga
# como atributos su nombre y su nota. Deberéis de definir los métodos
# para inicializar sus atributos, imprimirlos y mostrar un mensaje con
# el resultado de la nota y si ha aprobado o no.

class Alumno:
    _nombre = None
    _nota = None

    def __init__(self):
        self._nombre = ""
        self._nota = 0

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNota(self):
        return self._nota

    def setNota(self, nota):
        self._nota = nota

a1 = Alumno()
a1.setNombre(input("Ingrese nombre: "))
a1.setNota(input("Ingrese nota: "))

if int(a1.getNota()) > 6:
    print(a1.getNombre(), " Aprobo !! la nota es ", a1.getNota())
else:
    print("Desaprobastes ", a1.getNombre(),"la nota es ", a1.getNota())
