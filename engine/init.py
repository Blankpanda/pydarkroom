from engine import cooldowns , modifiers, states, fire
from resources import resources


def initalize():
    set_cooldown_times()
    set_starting_resource_values()
    set_base_modifiers()
    set_fire_intensity_states()


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
    fstate = {}
    maximum = fire.Fire().INTENSITY_MAXIMUM
    for i in range(0, maximum):
        if i == 0:
            fstate[i] = "The fire is unlit"
        elif i > 0 and i <= 20:
            fstate[i] = "The fire is smoldering"
        elif i > 20 and i <= 60:
            fstate[i] = "The fire is burning"
        elif i > 60 and i <= 90:
            fstate[i] = "The fire is roaring"
        elif i > 90 and i <= 100:
            fstate[i] = "The fire is blazing"

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
