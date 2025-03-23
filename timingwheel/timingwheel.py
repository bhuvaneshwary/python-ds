import logging
import select
import time
logger = logging.getLogger(__name__) 

class TimingWheel :
    def __init__(self):
        pass
    def initialise(self,seconds):
        while True:
            start = time.time()
            select.select([],[],[],seconds)
            end = time.time()
            print(f"Timer ended,ELAPSED TIME :{end-start:.2f} seconds(s)")

    def start_timer(self):
        logger.info("start")
    def update_timer(self):
        logger.info("update")
    def stop_timer(self):
        logger.info("stop")
