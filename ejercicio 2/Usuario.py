from logger import logger
class Usuario:
    def __init__(self,id_usuario=None,nombre=None,password=None):
        self.__id_usuario=id_usuario
        self.__nombre=nombre
        self.__password=password
        
    def __str__(self):
        return(f'Id_usuario:{self.__id_usuario}     '
               f'Nombre:{self.__nombre}     '
               f'Contraseña:{self.__password}       ')
    def getId(self):
        return self.__id_usuario
    def setId(self,id):
        self.__id_usuario=id
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getContrasenia(self):
        return self.__password
    def setContrasenia(self,contrasenia):
        self.__password=contrasenia                