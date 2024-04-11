import logging


logging.basicConfig(filename="log",level=logging.INFO ,
                     format='%(asctime)s:%(levelname)s:%(message)s:%(name)s:%(threadName)s:%(processName)s')
def add(firstnumber:int, seconnumber:int) -> float:

    return firstnumber + seconnumber


logging.warning(add(4,5))
logging.info(add(34,830))