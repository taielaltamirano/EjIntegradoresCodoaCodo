class Cuenta:

    def __init__(self, titular = None, cantidad = None):
        if titular == None:
            self.__titular = None
        else:
            self.__titular = titular
        if cantidad == None:
            self.__cantidad = None
        else:
            self.__cantidad = cantidad

    
    @property
    def titular(self):
        return self.__titular
    

    @property
    def cantidad(self):
        return self.__cantidad



    def mostrar(self):
        print(f"Titular: {self.__titular}, Cantidad: {self.__cantidad}")


    def ingresar(self,cantidad):
        if cantidad < 0 :
            pass
        else:
            self.__cantidad += cantidad


    def retirar(self,cantidad):
        self.__cantidad -= cantidad




