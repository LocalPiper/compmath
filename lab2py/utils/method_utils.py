from eq_classes.equation import Equation
import numpy as np


def calcultate_starting_approximation(eq: Equation, a, b):
    print("SECANT: Calculating starting approximation...")
    f = eq.f
    d2f = eq.d2f
    if (f(a) * d2f(a)) > 0:
        return True, a
    elif (f(b) * d2f(b)) > 0:
        return True, b
    print("SECANT: Slow convergeance")
    return False, None


def calculate_lambda(eq: Equation, a, b):
    arr = np.linspace(a, b)
    df = eq.df
    calc_arr = []
    for val in arr:
        calc_arr.append(df(val))
    m = -np.inf
    s = 0
    for val in calc_arr:
        if abs(val) > m:
            m = val
            s = np.sign(m)
    if s == 1:
        return -1 / abs(m)
    else:
        return 1 / abs(m)
