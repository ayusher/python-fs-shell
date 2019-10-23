import os, time
from threading import Thread
from serial import Serial

gs_port = "/dev/pts/3"
ser = Serial(gs_port)

def listen():
	while True:
		print("Flight: "+ser.readline().decode("utf-8"))
		print("\nλ: ", end = "")
def send():
	while True:
		ser.write(str.encode(input("λ: ")+"\n"))


t1 = Thread(target = listen)
t2 = Thread(target = send)
t2.start()
t1.start()
