import zlib
from logger import Logger 

class Downlink_Producer:
    def __init__(self):
        self.queue = []

    def control(self, message):
        self.queue.append(message)

    def actuate(self):
        self.queue = []
        logger = Logger() #TODO: don't make logger an obj
        logger.log("DOWNLINK", zlib.compress(bytes(self.queue)))
        return "Yay"