from logger import logger
from Conexion import Conexion
import sys
class Cursor_DAO:
    def __init__(self):
        self.__conexion=None
        self.__cursor=None
    
    def __enter__(self):
        self.__conexion=Conexion.Obtener_conexion()
        self.__cursor=self.__conexion.cursor()
        logger.debug(f'Abriendo el cursor')
        return self.__cursor
    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value:
            self.__cursor.rollbacK()
            logger.error(f'Error al ejecutar el cursor {exception_value}')
            sys.exit()
        else:
            self.__conexion.commit()
            logger.debug(f'Guardando commit')
           
            self.__cursor.close()
            logger.debug(f'Cerrando cursor')
            Conexion.liberando_pool(self.__conexion)
            logger.debug(f'liberando conexion')
  
if __name__=='__main__':
       with Cursor_DAO() as cursor:
         cursor.execute('SELECT *FROM persona;')
         logger.debug(f'{cursor.fetchall()}')                        
