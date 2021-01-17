from Persona import Persona
from logger import logger
from Conexion import Conexion
import sys

class PersonaDAO:
    __SELECCIONAR='SELECT * FROM  personas2;'
    __INSERTAR='INSERT INTO personas2(Nombre,Apellido,Correo) VALUES(%s,%s,%s);'
    __ACTUALIZAR='UPDATE personas2 set nombre=%s,apellido=%s,correo=%s WHERE id_persona=%s;'
    __ELIMINAR='DELETE personas2 where id_persona=%s'
    @classmethod
    def seleccionar(cls):
        try:
            cursor=Conexion.Obtenercursor()
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros=cursor.fetchall()
            personas=[]
            for registro in registros:
               persona=Persona(registro[0],registro[1],registro[2],registro[3])
               personas.append(persona)
               Conexion.Cerrar_conexion()
               return  personas  
            
        except Exception as e:
            logger.error(f'Error en la consulta f{e}')
            sys.exit()
            
    @classmethod
    def insertar(cls,persona):
        try:
           conexion=Conexion.Obtenerconexion()
           cursor=Conexion.Obtenerconexion().cursor()
           logger.debug(cursor.mogrify(cls.__INSERTAR))
           logger.debug(f'Persona a insertar {persona}')
           insertar_persona=(persona.getNombre(),persona.getApellido(),persona.getCorreo())
           cursor.execute(cls.__INSERTAR,insertar_persona)
           conexion.commit()
           return cursor.rowcount
        except Exception as e:   
            conexion.rollback()
            logger.error(f'Error al insertar {e}')
        finally:
            Conexion.Cerrar_conexion()    
        
                
            
if __name__=='__main__':
    #registro=PersonaDAO.seleccionar()
    #for p in registro:
     # logger.debug(p)
     p=Persona(nombre='victor',apellido='joto',correo='Maricon')
     resgistro=PersonaDAO.insertar(p)
     logger.debug(f'persona ingresada {resgistro}')