import logging
import inspect

# Crea un archivo ".log" donde tomara registro de timpo, funcion y mensaje
# donde cada funcion del archivo "selenium_driver", lo utilizara para ir registrando cada accion

def CustomLogger(logLevel=logging.DEBUG):
    # Toma el nombre de las clases o metodos donde se este llamando la funcion
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # por default el log de todos los mensajes
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: - %(name)s: - %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

