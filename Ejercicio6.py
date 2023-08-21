class Persona:
  
    def __init__(self, nombre, edad, documento):
        self.__nombre = nombre
        self.__edad = edad
        self.__documento = documento


    @property
    def nombre(self):
        return self.__nombre
       
     
    @property
    def edad(self):
        return self.__edad
     
     
    @property
    def documento(self):
        return self.__documento


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


    @documento.setter
    def documento(self,documento):
        if self.__documento < 0:
            print("DNI inválido")
        else:
            self.__documento = documento            

e1 = Persona("Juan",15,40244)

e1.nombre = "Pepo"
e1.edad = 40
e1.documento = 40804942

print(e1.nombre)
print(e1.edad)
print(e1.documento)