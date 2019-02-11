import numpy
import copy


def gauss_solve(a: numpy.array) -> numpy.array:
    eps = 1e-16
    a = numpy.array(a)
    height = len(a[:, 0])
    width = len(a[0, :])

    for g in range(height):

        biggest = abs(a[g][g])
        my = g
        t1 = g
        while t1 < height:
            if abs(a[t1][g]) > biggest:
                biggest = abs(a[t1][g])
                my = t1
            t1 += 1

        if abs(biggest) < eps:
            raise determinantException("Check determinant")

        if my != g:
            b = copy.deepcopy(a[g])
            a[g] = copy.deepcopy(a[my])
            a[my] = copy.deepcopy(b)

        main_value = float(a[g][g])
        z = g

        while z < width:
            a[g][z] = a[g][z] / main_value
            z += 1
        j = g + 1

        while j < height:
            b = a[j][g]
            z = g

            while z < width:
                a[j][z] = a[j][z] - a[g][z] * b
                z += 1
            j += 1
    a = backtrace(a, height, width)
    return a


class determinantException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def backtrace(a, len1, len2):
    a = numpy.array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1

        while j >= 0:
            a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
            j -= 1
        i -= 1
    return a[:, len2 - 1]

