# acts a structure for a item.

class Item(object):
    # todo: modifer change or gather increase

    @classmethod
    def make_gather(cls, blueprint, gather_increase):
        obj = cls()
        obj.requirements = blueprint
        obj.gather_increase = gather_increase
        obj.item_counter = 0
        return obj

    @classmethod
    def make_modif(cls, blueprint, modifier_change):
        obj = cls()
        obj.requirements = blueprint
        obj.modifier_change = modifier_change
        obj.item_counter = 0
        return obj

    def create(self):
        item_counter += 1


    def get_number_of(self):
        return item_counter

    def get_property(self):
        try:
            return self.gather_increase
        except Exception as e:
            return self.modifier_change
