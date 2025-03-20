import numpy

def det(a,b,c):
    matrix = numpy.array([a/a[2],b/b[2],c/c[2]])
    return numpy.linalg.det(matrix)