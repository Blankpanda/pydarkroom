import time
from engine import init
class Fire(object):
    def __init__(self):
        self.kindle_count = 0
        self.intensity = 0
        self.INTENSITY_MAXIMUM = 101

    def kindle(self , value):
        self.intensity += value

        if self.intensity >= self.INTENSITY_MAXIMUM:
            self.intensity = 100
        self.kindle_count += 1

    def get_current_intensity(self):
        return self.intensity

    def get_intensity_state(self,intenisty):
        intensity_states = init.get_fire_intensity_states()
        return intensity_states[intenisty]
