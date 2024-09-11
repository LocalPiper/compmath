from math import *


def f(x):
    return pow(x, 3) - x + 4


def df(x):
    return 3 * pow(x, 2) - 1


def d2f(x):
    return 6 * x
