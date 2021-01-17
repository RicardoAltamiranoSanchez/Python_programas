from pelicula import Pelicula
from catalogo_peliculas import Catalogo
opcion=0
while opcion<4:
    print("1:Agregar pelicula")
    print("2:Lista peliculas")
    print("3:Eliminar pelicula")
    print("4:Salir")
    opcion=int(input("Digite la opcion que quieras\n"))
    if(opcion==1):
         nombre=input("Escriba el nombre\n")
         p=Pelicula(nombre)
         
         Catalogo.agregar_peliculas(p)
    elif(opcion==2):
        Catalogo.listar_peliculas()
    elif(opcion==3):
        Catalogo.eliminar_pelicula()
    elif(opcion==4):
        pass
    else:
        print("Esa opcion no existe")             
        