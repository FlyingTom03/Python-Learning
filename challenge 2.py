import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

name = input ("what is your name?: ")
time.sleep(1)
delay_print ("Hello, " + name)
time.sleep(3)
sys.exit
