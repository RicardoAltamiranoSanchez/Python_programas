from logger import logger
from Conexion import Conexion
import sys
class Cursor:
    def __init__(self):
        self.__Conexion=None
        self.__cursor=None
        
    def __enter__(self):
        self.__Conexion=Conexion.Obtener_conexion()
        self.__cursor=self.__Conexion.cursor()
        logger.debug('Obteniendo Conexion')
        return self.__cursor
    
    def __exit__(self,exception_type,exception_value,exception_traceback): 
       
            if self.__exception_value is not None:
                self.__cursor.rollback()
                logger.error("error {self.__exception_valuer")
            else:
                self.__cursor.commit()
                logger.debug(f'haciendo commit')
                self.__cursor.close()
                Conexion.liberar_pool(self.__Conexion)
                
                    
         