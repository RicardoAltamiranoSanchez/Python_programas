from psycopg2 import pool
from logger import  logger
import sys
class Conexion:
    __usuario='postgres'
    __bd='labo'
    __contrasenia='admin'
    __puerto='5432'
    __host_db='127.0.0.1'
    __min=1
    __max=5
    __pool=None
    @classmethod
    def Obtener_pool(cls):
       if cls.__pool is None:
           try:
                cls.__pool=pool.SimpleConnectionPool(cls.__min,
                                             cls.__max,
                                             host=cls.__host_db,
                                             user=cls.__usuario,
                                             password=cls.__contrasenia,
                                             port=cls.__puerto,
                                             database=cls.__bd)
                logger.debug(f'Obteniendo pool {cls.__pool}')
                return cls.__pool
           except Exception as e:
                 logger.error(f'Error al obtener el pool {e}')
                 sys.exit()
       else:
            return cls.__pool    
    @classmethod
    def Obtener_conexion(cls):
       try:
            conexion=cls.Obtener_pool().getconn()
            logger.debug(f'Obteniedo conexion {conexion}')
            return conexion
       except Exception as e:
           logger.debug(f'Error al obtener conexion {e}')
           sys.exit()
    @classmethod
    def liberando_pool(cls,conexion):
        try:
            cls.Obtener_pool().putconn(conexion)
            logger.debug(f'liberando esta conexion {conexion}')
            logger.debug(f'Estado de pool{cls.__pool}')
        except Exception as e:
            logger.error(f'Error al devolver el pool {e}')
            sys.exit() 
            
    @classmethod
    def Cerrar_pool(cls):
        try:
            cls.Obtener_pool().closeall()
            logger.debug(f'Cerrando todas las conexion de pool')
        except Exception as e:
            logger.error(f'Error al cerrar conexion {e}')                        
    
if __name__=='__main__':
    Conexion.Obtener_pool()    
    conexion1=Conexion.Obtener_conexion() 
    conexion2=Conexion.Obtener_conexion()   
    Conexion.liberando_pool(conexion1) 
    Conexion.liberando_pool(conexion2) 
    Conexion.Cerrar_pool()