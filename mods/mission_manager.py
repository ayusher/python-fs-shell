from modes.modes import Mode

class Mission_Manager:
    def __init__(self):
        self.mode = Mode.safe
        self.time_holder = 0

    def control(self, sfr, acts):
        constants = {"GS_LON":-77.306374, "GS_LAT": 38.846226}
        # Mode switching logic
        if self.mode==Mode.standby:
            pass

        if self.mode==Mode.safe:
            pass # diagnose problem

        if self.mode==Mode.normal:
            if (sfr["GPS_LON"]-constants["GS_LON"])**2+(sfr["GPS_LAT"]-constants["GS_LAT"])**2<900:
                self.mode=Mode.dump

        if self.mode==Mode.dump:
            if (sfr["GPS_LON"]-constants["GS_LON"])**2+(sfr["GPS_LAT"]-constants["GS_LAT"])**2>900:
                self.mode=Mode.normal
        
        outlist = []
        acts["Downlink_Producer"].control(str(sfr))

        if int(sfr["TIME_START"])//5>self.time_holder: #Every 5 secs
            outlist.append(acts["Downlink_Producer"].actuate)
            self.time_holder = int(sfr["TIME_START"])//5
        
        return outlist
        