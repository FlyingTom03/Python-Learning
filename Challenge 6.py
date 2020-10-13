import time
import sys
import random

print("><><><><><><><><><><><")
print("> Elapsed Time Tester <")
print("><><><><><><><><><><><")

time.sleep(1)
print("you have to estimate when 10 seconds have passed.")
print("you will have to press the enter/return key to start and stop the timer.")
time.sleep(.2)
print("><><><><><><><><><><><><")
time.sleep(.2)
text = input("Press the return key to start timer?")
start=time.time()
text2 = input("Press the return key after you think 10 (+- 1s) seconds have elased")
end = time.time()
print("><><><><><><><><><><><><")

duration = round(end - start,2)
print("Elapsed Time: " + str(duration) + " seconds.")


if duration < 9:
    print ("You Failed")
    time.sleep(3)
    sys.exit

if duration > 11:
    print ("You Failed")
    time.sleep(3)
    sys.exit

else :
    print ("You Passed")
    s = 10 - end
    print ("you were " + s +" Seconds away fron 10 Seconds")
    time.sleep(3)
    sys.exit
