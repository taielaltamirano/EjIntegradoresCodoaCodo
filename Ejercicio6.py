class Persona:
  
    def __init__(self, nombre = None, edad = None, documento = None):
        if nombre == None:
            self.__nombre = None
        else:
            self.__nombre = nombre
        if edad == None:
            self.__edad = None
        else:
            self.__edad = edad
        if documento == None:
            self.__documento = None
        else:
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
    def edad(self,nueva_edad):
        
        if nueva_edad <= 0 or nueva_edad > 100 :
            print("Rango de edad inválido")
        else:
            self.__edad = nueva_edad    


    @documento.setter
    def documento(self,documento):
        if documento <= 0:
            print("DNI inválido")
        else:
            self.__documento = documento            


    def mostrar(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__documento}")



    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            return True
        else:
            return False



