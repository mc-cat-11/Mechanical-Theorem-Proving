import numpy

class Conic:
    def __init__(self, name, params):
        self.name = name
        self.params = numpy.array(params)