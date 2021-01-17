from persona import Persona
from conexion import Conexion
from logger_base import logger
class Persona_DAO:
    __seleccionar='SELECT *FROM persona;'
    __insertar='INSERT INTO persona(nombre,apellido,correo) VALUES(%s,%s,%s);'
    __Actualizar='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id=%s;'
    #Metodo seleccionar para la base de datos
    @classmethod
    def Seleccionar_bd(cls):
        cursor=Conexion.obtener_cursor()
        logger.debug(cursor.mogrify(cls.__seleccionar))
        cursor.execute(cls.__seleccionar)
        registros=cursor.fetchall()
        personas=[]
        for registro in registros:
            persona=Persona(registro[0],registro[1],registro[2],registro[3])
            personas.append(persona)
            return personas
    @classmethod
    def Inserta_persona(cls,persona):
        try:
            conexion=Conexion.obtenerconexion()
            cursor=Conexion.obtener_cursor()
            logger.debug(cursor.mogrify(cls.__insertar))
            logger.debug(f'Persona insertada{persona}')
            registro=(persona.getNombre(),persona.getApellido(),persona.getEmail())
            cursor.execute(cls.__insertar,registro)
            cantidad=cursor.rowcount
            conexion.commit()
            logger.debug(f'Inserccion existosa {cantidad}')
        except Exception as e:
            logger.ERROR(f'Error al inserta persona {e}')
            conexion.rollback()
        finally:
            conexion.close()
            cursor.close()
    @classmethod
    def Actualizar_bd(cls,persona,nombre):
        try:
            conexion=Conexion.obtenerconexion()
            cursor=Conexion.obtener_cursor()
            logger.debug(cursor.mogrify(cls.__Actualizar))
            logger.debug(f'Persona Acutalizada {persona}')
            registro=(persona.getNombre(),persona.getApellido,persona.getEmail(),nombre)      
            cursor.execute(cls.__Actualizar,registro)
            conexion.commit()
            cantidad=cursor.rowcount
            logger.debug(f'Actualizacion con exito {cantidad} ')
            
        except Exception as e:
            logger.ERROR(f'Error al actualizar persona {e}')
            conexion.rollback()
        finally:
            conexion.close()
            cursor.close()            
    
    @classmethod
    def  Eliminar_bd(cls):
         try:
             conexion=Conexion.obtenerconexion()
             cursor=Conexion.obtener_cursor()
             logger.debug(cursor.mogrify(cls.__eliminar))
             logger.debug(f'Persona eliminada {persona}')
             
             
         except expression as identifier:
             pass
          
if __name__=='__main__': 
    #persona=Persona_DAO.Seleccionar_bd()
    #for p in persona:
     #   logger.debug(p)      
    #p=Persona(nombre='Ricardo',apellido='Altamirano',email='ricardo@gmail.com')  
    #Persona_DAO.Inserta_persona(p)
    
    p=Persona('Rodrigo','Hernandez','rodrigo@gmail.com')
    nombre=input('Digite el nombre que quieres actualizar\n')
     
    Actualizar=Persona_DAO.Actualizar_bd(p,nombre)   
    