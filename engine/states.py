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

#
class Events(object):
    def __init__(self):
        self.burn_count = 0
        self.wood_count = 0
        self.stone_count = 0
        self.start_achieved = False
        self.wood_achieved  = False
        self.stone_achieved = False
        self.items_achieved = False

    def update_props(self, **kwargs):
        for key in kwargs:
            if key == "burn_count":
                self.burn_count = kwargs["burn_count"]
            elif key == "wood_count":
                self.wood_count = kwargs["wood_count"]
            elif key == "stone_count":
                self.stone_count = kwargs["stone_count"]


    def check_events(self):
        self.start_event()
        self.wood_event()
        self.stone_event()
        self.items_event()


    def start_event(self):
        if self.burn_count <= 0:
            self.start_achieved = True

    def wood_event(self):
        if self.burn_count >= 5:
            self.wood_achieved = True

    def stone_event(self):
        if self.wood_count >= 25:
            self.stone_achieved = True

    def items_event(self):
        if self.wood_count >= 50 and self.stone_count >= 10:
            self.items_achieved = True
