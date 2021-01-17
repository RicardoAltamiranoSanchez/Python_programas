from logger import logger
from psycopg2 import pool
import sys
class Conexion:
    __usuario='postgres'
    __contrasenia='admin'
    __host='127.0.0.1'
    __port='5432'
    __db='labo'
    __min=1
    __max=5
    __pool=None
    
    @classmethod
    def Obtener_pool(cls):
       if cls.__pool is None:
           try:
                cls.__pool=pool.SimpleConnectionPool(cls.__min,
                                             cls.__max,
                                             host=cls.__host,
                                             user=cls.__usuario,
                                             password=cls.__contrasenia,
                                             port=cls.__port,
                                             database=cls.__db
                                            
                                             )
                logger.debug(f'Obteniendo pool exitosamente cls.__pool')
                return cls.__pool
           except Exception as e:
               logger.error(f'Error al obtener el pool {e}')
               sys.exit()
    @classmethod
    def Obtener_conexion(cls):
           try:
               conexion=cls.Obtener_pool().getconn()
               logger.debug(f'Obteniendo conexion exitosamente {conexion}')
               return conexion   
           except Exception as e:
               logger.error(f'Error al obtener la conexion {e}')
    @classmethod
    def liberar_pool(cls,conect):
        try:
            
            cls.Obtener_pool().putconn(conect)
            logger.debug(f'Liberando pool')               
        except Exception  as e:
            logger.error(f'Error al liberar el pool {e}')
           
    @classmethod
    def Cerrar_conexion(cls):
        cls.Obtener_pool().closeall()
        logger.debug(f'Cerrando conexiones')
        
if __name__=='__main__':
    
     conexion1=Conexion.Obtener_conexion() 
     conexion2=Conexion.Obtener_conexion() 
     Conexion.liberar_pool(conexion1)
     Conexion.liberar_pool(conexion2)
     Conexion.Cerrar_conexion()      
                