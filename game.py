import init
import cooldown

def start():

    fire_off_cooldown = True

    while True:
        uin = input("enter 1: ")

        if uin == "1" and fire_off_cooldown:
            cooldown.start(cds.fire_cooldown)
            fire_off_cooldown = False
            if cooldown.check():
                fire_cooldown
            else:
                print("1 is on cooldown")
