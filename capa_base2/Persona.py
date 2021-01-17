class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,correo=None):
        self.__id_persona=id_persona
        self.__nombre=nombre
        self.__apellido=apellido
        self.__correo=correo
        
    def __str__(self):
        return (f'Id_persona={self.__id_persona},'
               f'Nombre={self.__nombre},'
               f'Apellido={self.__apellido},'
               f'Correo={self.__correo}'
        )
    def getid(self):
        return self.__id_persona
    def setid(self,id):
        self.__id_persona=id
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre 
    def getApellido(self):
        return self.__apellido
    def setApellido(self,apellido):
        self.__apellido=apellido
    def getCorreo(self):
        return self.__correo
    def setCorreo(self,correo):
        self.__correo=correo               
        
        
if __name__=='__main__':
    p=Persona(None,'Ricardo','Altamirano','ricardo@gmail.com')    
    print(p)    