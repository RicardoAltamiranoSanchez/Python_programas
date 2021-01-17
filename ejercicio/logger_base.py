import logging
logger=logging
logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s:,%(levelname)s:,[%(filename)s:,%(lineno)s:],%(message)s:',
                   datefmt='%I:%M:%S %p',
                   handlers=[
                       logging.FileHandler('Capa_datos'),
                       logging.StreamHandler()
                   ])
if __name__=='__main__':
    logging.warning("Mensaje de de peligro")
    logging.debug("Mensaje de debug")
    logging.info("Mensaje de info")
