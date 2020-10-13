import time

def appendToList(n):
    alist = []
    t0 = time.clock()
    for i in range(n):
        alist = alist + [i]
    t1 =time.clock()
    runtime == round((t1-t0)* 1000,2)
    print ("time to append",n, " items to list ",runtime, "milliseconds")

def concatenateList(n):
    alist = []
    t0 = time.clock()
    for i in range(n):
        alist = alist + [i]
    t1 = time.clock()
    runtime = round((t1 - t0)* 1000,2)
    print ("Time to concantenate ",n, "items to list ",runtime, "milliseconds")

k = int(input ("how many items do you want to add to your list? "))
appendToList(k)
concantenateList(k)
quit = input()
