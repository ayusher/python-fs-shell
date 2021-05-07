from pyorbital.orbital import Orbital
from datetime import datetime
class GPS:
    def read_lon(self):
        snpp = Orbital('ISS', tle_file='mods/iss_tle.txt')
        now = datetime.utcnow()
        return snpp.get_lonlatalt(now)[0]

    def read_lat(self):
        snpp = Orbital('ISS', tle_file='mods/iss_tle.txt')
        now = datetime.utcnow()
        return snpp.get_lonlatalt(now)[1]

    def read_alt(self):
        snpp = Orbital('ISS', tle_file='mods/iss_tle.txt')
        now = datetime.utcnow()
        return snpp.get_lonlatalt(now)[2]
