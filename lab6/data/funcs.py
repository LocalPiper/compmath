from numpy import *
import math

def f1(x, y):
    return y + (1 + x) * pow(y, 2)

def f1_s(x, c):
    return - (pow(e, x)) / (c + pow(e, x) * x)

def f1_c(x, y):
    try:
        return -pow(e, x) / y - pow(e, x) * x
    except ZeroDivisionError:
        print("Zero division detected. You are cringe.")
        y = pow(10, -18)
        return -pow(e, x) / y - pow(e, x) * x

def f2(x, y):
    try:
        return -y / (x + y)
    except ZeroDivisionError:
        print("Zero division detected. You are cringe.")
        x = pow(10, -18)
        return -y / (x + y)

def f2_s(x, c):
    return -math.sqrt(c + pow(x,2)) - x

def f2_c(x, y):
    return pow(y, 2) + 2*x*y

def f3(x, y):
    return x + y

def f3_s(x, c):
    return c * pow(e, x) - x - 1

def f3_c(x, y):
    return (y + x + 1) / pow(e, x)