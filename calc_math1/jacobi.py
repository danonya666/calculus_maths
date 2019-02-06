import numpy


def sufficient_condition(a):
    a = numpy.array(a)
    flag = True
    for i in range(len(a)):
        ii = a[i][i]
        line_sum = 0
        for j in range(len(a[i])):
            if j != i:
                line_sum += a[i][j]
        if abs(ii) >= abs(line_sum):
            pass
        else:
            flag = False
            print('sufficient condition is not satisfied!')
            return flag
    print('sufficient condition is satisfied!')
    return flag


def vector_distance(v1, v2):
    dist = 0
    for i in range(len(v1)):
        dist += (v1[i] - v2[i]) ** 2
    dist = numpy.sqrt(dist)
    return dist


class JacobiException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def jacobi(A, b, N=25, x=None, epsilon=0.01):
    """Solves the equation Ax=b via the Jacobi iterative method.
    """
    # Create an initial guess if needed
    if not sufficient_condition(A):
        raise JacobiException('sufficient condition is not satisfied')
    if x is None:
        x = numpy.zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = numpy.diag(A)
    R = A - numpy.diagflat(D)

    # Iterate for N times
    old_x = (b - numpy.dot(R, x)) / D
    while vector_distance(old_x, x) > epsilon:
        old_x = x
        x = (b - numpy.dot(R, x)) / D
    print('Jacobi is done!')
    print('inaccuracy = {}'.format(vector_distance(old_x, x)))
    return x


""" 
  for i in range(N):
        x = (b - numpy.dot(R, x)) / D
        print(x)
"""
