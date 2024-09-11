import math


def f(x):
    return math.sin(x) + pow(math.e, x)


def df(x):
    return math.cos(x) + pow(math.e, x)


def d2f(x):
    return -math.sin(x) + pow(math.e, x)
