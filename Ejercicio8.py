from Ejercicio6 import Persona
from Ejercicio7 import Cuenta

class CuentaJoven(Cuenta):

    def __init__(self, titular=None, cantidad=None,bonificacion = None):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion


    @property
    def bonificacion(self):
        return self.__bonificacion
    

    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        if self.titular.es_mayor_de_edad() and self.titular.edad < 25:
            return True
        else:
            return False

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            pass
    

    def mostrar(self):
        print(f"Bonificación: {self.__bonificacion}")

persona = Persona("Mario",18,40840192)
cv = CuentaJoven(persona,12.5,45)

print(cv.cantidad)
cv.retirar(14.5)
print(cv.cantidad)
cv.mostrar()