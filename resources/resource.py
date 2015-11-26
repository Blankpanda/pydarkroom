class ResourceCounter(object):
    def __init__(self, item, starting_value):
        self.name = item
        self.accum = starting_value
        self.modifier = 1

    def get_resource_counter():
        return self.accum

    def accum_resource_counter(self, value):
        self.accum += (value * self.modifier)
