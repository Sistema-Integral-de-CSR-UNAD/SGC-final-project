import logging
import os

def configurar_logger():
    """
    Configurar el sistema de logs para poder registrar los eventos ocurridos en un
    archivo externo. Este código denifirá el comportamiento del registro.
    """
    log_dir = "logs"

    try:
        #En caso de no existir el directorio de logs, se crea de manera automática
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            print (f"Directorio '{log_dir}' creado automáticamente")
    except Exception as e:
        print(f"Aviso: No se pudo crear la carpeta de logs: {e}")
        log_dir = "." #Si no se puede crear, se guardarán los logs en la raiz

    log_path = os.path.join(log_dir, "sistema.log")

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8"
        )
    return logging.getLogger("SoftwareFJ")