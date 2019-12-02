import mods
import time
import os, pty, sys
from serial import Serial
import threading
#import smbus2 as smbus

ser_port = "/dev/pts/2"
imu_add = 0x54
debug = False
execute_time = 10
batch_size = 5

if sys.argv[1]=="--debug":
	debug = True

if __name__ == "__main__":
    submodules = {"radio": mods.radio(ser_port, debug), "imu": mods.imu(imu_add)}
    for i in submodules:
        print(i, " is active.")

    time.sleep(1)
    submodules["radio"].enqueue({"timestamp": time.time(), "heartbeat":"AT AWAKE"}, 0)
    
    while True:
        time.sleep(execute_time)
        submodules["radio"].enqueue({"timestamp": time.time(), "heartbeat":"AT ALIVE"}, 0)
        submodules["radio"].process(batch_size)
