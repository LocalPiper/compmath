def f(x, y):
    return pow(x, 2) + pow(y, 2) - 4


def g(x, y):
    return y - 3 * pow(x, 2)


def dfx(x, y):
    return 2 * x


def dfy(x, y):
    return 2 * y


def dgx(x, y):
    return -6 * x


def dgy(x, y):
    return 1
