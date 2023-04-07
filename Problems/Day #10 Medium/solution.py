import time

def say_hello():
    print("Hello!")

def scheduler(f:object, n:int):
    if n:
        time.sleep(n / 1000)
        f()
    return


scheduler(say_hello, 300)