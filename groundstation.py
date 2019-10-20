import os, time
from serial import Serial

gs_port = "/dev/pts/3"
ser = Serial(gs_port)

while True:
	try:
		print("Flight: "+ser.readline().decode("utf-8"))
	except Exception as e:
		print(e)
