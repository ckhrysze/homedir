#!/usr/bin/env python
import subprocess
import sys

#cmd = ['/run/myscript', '--arg', 'value']

try:
    p = subprocess.Popen("top", stdout=subprocess.PIPE)
    for line in p.stdout:
        print line
    p.wait()
except KeyboardInterrupt:
    print p.returncode
sys.exit(0)
