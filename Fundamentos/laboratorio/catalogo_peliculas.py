
import os
class Catalogo:
    ruta_archivo="c:\\cursos\\Python\\Fundamentos\\laboratorio\\peliculas.txt"
   
   
    @staticmethod
    def agregar_peliculas(pelicula):
        try:
         archivo=open(Catalogo.ruta_archivo,"a")
         archivo.write(pelicula.__str__())    
         print("Se agrego nueva pelicula")
        
        except Exception as e:
         print(e)
        finally:
         archivo.close()
                
    @staticmethod
    def listar_peliculas():
     try:
         archivo=open(Catalogo.ruta_archivo,"r")
         print("Lista de peliculas")
         print(archivo.read())
     except Exception as e:
         print(e)
     finally:
         archivo.close()    
    @staticmethod
    def eliminar_pelicula():
      try:
         
          os.remove(Catalogo.ruta_archivo)
          print("Eliminando peliculas")
      except Exception as e:
            print(e)
      
                 
             

