from logger_base import logger
class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None):
        self.__id_persona=id_persona
        self.__nombre=nombre
        self.__apellido=apellido
        self.__email=email
    def __str__(self):
        return(
            f'Id_persona={self.__id_persona},'
            f'Nombre={self.__nombre},'
            f'Apellido={self.__apellido},'
            f'Email={self.__email}'
        ) 
    def getId(self):
        return self.__id_persona    
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getEmail(self):
        return self.__email    
    def setNombre(self,nombre):
        self.__nombre=nombre
    def setApellido(self,apellido):
        self.__apellido=apellido
    def setCorreo(self,email):
        self.__email=email           

if __name__=='__main__':
    p=Persona(id_persona=None,nombre="Ricardo",apellido='Altamirano',email='ricardo@gmail.com')
    logger.debug(p)  
        
        
       

