from item import item , blueprints
class Items(object):
    def __init__(self):
        self.hatchet = self.make_hatchet()
        self.pickaxe = self.make_pickaxe()


    def make_hatchet(self):
        blueprint = blueprints.Blueprint(wood = 5, stone = 1).recipe

        return item.Item.make_gather(blueprint, gather_increase = 2)


    def make_pickaxe(self):
        blueprint = blueprints.Blueprint(wood = 5, stone = 5).recipe

        return item.Item.make_modif(blueprint, modifier_change = 3)
