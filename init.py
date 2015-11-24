import cooldowns

def initalize():
    set_cooldown_times()


def set_cooldown_times():
    global cds
    cds = cooldowns.Cooldowns(5,10,15)
