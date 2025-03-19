import numpy

class Point:
    def __init__(self, name, homog):
        self.name = name
        self.homog = numpy.array(homog)
        self.x = self.homog[0]/self.homog[2]
        self.y = self.homog[1]/self.homog[2]