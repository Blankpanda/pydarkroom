import init
import cooldown

def start():

     # cooldown booleans
    fire_off_cooldown = True
    wood_off_cooldown = True

    cds = init.get_cooldown_times() # an oject containing cooldown timers

    fire_cooldown_timer = cooldown.CooldownTimer(cds.fire_cooldown)
    wood_cooldown_timer = cooldown.CooldownTimer(cds.wood_cooldown)


    while True:
        uin = input("enter n: ")

        if uin == "1" and fire_off_cooldown:
            fire_cooldown_timer.start()
            fire_off_cooldown = False

        if fire_cooldown_timer.check():
            fire_off_cooldown = True
            print("off cooldown.")
        else:
            print("on cooldown.")

        #
        # if uin == "2" and wood_off_cooldown:
        #     wood_cooldown_timer.start()
        #     wood_off_cooldown = False
        #
        # if wood_cooldown_timer.check():
        #     wood_off_cooldown = True
        #     print("off cooldown.")
        # else:
        #     print("on cooldown.")
