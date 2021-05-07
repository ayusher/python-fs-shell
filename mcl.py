import ast, time

from mods.radio_1 import Radio_1
from mods.dummy_gps import GPS
from mods.downlink_producer import Downlink_Producer

from mods.mission_manager import Mission_Manager

from logger import Logger

class MCL:

    def __init__(self, config):
        self.state_field_registry = {}
        self.reads = config["read"]
        self.read_objects = dict([(key, globals()[key]()) for key in self.reads])

        self.actuates = config["actuate"]
        self.actuate_objects = dict([(key, globals()[key]()) for key in self.actuates])

        self.mm = Mission_Manager()

    def execute(self):
        logger = Logger()
        start_loop = time.time()
        while True:
            self.state_field_registry["TIME_START"] = time.time()-start_loop
            #READ
            for device in self.reads:
                for var in self.reads[device]:
                    self.state_field_registry[device+"_"+var] = getattr(self.read_objects[device], self.reads[device][var])()
            logger.log('STATUS', "READ COMPLETE")
            logger.log('INFO', str(self.state_field_registry))

            #CONTROL
            actuate_list = self.mm.control(self.state_field_registry, self.actuate_objects)
            logger.log('INFO', str(self.mm.mode))

            #ACTUATE
            for func in actuate_list:
                func()

            time.sleep(1)
