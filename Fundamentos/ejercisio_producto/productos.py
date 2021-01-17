class Producto:
    contador_producto=0
    def __init__(self,nombre,precio):
        Producto.contador_producto+=1
        self.__id_producto=Producto.contador_producto
        self.__nombre=nombre
        self.__precio=precio
    def getId(self):
        return self.__id_producto 
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio   
    def __str__(self):
         return "id:"+str(self.getId())+"\nNombre:"+self.getNombre()+"\nPrecio:"+str(self.getPrecio())
    