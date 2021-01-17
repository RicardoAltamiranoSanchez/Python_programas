from productos import Producto
from ordenes import Ordenes
producto=Producto("Chamarra",1250.00)
producto2=Producto("Pantalon",400)
producto3=Producto("Camisa",700)
productos=[producto,producto2]
orden=Ordenes(productos)
orden.agregar_producto(producto3)
print(orden)
print(orden.total())