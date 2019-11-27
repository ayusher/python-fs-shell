import time, json, subprocess
from datetime import datetime

def clock():
    return datetime.utcnow().isoformat()

def uptime():
    return subprocess.check_output(['cat', '/proc/uptime']).decode('utf-8').split()[0]

def sudo_shell():
    return "Add later"

commands = [clock]

def run(packet):
    packet = json.loads(packet)
    try:
        print(globals()[packet["command"]]())
        return globals()[packet["command"]]()
    except Exception as e:
        print(e)
