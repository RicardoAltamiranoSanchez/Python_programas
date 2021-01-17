import psycopg2 as bd
from logger_base import logger
import sys
class Conexion:
    __usuario='postgres'
    __host='127.0.0.1'
    __contrasenia='admin'
    __puerto='5432'
    __bd='Personas'
    __conexion=None
    __cursor=None
    @classmethod
    def Obtener_conexion(cls):
        try:
            if cls.__conexion is None:
                
                 cls.__conexion=bd.connect(host=cls.__host,
                                      user=cls.__usuario,
                                      password=cls.__contrasenia,
                                      port=cls.__puerto,
                                      database=cls.__bd)
                 logger.debug(f'Conexion existosas {cls.__conexion}')
                 return cls.__conexion
             
            else:
                return cls.__conexion
        
        except Exception as e:
            logger.error(f'Error en la conexion {e}')
            sys.exit()
    @classmethod
    def Obtener_cursor(cls):
        try:
            if cls.__cursor is None:
                cls.__cursor=cls.Obtener_conexion().cursor()
                logger.debug(f'Cursor abierto {cls.__cursor}')
                return cls.__cursor
            else:
                return cls.__cursor               
        except Exception as e:
            logger.error(f'Error al abrir el cursor')
            sys.exit()    
         
         
    @classmethod
    def Cerra_conexion(cls):
        try:
            if cls.__cursor is not None:
                cls.__cursor.close()
                
        except Exception as e:
            logger.error(f'Error al cerrar el cursor')
            sys.exit()
        try:
            if cls.__conexion is not None:
                cls.__conexion.close()
        except Exception as e:
            logger.error(f'Error al cerrar la conexion') 
            sys.exit() 
        logger.debug(f'Cerrado cursor y la conexion exitosamente')                  
     
            
            
            
            
if __name__=='__main__':
    Conexion.Obtener_conexion()
    Conexion.Obtener_cursor() 
    Conexion.Cerra_conexion()  