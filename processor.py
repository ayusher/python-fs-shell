import time, json, subprocess
from datetime import datetime

def clock():
    return datetime.utcnow().isoformat()

def uptime():
    return subprocess.check_output(['cat', '/proc/uptime']).decode('utf-8').split()[0]

def add(a, b):
    return a+b

def sudo_shell():
    return "shell"

def run(packet):
    packet = json.loads(packet)
    try:
        return(globals()[packet["command"].split()[0]](*parse_args(packet["command"].split()[1:])))
        #return globals()[packet["command"].split()[0]]()
    except Exception as e:
        print(e)
        return "Invalid command"

def parse_args(args):
    known_types = {"int": int, "float": float, "str": str}
    return [known_types[i[:i.index(":")]](i[i.index(":")+1:]) for i in args]
