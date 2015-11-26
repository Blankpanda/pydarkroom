from engine import cooldowns , modifiers
from resources import resources


def initalize():
    set_cooldown_times()
    set_starting_resource_values()
    set_base_modifiers()


def set_cooldown_times():
    global cds
    cds = cooldowns.Cooldowns(5,10,15)

def set_starting_resource_values():
    global res
    res = resources.Resources(5,0)


def set_base_modifiers():
    global mods
    mods = modifiers.BaseModifiers(1,1)



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
