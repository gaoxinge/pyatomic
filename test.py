import threading
from pyatomic import *


#########################################################
balance = 0

def run_thread(n):
    global balance
    for _ in range(n):
        balance += 1

t1 = threading.Thread(target=run_thread, args=(100000,))
t2 = threading.Thread(target=run_thread, args=(100000,))
t3 = threading.Thread(target=run_thread, args=(100000,))
t4 = threading.Thread(target=run_thread, args=(100000,))
t5 = threading.Thread(target=run_thread, args=(100000,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print(balance)


#########################################################
balance = 0

def run_thread(n):
    global balance
    for _ in range(n):
        f1(balance)

t1 = threading.Thread(target=run_thread, args=(100000,))
t2 = threading.Thread(target=run_thread, args=(100000,))
t3 = threading.Thread(target=run_thread, args=(100000,))
t4 = threading.Thread(target=run_thread, args=(100000,))
t5 = threading.Thread(target=run_thread, args=(100000,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print(balance)


#########################################################
balance = 0

def run_thread(n):
    global balance
    for _ in range(n):
        f2(balance)

t1 = threading.Thread(target=run_thread, args=(100000,))
t2 = threading.Thread(target=run_thread, args=(100000,))
t3 = threading.Thread(target=run_thread, args=(100000,))
t4 = threading.Thread(target=run_thread, args=(100000,))
t5 = threading.Thread(target=run_thread, args=(100000,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print(balance)