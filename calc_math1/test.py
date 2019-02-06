import gauss
import numpy
from jacobi import jacobi, sufficient_condition

a = numpy.array([[2.958, 0.147, 0.354, 0.238, 0.651],
                 [0.127, 2.395, 0.256, 0.273, 0.898],
                 [0.403, 0.184, 3.815, 0.416, 0.595],
                 [0.259, 0.361, 0.281, 3.736, 0.389]])
# a= numpy.array([[ 1. ,  0.6, -0.4,  0.4],
# [ 0.,   1.,  -1.5,  1.5],
# [ 0.,   0.,   1.,   1. ]])
print(a)
print("\n")

b = gauss.gaussFunc(a)
print("Gauss is done!")
print(b)


a = numpy.array([[2.958, 0.147, 0.354, 0.238],
                 [0.127, 2.395, 0.256, 0.273],
                 [0.403, 0.184, 3.815, 0.416],
                 [0.259, 0.361, 0.281, 3.736]])
b = numpy.array([0.651, 0.898, 0.595, 0.389])
print(jacobi(a, b))
