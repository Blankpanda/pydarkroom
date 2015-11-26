class ResourceCounter(object):
    def __init__(self, item, starting_value):
        self.name = item
        self.accum = starting_value
        self.modifier = 1

    def get_resource_counter(self):
        return self.accum

    def accum_resource_counter(self, value):
        self.accum += (value * self.modifier)

    def subtract_resource_counter(self, value):
        self.accum -= value
