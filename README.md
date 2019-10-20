# ideal-python-fs
An ideal template for python flight software

## Dependencies
 * python 3.x
 * python (pip) dependencies found in Pipfile: `pipenv install`
 * socat: `sudo apt install socat`

## How to run
 * create virtual serial port for radio, run flight software, spawn groundstation terminal: `./create.sh`
      * ser_port and gs_port in main.py and groundstation.py may need to be changed based on ports made by socat
      * command to spawn new shell in create.sh may need to be changed to fit user's OS
           * code in repo designed for WSL
           
