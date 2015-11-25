import time

class CooldownTimer(object):

    def __init__(self, time):
        self.cooldown_time = time
        self.start_time = 0

    def start(self):
        self.start_time = time.time()

    def check(self):
        if time.time() >= (self.start_time + self.cooldown_time):
            print(time.time())
            return True
        else:
            return False
