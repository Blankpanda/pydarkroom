# used to initalize base modifiers for resources
from resources import resources
# I dont think I actually need this ?
class BaseModifiers(object):
    def __init__(self,wood_gathered, stone_gathered):
        self.wood_gathered = wood_gathered
        self.stone_gathered = stone_gathered

# outside of the class

# accepts an object and changes its modifer property.
# the object would have to be a resource.
def change_modifier(resource, value):
    # not quite sure how I could impliment this
    # other than the way it is.
    resource.modifier = value
    return resource
