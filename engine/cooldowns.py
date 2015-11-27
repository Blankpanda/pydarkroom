# structure that holds initalized cooldown times.
class Cooldowns(object):
    def __init__(self, fire_cooldown, wood_cooldown, stone_cooldown):
        self.fire_cooldown = fire_cooldown
        self.wood_cooldown = wood_cooldown
        self.stone_cooldown = stone_cooldown
