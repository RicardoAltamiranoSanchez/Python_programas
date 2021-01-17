class Ordenes:
    contador_ordenes=0
    def __init__(self,producto):
        Ordenes.contador_ordenes+=1
        self.__id_orden=Ordenes.contador_ordenes
        self.__producto=producto
    def agregar_producto(self,producto_nuevo):
        self.__producto.append(producto_nuevo)
    def total(self):
        total=0
        for p in self.__producto:
            total=total+p.getPrecio()
        return total    
            
    def __str__(self):
        lista_producto=""
        for producto in self.__producto:
           lista_producto+=producto.__str__()+"\n"
        return "Id_orden:"+str(self.__id_orden)+"\nProductos"+lista_producto       