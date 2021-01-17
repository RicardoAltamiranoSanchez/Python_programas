from logger_base import logger
from Cursor_del_pool import Cursor_pool
from persona import Persona
class Persona_DAO:
    __SELECCIONAR='SELECT * FROM persona ORDER BY id_persona;'
    __INSERTAR='INSERT INTO persona(nombre,apellido,correo) VALUES(%s,%s,%s);'
    __Actualizar='UPDATE persona SET nombre=%s,apellido=%s,correo=%s WHERE id_persona=%s;'
    __ELIMINAR='DELETE FROM persona WHERE  id_persona=%s;'
    
    
    
    
    @classmethod
    def Seleccionar(cls):
     with Cursor_pool() as cursor: 
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registro=cursor.fetchall()
        personas=[]
        for i in registro:
            persona=Persona(i[0],i[1],i[2],i[3])
            personas.append(persona)
           
        return personas
    @classmethod
    def Insertar(cls,persona):
      
          with Cursor_pool() as cursor: 
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar {persona}')
            valores=(persona.getNombre(),persona.getApellido(),persona.getCorreo())
            cursor.execute(cls.__INSERTAR,valores)
            return  cursor.rowcount
      
        
    @classmethod
    def Actualizar(cls,persona):
         with Cursor_pool() as cursor: 
            logger.debug(cursor.mogrify(cls.__Actualizar))
            logger.debug('Actualizacion de la persona {persona}')
            valores=(persona.getNombre(),persona.getApellido(),persona.getCorreo(),persona.getId())
            cursor.execute(cls.__Actualizar,valores)
            
            return cursor.rowcount      
    @classmethod
    def Eliminar(cls,persona):
         with Cursor_pool() as cursor: 
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            valores=(persona.getId(),)
            cursor.execute(cls.__ELIMINAR,valores)
            return cursor.rowcount
        
if __name__=='__main__':
   #p=Persona_DAO.Seleccionar()
   #for P in p:
      #logger.debug(P)   
  #p=Persona(nombre='Superman',apellido='ken',correo='hombredeacero@gmail.com')
  #pd=Persona_DAO.Insertar(p)
  #logger.debug(pd)
    #p=Persona(nombre='robin',apellido='hoot',correo='robaniños@gmail.com',id_persona=6)
    #P=Persona_DAO.Actualizar(p)
    #logger.debug(P)
  #p=Persona(id_persona=6)
  #P=Persona_DAO.Eliminar(p)
  #logger.debug(P)