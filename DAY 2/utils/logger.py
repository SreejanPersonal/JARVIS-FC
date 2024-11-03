import logging
from termcolor import colored

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    class ColoredFormatter(logging.Formatter):
        def format(self, record):
            if record.levelno == logging.INFO:
                color = 'cyan'
            elif record.levelno == logging.WARNING:
                color = 'yellow'
            elif record.levelno == logging.ERROR:
                color = 'red'
            else:
                color = 'white'
            
            record.msg = colored(record.msg, color)
            return super().format(record)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = ColoredFormatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger