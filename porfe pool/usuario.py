from logger_base import logger

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password

    def __str__(self):
        return (
            f'Id Usuario: {self.__id_usuario}, '
            f'Username: {self.__username}, '
            f'Password: {self.__password} '
        )

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_id_usuario(self):
        return self.__id_usuario

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario


if __name__ == '__main__':
    usuario1 = Usuario(1, 'jperez', '123')
    logger.debug(usuario1)
    # simulando un objeto a insertar de tipo usuario
    usuario2 = Usuario(username='kgomez', password='543')
    logger.debug(usuario2)
    # simular el caso de eliminar un objeto de tipo usuario
    usuario3 = Usuario(id_usuario=2)
    logger.debug(usuario3)