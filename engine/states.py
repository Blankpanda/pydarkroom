# build and initalze different game states.
from engine import fire


# creates a dictionary with descriptions based on intensity
class FireIntensityStates(object):
    def __init__(self):
        self.fire_states = {}
        self.maximum = fire.Fire().INTENSITY_MAXIMUM
        for i in range(0, self.maximum):
            if i == 0:
                self.fire_states[i] = "The fire is unlit"
            elif i > 0 and i <= 20:
                self.fire_states[i] = "The fire is smoldering"
            elif i > 20 and i <= 60:
                self.fire_states[i] = "The fire is burning"
            elif i > 60 and i <= 90:
                self.fire_states[i] = "The fire is roaring"
            elif i > 90 and i < 101:
                self.fire_states[i] = "The fire is blazing"


    def get_fire_states(self):
        return self.fire_states

    def get_fire_state(self,intensity):
        return self.fire_states[intensity]
