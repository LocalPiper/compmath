from math import *


def f(x):
    return pow(x, 3) + 4.81 * pow(x, 2) - 17.37 * x + 5.38


def df(x):
    return 3 * pow(x, 2) + 9.62 * x - 17.37


def d2f(x):
    return 6 * x + 9.62
