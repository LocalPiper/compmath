from eq_classes.equation import Equation
import numpy as np


def analyze_root_existence(eq: Equation, a, b):
    arr = np.linspace(a, b)
    f = eq.f
    if (f(a) * f(b)) < 0:
        print("ANALYZE: At least 1 root exists on this interval")
        sign = None
        df = eq.df
        roots = 0
        for val in arr:
            if sign == None:
                sign = np.sign(df(val))
            else:
                if np.sign(df(val)) != sign:
                    roots += 1
                    sign = np.sign(df(val))

        if roots == 1:
            print("ANALYZE: This interval has exactly 1 root")
            return True
        else:
            if roots == 0:
                print(
                    "ANALYZE: This interval has more than 1 root... wait, something's not right..."
                )
                return False
            else:
                print("ANALYZE: This interval has more than 1 root")
                return False
    else:
        # dumbass math, there may be roots but the quote-on-quote necessary condition does not see them
        sign = None
        df = eq.df
        roots = 0
        for val in arr:
            if sign == None:
                sign = np.sign(df(val))
            else:
                if np.sign(df(val)) != sign:
                    roots += 1
                    sign = np.sign(df(val))
        if roots == 0:
            print("ANALYZE: This interval has no roots")
            return False
        else:
            print("ANALYZE: This interval has more than 1 root")
            return False
