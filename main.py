import mods
import time
import os, pty
from serial import Serial
import threading
#import smbus

master, slave = pty.openpty()
s_name = os.ttyname(slave)
imu_add = 0x54

if __name__ == "__main__":
    submodules = {"radio": mods.radio(s_name, master), "imu": mods.imu(imu_add)}
    for i in submodules:
        print(i, " is active.")

