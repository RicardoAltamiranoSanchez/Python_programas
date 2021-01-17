from logger import logger
while True:
    logger.debug(f'Elige una opcion\n'
                 f'1.Seleccionar\n'
                 f'2.Insertar\n'
                 f'3.Actualizar\n'
                 f'4.Eliminar\n')
    opcion=int(input('Digite la opcion'))
    