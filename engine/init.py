# everything that needs to be done before the game starts.
# we also use it get these starting values for the game.
from engine import cooldowns , modifiers, states, fire
from item import items
from resources import resources


def initalize():
    set_cooldown_times()
    set_starting_resource_values()
    set_base_modifiers()
    set_fire_intensity_states()
    set_items()


def set_cooldown_times():
    global cds
    cds = cooldowns.Cooldowns(5,10,15)

def set_starting_resource_values():
    global res
    res = resources.Resources(5,0)


def set_base_modifiers():
    global mods
    mods = modifiers.BaseModifiers(1,1)

def set_fire_intensity_states():
    global fstate
    fstate = states.FireIntensityStates().get_fire_states()

def set_items():
    global items
    items = items.Items()



def get_fire_intensity_states():
    try:
        return fstate
    except Exception as e:
        set_fire_intensity_states()


def get_base_modifiers():
    try:
        return mods
    except Exception as e:
        set_base_modifiers()

def get_starting_resource_values():
    try:
        return res
    except Exception as e:
        set_starting_resource_values()

def get_cooldown_times():
    try:
        return cds
    except Exception as e:
        set_cooldown_times()

def get_items():
    try:
        return items
    except Exception as e:
        raise
