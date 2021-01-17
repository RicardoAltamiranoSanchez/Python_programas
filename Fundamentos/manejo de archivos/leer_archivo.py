#archivo = open("C:\\Cursos\\Python\\Fundamentos\\prueba.txt", "r")
archivo = open("prueba.txt", "r")
#print(archivo.read())

#leer algunos caracteres
#print(archivo.read(5))
#print(archivo.read(3))

#leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

#iterarando
#for linea in archivo:
#    print(linea)
    
#leer lineas
#print(archivo.readlines())    

#acceder a una linea de la lista
#print(archivo.readlines()[2])

#abrimos un nuevo archivo
#con a anexamos información a nuestro archivo
#archivo2 = open("copia.txt", "a")
archivo2 = open("copia.txt", "w")
archivo2.write(archivo.read())

archivo.close()
archivo2.close()