from cmath import sin


def signs_vary(a, b):
    """Also return true if one of the variables is 0"""
    return a * b <= 0


def localize_root(start, end, variables_gap=1, epsilon_interval=0.01):
    # print('start = {}, end = {}'.format(start, end))
    x = start
    while x <= end:
        x1 = x + variables_gap
        a = 2 - 0.5 * x ** 2 - 0.5 * x ** -1 * sin(x) - x
        b = 2 - 0.5 * x1 ** 2 - 0.5 * x1 ** -1 * sin(x1) - x1
        if signs_vary(a.real, b.real):
            # print('root is between {} and {}'.format(x, x1))
            # print(end - start - epsilon_interval)
            if x1 - x < epsilon_interval:
                print('root is between {} and {}'.format(x, x1))
                return [x, x1]
            res = localize_root(x, x1 - ((x1 - x) / 2), 0.25 * (end - start))
            try:
                if int(res[1]) - int(res[0]) < epsilon_interval:
                    return res
            except:
                print('root is between {} and {}'.format(start, end))
                return [start, end]
            # localize_root(x1 - ((x1 - x) / 2, x1))
        x += epsilon_interval


localize_root(-10, 10, 1, 0.01)
