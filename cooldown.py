import time

def start(cooldown):
    global start
    global cd

    start = time.time()
    cd = cooldown


def check():
    if time.time() >= (start + cd):
        print(time.time())
        return True
    else:
        return False
