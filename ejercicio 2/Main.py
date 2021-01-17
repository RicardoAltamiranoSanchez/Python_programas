from Usuario import Usuario
from UsuarioDAO import Usuario_DAO
from logger import logger
while True:
    print(f'Opciones\n'
                 f'1.Ver la lista de usuario en el servidor\n'
                 f'2.Agregar nuevo usuario ala servidor\n'
                 f'3.Actualizar a un usuario en el servidor\n'
                 f'4.Eliminar a un usuario del servidor\n'
                 f'5.Salir')
    opcion=int(input('Eliga una opcion\n'))
    if opcion ==1:
        print('Lista de usuarios')
        lista=Usuario_DAO.seleccionar()
        for l in lista:
            print(l)
    elif opcion==2:
        print('Agregando nuevo registro')
        nombre=input('Digite el nombre para el usuario del nuevo ingreso\n')
        contrasenia=input('Digite la contrasenia que tendra el usuario de nuevo ingreso\n')
        info=Usuario(nombre=nombre,password=contrasenia)
        Usuario_DAO.insertar(info)
        logger.info(f'Usuario insertado {info}')
    elif opcion==3:
        print('Actualizando usuario')
        id=int(input('Digite el id del usuario a actualizar\n'))
        nombre=input('Digite el nombre\n')
        contrasenia=input('Digite la contraseña\n')
        info=Usuario(id,nombre,contrasenia)
        Usuario_DAO.actualizar(info)
        logger.info(f'Actualizacion de usuario {info}')
    elif opcion==4:
        print('Eliminado usuario del servidor')
        id=int(input('Digite el id del usuario a eliminar\n'))
        info=Usuario(id)
        Usuario_DAO.eliminar(info)
        logger.info(f'Eliminacion de usuario {info}')
    elif opcion==5:
        break
    else :
       print(f'Esa opcion no existe\n'
             f'Escoja una opcion que se muestra en el menu de opciones')   
        