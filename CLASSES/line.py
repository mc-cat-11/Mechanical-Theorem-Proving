import numpy

class Line:
    def __init__(self, name, homog):
        self.name = name
        self.homog = numpy.array(homog)