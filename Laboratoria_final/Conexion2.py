from logger import logger
from psycopg2 import pool
import sys
class Conexion2:
    __usuario='postgres'
    __contrasenia='admin'
    __db='labo'
    __port_db_='5432'
    __host='127.0.0.1'
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
                                                     port=cls.__port_db,
                                                     database=cls.__db
                                                     )
                logger.debug(f'pool existosa {cls.__pool}')
                return cls.__pool
                
            except Exception as e:
                logger.error(f'Error en la conexion {e}')
    
    @classmethod
    def Obtener_conexion(cls):
        conexion=cls.Obtener_pool().getconn()
        logger.debug(f'Conexion existosa {conexion}')
        return conexion            
                
if __name__=='__main__':
   
    Conexion2.Obtener_conexion()                
                