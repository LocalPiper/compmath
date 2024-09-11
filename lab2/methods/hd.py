from eq_classes.equation import Equation
from math import *

MAX_ITER = 100


def check_hd(eps, a, b):
    print("\nHD: Checking halving division...")
    if ceil(log2(abs(a - b) / eps)) > MAX_ITER:
        print("HD: Equation will not be solved - bounds are too far away")
        return False
    else:
        print("HD: Good to go")
        return True


def perform_hd(eq: Equation, eps, a, b):
    print("\nPerforming halving division: ")
    f = eq.f
    iteration = 0
    while abs(a - b) > eps:
        iteration += 1
        x = (a + b) / 2
        if (f(x) * f(a)) > 0:
            a = x
        else:
            b = x

    print("Number of iterations: " + str(iteration))
    print("Solution: " + str(x))
    print()
