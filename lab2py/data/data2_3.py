import math


def f(x, y):
    return 4 * pow(math.e, x) + 3 * pow(math.e, y) - 12 * pow(x, 2)


def g(x, y):
    return y - 0.001 * pow(math.e, 2 * x) + 1 - 0.03 * pow(x, 2)


def dfx(x, y):
    return 4 * pow(math.e, x) - 24 * x


def dfy(x, y):
    return 3 * pow(math.e, y)


def dgx(x, y):
    return -0.002 * pow(math.e, 2 * x) - 0.06 * x


def dgy(x, y):
    return 1
