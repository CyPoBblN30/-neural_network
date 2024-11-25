import logging


logging.basicConfig(filename='first.log', level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

logging.critical('Error')