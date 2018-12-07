import logging
from functools import wraps
import time


def create_logger(filename, level):
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        root_logger.removeHandler(handler)
    fh = logging.FileHandler(filename)
    root_logger.addHandler(fh)
    root_logger.setLevel(logging.DEBUG)
    return root_logger


def log_debug(function): 
    
    @wraps
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logging.debug("start {} at {}}".format(function.__name__, start_time))
        res = function(*args,**kwargs)
        end_time = time.time()
        logging.debug("ends {} at {}".format(function.__name__, end_time))
        logging.debug("elapsed time for {} at {} with args {} and kwargs {}".format(function.__name__, end_time, args, kwargs))
        return res
    
    return wrapper
