from logger_base import logger
from conexion import Conexion
class Cursor_pool:
    def __init__(self):
        self.__conect=None
        self.__cursor=None
        
    def __enter__(self):
        logger.debug(f'Abriendo el cursor')
        self.__conect=Conexion.Obtener_conexion()
        self.__cursor=self.__conect.cursor()
        return self.__cursor
        
        
    def __exit__(self,exception_type,exception_value,exception_traceback):
        if exception_value:
            self.__conect.rollback()
            logger.error(f'Error')
        else:
           self.__conect.commit()
           logger.debug(f'haciendo commit')
        self.__cursor.close()
        Conexion.Liberar_pool(self.__conect)       
        
if __name__=='__main__':
     with Cursor_pool() as cursor: 
         cursor.execute('SELECT *FROM persona')
         logger.debug('listado') 
         logger.debug(cursor.fetchall())      
          