from engine import cooldowns

def initalize():
    set_cooldown_times()


def set_cooldown_times():
    global cds
    cds = cooldowns.Cooldowns(5,10,15)

def get_cooldown_times():
    try:
        return cds
    except Exception as e:
        raise
