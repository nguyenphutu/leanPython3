import time
from threading import Thread

def timer(name):
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Hi " + name + "This program has now been running for " + str(count) + " minutes.")

print("Hello! Welcome to the program timer!")
name = input("What is your name?")
print("Nice to meet you, " + name + "!")
background_thread = Thread(target=timer, args=(name,))
background_thread.start()
background_thread.join()