# main game loop.
# currently used as a testing ground for game mechanics


from engine import init, cooldown, modifiers, fire, states
from resources import resource
import threading
from multiprocessing.pool import ThreadPool

def build():
    game_thread = threading.Thread(target = start)
    game_thread.start()

def start():

    cds = init.get_cooldown_times() # an oject containing cooldown timers
    res = init.get_starting_resource_values() # an object containing
                                              # resource staring values
     # cooldown booleans
    fire_off_cooldown = True
    wood_off_cooldown = True

    # cooldown timers
    fire_cooldown_timer = cooldown.CooldownTimer(cds.fire_cooldown)
    wood_cooldown_timer = cooldown.CooldownTimer(cds.wood_cooldown)

    # resource counters
    wood_resource_counter = resource.ResourceCounter("wood",res.wood)
    stone_resource_counter = resource.ResourceCounter("stone", res.stone)

    #flame objects
    flame = fire.Fire()

    pool = ThreadPool(processes = 1) # holds the values of user input
                                     # since user input is handled
                                     # on a different thread.
    # GameStates
    GameStates = states.Events()

    while True:

        burn_count = flame.get_current_kindle_count()
        wood_count = wood_resource_counter.get_resource_counter()
        stone_count = stone_resource_counter.get_resource_counter()

        GameStates.update_props( burn_count = burn_count,
        wood_count = wood_count,
        stone_count = stone_count)
        GameStates.check_events()



        if flame.get_current_kindle_count() == 0:
            print("Light the fire.")

        uin = get_user_input()

        if uin == "1" and fire_off_cooldown:
            fire_cooldown_timer.start()
            fire_off_cooldown = False
            flame_is_burning = True
            flame.kindle(20)
            print(flame.get_intensity_state(flame.get_current_intensity()))

        if flame.check_burn_time():
            flame.start_burn()
            flame.burn()

        if fire_cooldown_timer.check() and fire_off_cooldown == False:
            fire_off_cooldown = True
            print("kindle off cooldown")




def get_user_input():
    uin = input("enter n:")
    return uin
