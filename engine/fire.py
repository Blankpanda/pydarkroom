# fire class that we use to track the fires intensity, change intensity
# retrieve kindle count and get states based on intensity using states.py
import time
from engine import init
class Fire(object):
    def __init__(self):
        self.kindle_count = 0
        self.intensity = 0
        self.INTENSITY_MAXIMUM = 101 # because the dictionary that holds
                                     # fire states needs to have 100 values.
        self.burn_rate = 5
        self.start_time = 0

    def kindle(self , value):
        self.intensity += value

        # we dont want the intensity going over 101 because
        # it would go over the intensity_state dictionary
        # and the fire cannot be more intense then the value 101.
        # it is set to 100 because tha is the final value
        # in dictionary.
        if self.intensity >= self.INTENSITY_MAXIMUM:
            self.intensity = 100

        self.kindle_count += 1

    def start_burn(self):
        if self.kindle_count > 0:
            self.start_time = time.time()

    def check_burn_time(self):
        if time.time() >= (self.start_time + self.burn_rate):
            print("T")
            return True
        else:
            print("F")
            return False

    def burn(self):
        self.intensity -= 15

    # gets a numeric value thats holds the fires current intesnity.
    def get_current_intensity(self):
        return self.intensity

    # gets a string value from intensity_states based on the current intensity
    def get_intensity_state(self,intensity):
        intensity_states = init.get_fire_intensity_states()
        return intensity_states[intensity]
