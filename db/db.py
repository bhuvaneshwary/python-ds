import logging
class DataBase :
    def __init__(self):
        pass
    def store(self):
        logging.info("Entered store")
    def store_with_timeout(self):
        logging.info("Entered store_with_timeout ")
    def retrieve(self):
        logging.info("Entered retrieve")
    def database_load(self):
        logging.info("Entered database_load")
    def count(self):
        logging.info("Entered count")
    