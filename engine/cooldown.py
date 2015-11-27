# starts a countdown timer for a specified ammount of time.
import time

class CooldownTimer(object):

    def __init__(self, time):
        self.cooldown_time = time
        self.start_time = 0

    # we dont want start this in the constructor because the object
    # may be declared at a different time.
    # this also allows us to re-use the object with the same value. yay.    
    def start(self):
        self.start_time = time.time()

    def check(self):
        if time.time() >= (self.start_time + self.cooldown_time):
            return True
        else:
            return False
