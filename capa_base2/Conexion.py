from logger import logger
import psycopg2 as bd
import sys
class Conexion:
    __basedatos='prueba'
    __username='postgres'
    __password='admin'
    __puerto='5432'
    __host='127.0.0.1'
    __conexion=None
    __cursor=None
    @classmethod
    def Obtenerconexion(cls):
      if cls.__conexion is None:
       try:
           cls.__conexion=bd.connect(user=cls.__username,
                                     database=cls.__basedatos,
                                     password=cls.__password,
                                     host=cls.__host,
                                     port=cls.__puerto )
                               
           logger.debug(f'Conexion exitosa {cls.__conexion}')
           return cls.__conexion
       except Exception as e:
           logger.error(f'Error en la conexion {e}')
           sys.exit()
       else:
          return cls.__conexion
     
    @classmethod
    def Obtenercursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor=cls.Obtenerconexion().cursor()
                logger.debug(f'Cursor abierto {cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                logger.error(f'Error al abrir el cursor {e}')
                sys.exit()
        else:
            return cls.__cursor        
    @classmethod
    def Cerrar_conexion(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            
            except Exception as e:
                logger.error(f'Error al cerrar el cursor {e}')
                sys.exit()
        else:
            pass
        
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
              
                
            except Exception as e:
                logger.error(f'Error al cerrar conexion {e}')
                sys.exit() 
        else:
            pass          
        logger.debug(f'Se cerraron los objetos de cursor y conexion')
        
if __name__=='__main__':

 Conexion.Obtenercursor()
 Conexion.Cerrar_conexion() 
          
