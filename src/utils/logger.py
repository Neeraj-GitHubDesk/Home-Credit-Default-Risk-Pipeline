import logging  # to manage log messages
import os   # to work with the file system
from logging.handlers import RotatingFileHandler    # for log rotation

def get_logger(name: str, log_file: str):   #name : src.data.data_trining
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Sets the minimum severity level

    if logger.hasHandlers():    # duplicate logger handling
        return logger
    
    os.makedirs(os.path.dirname(f"logs/{log_file}"), exist_ok=True) # check for log directory

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(f"logs/{log_file}", maxBytes=5*1024*1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger