from usuario_dao import UsuarioDao
from logger_base import logger
from usuario import Usuario

opcion = None
while opcion != '5':
    print('Opciones:')
    print('1. Listar usuarios:')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = input('Escribe tu opción (1-5): ')
    if opcion == '1':
        # Listado de usuarios
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            logger.info(usuario)
    elif opcion == '2':
        # Insertamos un nuevo registro
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertadas = UsuarioDao.insertar(usuario)
        logger.info(f'Usuarios insertados: {usuarios_insertadas}')
    elif opcion == '3':
        # Actualizar un registro existente
        id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Escribe el nuevo password: ')
        
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizadas = UsuarioDao.actualizar(usuario)
        logger.info(f'Usuarios actualizadas: {usuarios_actualizadas}')
    elif opcion == '4':
        # eliminar usuario existente
        id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario_var)
        usuarios_eliminadas = UsuarioDao.eliminar(usuario)
        logger.info(f'Usuarios eliminadas: {usuarios_eliminadas}')
else:
    print('Salimos de la aplicación...')