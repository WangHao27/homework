import datetime
import logging
import functools

def log(level,message=None):
    def decorate(func):
        msg = message if message else func.__name__
        logger = logging.getLogger(msg)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level,msg)
            ch = logging.StreamHandler()
            ch.setLevel(level)
            formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                          '-%(levelname)s-[日志信息]: %(message)s',
                                          datefmt='%a, %d %b %Y %H:%M:%S')
            ch.setFormatter(formatter)
            logger.addHandler(ch)
            res = func(*args, **kwargs)
            return res
        return wrapper
    return decorate
