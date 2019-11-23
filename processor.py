import time, json

def clock():
    return time.gmtime()

def sudo_shell():
    return "Add later"

commands = [clock]

def run(packet):
    packet = json.loads(packet)
    try:
        print(globals()[packet["command"]]())
    except Exception as e:
        print(e)
