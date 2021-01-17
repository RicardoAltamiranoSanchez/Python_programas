from logger import logger
from Usuario import Usuario
from Conexion import Conexion
from Cursor_pool import Cursor_DAO
class Usuario_DAO:
    __SELECCIONAR='SELECT *FROM persona;'
    __INSERTAR='INSERT INTO persona(nombre,contraseña)VALUES(%s,%s);'
    __ACTUALIZAR='UPDATE persona SET nombre=%s,contraseña=%s WHERE id_usuario=%s;'
    __ELIMINAR='DELETE FROM persona WHERE id_usuario=%s;'
    @classmethod
    def seleccionar(cls):
        with Cursor_DAO() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registro=cursor.fetchall()
            persona=[]
            logger.debug(f'lista')
            for r in registro:
                Persona=Usuario(r[0],r[1],r[2])
                persona.append(Persona)
            return persona  
    @classmethod
    def insertar(cls,usuario):
        with Cursor_DAO() as cursor:
          logger.debug(cursor.mogrify(cls.__INSERTAR)) 
          persona=(usuario.getNombre(),usuario.getContrasenia())
          cursor.execute(cls.__INSERTAR,persona)
          logger.debug(f'Usuario Insertado') 
          return cursor.rowcount
           
    @classmethod
    def actualizar(cls,usuario):
        with Cursor_DAO() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Usuario a actualizar {usuario}')
            persona=(usuario.getNombre(),usuario.getContrasenia(),usuario.getId())
            cursor.execute(cls.__ACTUALIZAR,persona)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,usuario):
        with Cursor_DAO() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))    
            logger.debug(f'Eliminando usuario{usuario}')
            persona=(usuario.getId(),)
            cursor.execute(cls.__ELIMINAR,persona)
            return cursor.rowcount
                   
           
if __name__=='__main__':
   #u=Usuario_DAO.seleccionar()                
   #logger.debug(u)
   #U=Usuario(nombre='Fernado',password='fer')
   #UD=Usuario_DAO.insertar(U)
   #logger.debug(UD)
   U=Usuario(4)
   Usuario_DAO.eliminar(U)          
   