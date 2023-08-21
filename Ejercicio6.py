class Persona:
  
    def __init__(self, nombre = None, edad = None, dni = None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni


    @property
    def nombre(self):
        return self.__nombre
       
     
    @property
    def edad(self):
        return self.__edad
     
     
    @property
    def dni(self):
        return self.__dni


    @nombre.setter
    def nombre(self,nuevo_nombre):
        if self.__nombre == nuevo_nombre or len(nuevo_nombre) < 3:
            print("Nombre inválido")
        else:
            self.__nombre = nuevo_nombre

    @edad.setter
    def edad(self,edad):
        if self.__edad < 0 or self.__edad > 100:
            print("Rango de edad inválido")
        else:
            self.__edad = edad    


    @edad.setter
    def dni(self,dni):
        if self.__dni < 0 or self.__dni > 100000000:
            print("DNI inválido")
        else:
            self.__dni = dni            

e1 = Persona("Juan",15,40244)





print(e1.dni)