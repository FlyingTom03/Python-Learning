import random
import time
import sys


def menu():
        f = open("menutext.txt", "r")
        for c in f.read():
            sys.stdout.write(c)
            time.sleep(0.000001)
        user=input("\n               Enter Choice: ")
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.000001)
        print("\n")
    
        if user=="1":
            codebreaker()

        elif user=="2":
            dice()

        elif user=="3":
            one()

        elif user=="4":
            two()

        elif user=="5":
            three()

        else:
            menu()

            
def codebreaker():
    num=random.randint(1000,9999)

    print("><><><><><><><><><><")
    print("CodeBreaker( Digit)")
    print("><><><><><><><><><><")

    while True:
        a=int(input("\nGuess Number: "))
        if a < num:
            print("\nHigher")
    
        if a > num:
            print("\nLower")
    
        if a == num:
            print("\nCORRECT")
            print (" ")
            print (" ")
            menu()
    line = open ("line.txt", "r")
    for c in line.read():
        sys.stdout.write(c)
        time.sleep(0.0000001)
    True


def dice():
    num=random.randint(1,6)
    print (num)
    line = open ("line.txt", "r")
    for c in line.read():
        sys.stdout.write(c)
        time.sleep(0.0000001)
    print(" ")
    again = input("\nDo you want to roll another dice (y/n)? ")
    if again == "y":
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.0000001)
        print (" ")
        print (" ")
        dice()

    else:
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.0000001)
        print (" ")
        print (" ")
        print (" ")
        menu()


def one():
    num=random.randint(1,9)
    print (num)
    line = open ("line.txt", "r")
    for c in line.read():
        sys.stdout.write(c)
        time.sleep(0.0000001)
    print (" ")
    again = input("\nDo you want another 3 digit number (y/n)? ")
    if again == "y":
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.0000001)
        print (" ")
        print (" ")
        one()

    else:
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.0000001)
        print (" ")
        print (" ")
        print (" ")
        menu()


def two():
    num=random.randint(11,99)
    print (num)
    line = open ("line.txt", "r")
    for c in line.read():
        sys.stdout.write(c)
        time.sleep(0.0000001)
    print (" ")
    again = input("\nDo you want another 3 digit number (y/n)? ")
    if again == "y":
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.0000001)
        print (" ")
        print (" ")
        two()

    else:
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.0000001)
        print (" ")
        print (" ")
        print (" ")
        menu()

def three():
    num=random.randint(111,999)
    print (num)
    line = open ("line.txt", "r")
    for c in line.read():
        sys.stdout.write(c)
        time.sleep(0.0000001)
    print (" ")
    again = input("\nDo you want another 3 digit number (y/n)? ")
    if again == "y":
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.0000001)
        print (" ")
        print (" ")
        three()

    else:
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.0000001)
        print (" ")
        print (" ")
        print (" ")
        menu()

    
menu()
