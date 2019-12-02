import os, pty, threading, os, time
from serial import Serial
from fake_rpi import smbus
from threading import Thread
import heapq
import json
import processor

class radio():
    def __init__(self, ser_port, debug):
        self.ser = Serial(ser_port)
        #self.ser.write(b"AT\n")
        self.send_queue = []
        self.listen_queue = []
        self.lock = threading.Lock()
        self.debug = debug
        self.thread_stop = False
        #self.ser.write(b"AT")
        #print(os.read(master, 1000))
        self.start_threads()

    def enqueue(self, raw_data, priority):
        with self.lock:
            heapq.heappush(self.send_queue, (priority, json.dumps(raw_data)))
        return True

    def send(self):
        while True:
            if self.thread_stop:
                return
            if len(self.send_queue)>0:
                with self.lock:
                    self.ser.write(str.encode(heapq.heappop(self.send_queue)[1]+"\n"))
                    time.sleep(.5)

    def listen(self):
        while True:
            if self.thread_stop:
                return
            p = self.ser.readline().decode("utf-8")
            if self.debug:
                print(p, end = "")
            heapq.heappush(self.listen_queue, p)

    def process(self, batch_size):
        for i in range(min(batch_size, len(self.listen_queue))):
            self.enqueue({"timestamp": time.time(), "response": processor.run(heapq.heappop(self.listen_queue))}, 1)

    def restart_threads(self):
        self.thread_stop = True

        self.list_thread.join()
        self.send_thread.join()

        self.thread_stop = False

        self.start_threads()
        
        
    def start_threads(self):
        self.list_thread = Thread(target = self.listen)
        self.list_thread.daemon = True
        self.send_thread = Thread(target = self.send)
        self.send_thread.daemon = True
        self.list_thread.start()
        self.send_thread.start()


class imu(): #MPU6050
    def __init__(self, add):
        self.address = add
        self.bus = smbus.SMBus(1)
        self.accelx = 0x3B
        self.accely = 0x3D
        self.accelz = 0x3F

        self.temp = 0x41

        self.gyrox = 0x43
        self.gyroy = 0x45
        self.gyroz = 0x47

        self.gyro_conf = 0x1B
        self.accel_conf = 0x1C


        self.pwr = 0x6B

        self.bus.write_byte_data(self.address, self.pwr, 0x00)
        self.bus.write_byte_data(self.address, self.accel_conf, 0x00)
        self.bus.write_byte_data(self.address, self.gyro_conf, 0x00)


    def read_i2c_word(self, register):
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        value = (high << 8) + low

        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

    
    def get_accel_data(self):
        x = self.read_i2c_word(self.accelx)
        y = self.read_i2c_word(self.accely)
        z = self.read_i2c_word(self.accelz)

        return [x/2, y/2, z/2]


    def get_gyro_data(self):
        x = self.read_i2c_word(self.gyrox)
        y = self.read_i2c_word(self.gyroy)
        z = self.read_i2c_word(self.gyroz)

        return [x/131.0, y/131.0, z/131.0]


    def get_temp_data():
        raw_temp = self.read_i2c_word(self.temp)
        actual_temp = (raw_temp / 340.0) + 36.53

        return actual_temp


    def listen(self):
        return self.ser.read()
