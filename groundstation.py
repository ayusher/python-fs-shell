import os, time, sys, json
from threading import Thread
from serial import Serial

gs_port = "/dev/pts/3"
ser = Serial(gs_port)

def listen():
	while True:
		time.sleep(.5)
		print("Flight: "+ser.readline().decode("utf-8"))
		print("\nλ: ", end = "")
def send():
	while True:
		time.sleep(.5)
		command = input("λ: ")
		ser.write(str.encode(json.dumps({"command":command})+"\n"))

t1 = Thread(target = listen)
t2 = Thread(target = send)
t2.start()
t1.start()
