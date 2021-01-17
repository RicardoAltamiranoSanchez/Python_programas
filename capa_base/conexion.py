from logger_base import logger
import psycopg2 as bd
import sys
class Conexion:
    __database="prueba"
    __username="postgres"
    __password="admin"
    __port="5432"
    __host="127.0.0.1"
    __conexion=None
    __cursor=None
    @classmethod
    def obtenerconexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion=bd.connect(host=cls.__host,
                                          user=cls.__username,
                                          password=cls.__password,
                                          port=cls.__port,
                                          database=cls.__database)
                logger.debug(f'Conexion exitosa:{cls.__conexion}')
                return cls.__conexion
            except Exception as e:
                 logger.error(f'Error en la conexion {e}')
                 sys.exit()
        else:
            return cls.__conexion   
    
    @classmethod
    def obtener_cursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor=cls.obtenerconexion().cursor()
                logger.debug(f'Abierto el cursor exitosamente:{cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                logger.error(f'Error en el cursor {e}')
                sys.exit()
        else:
            cls.__cursor
            
    @classmethod       
    def cerrar_bd(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
                logger.debug(f'Cerrando el cursor ')
            except Exception as e:
                logger.error(f'Error el a cerrar el cursor {e}')
                sys.exit()
        else:
            pass
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
                logger.debug(f'Cerrando la conexion')
            except Exception as e:
                logger.error(f'Error al cerra la conexion {e}')
                sys.exit()        
        else:
            pass    
                
if __name__=='__main__':
    
    logger.info(Conexion.obtener_cursor())
    Conexion.cerrar_bd()
    
                  
        