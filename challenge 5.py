import time
import sys

name = input('name: ')
print ("now enter your age")
age = input("age: " )
age = int(age)

days = age * 365
minutes = age * 525600
seconds = age * 31536000


print (name + ", you have been alive for")
print ("-------")
print (days)
print ("Days")
time.sleep(0.2)
print ("-------")
print (minutes)
print ("Minutes")
time.sleep(0.2)
print ("-------")
print (seconds)
print ("Seconds")
time.sleep(0.2)
print ("-------")

time.sleep(5)
sys.exit
