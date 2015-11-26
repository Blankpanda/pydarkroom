from resources import resources

class BaseModifiers(object):
    def __init__(self,wood_gathered, stone_gathered):
        self.wood_gathered = wood_gathered
        self.stone_gathered = stone_gathered



def change_modifier(resource, value):
    # not quite sure how I could impliment this
    # other than the way it is.
    resource.modifier = value
    return resource
