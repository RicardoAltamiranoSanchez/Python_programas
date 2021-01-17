from psycopg2 import pool
from logger_base import logger
import sys
class Conexion:
    __usuario='postgres'
    __host='127.0.0.1'
    __contrasenia='admin'
    __puerto='5432'
    __bd='Personas'
    __min_con=1
    __max_con=5
    __pool=None
    @classmethod
    def Obtener_pool(cls):
     if cls.__pool is None:
         try:
          cls.__pool=pool.SimpleConnectionPool(      cls.__min_con,
                                                     cls.__max_con,
                                                     host=cls.__host,
                                                     user=cls.__usuario,
                                                     password=cls.__contrasenia,
                                                     port=cls.__puerto,
                                                     database=cls.__bd)
          logger.debug(f'Conexion en pool exitosa{cls.__pool}')
          return cls.__pool
         except Exception as e:
             logger.error(f'Error en el pool{e}')
             sys.exit()
     else:
         return cls.__pool        
             
    
    @classmethod
    def Obtener_conexion(cls):
           conexion=cls.Obtener_pool().getconn()
           logger.debug(f'Obteniendo conexion atravez del pool{conexion}')
           return conexion
       
    @classmethod
    def Liberar_pool(cls,conexion):
        cls.Obtener_pool().putconn(conexion)
        logger.debug(f'regresemos la conexion al pool {conexion}')
        logger.debug(f'Estado del pool {cls.__pool}')
        
    @classmethod
    def Cerra_pool(cls):
        cls.Obtener_pool().closeall()
        logger.debug(f'Cerramos la conexione del pool {cls.__pool}')
                       
     
            
            
            
            
if __name__=='__main__':
  conexion1=Conexion.Obtener_conexion()
  conexion2=Conexion.Obtener_conexion()
  Conexion.Liberar_pool(conexion1)
  Conexion.Liberar_pool(conexion2)
  Conexion.Cerra_pool()