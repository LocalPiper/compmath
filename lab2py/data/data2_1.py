def f(x, y):
    return pow(x, 3) + pow(y, 2) - 10


def g(x, y):
    return 2 * x + y - 1


def dfx(x, y):
    return 3 * pow(x, 2)


def dfy(x, y):
    return 2 * y


def dgx(x, y):
    return 2


def dgy(x, y):
    return 1
