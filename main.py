import mods
import time
import os, pty, sys
from serial import Serial
import threading
#import smbus2 as smbus

ser_port = "/dev/pts/2"
imu_add = 0x54
debug = False

if sys.argv[1]=="--debug":
	debug = True

if __name__ == "__main__":
    submodules = {"radio": mods.radio(ser_port, debug), "imu": mods.imu(imu_add)}
    for i in submodules:
        print(i, " is active.")

    time.sleep(1)
    submodules["radio"].enqueue({"heartbeat":"AT"}, 0)

