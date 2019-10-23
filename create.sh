#!/bin/bash
(socat -d -d pty,raw,echo=0 pty,raw,echo=0 &)

vari="$(pwd)"
cmd.exe /c start bash.exe -c "python3 $vari/groundstation.py"
python3 main.py --debug
