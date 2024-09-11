from eq_classes.equation import Equation

MAX_ITER = 100


def check_si(eq: Equation, a, b, l):
    df = eq.df
    if (abs(1 + l * df(a)) < 1) and (abs(1 + l * df(b)) < 1):
        if (round(1 + l * df(a)) == 0) and (round(1 + l * df(b)) == 0):
            print("SI: Fast convergeance")
            return True
        print("SI: Slow convergeance")
        return True
    print("SI: Diverges!")
    return False


def perform_si(eq: Equation, x, l, eps):
    print("\nPerforming simple iteration method")
    f = eq.f
    done = False
    iteration = 0
    while (not done) and (iteration <= MAX_ITER):
        iteration += 1
        xi = x + l * f(x)
        if abs(xi - x) <= eps:
            done = True
        else:
            x = xi

    print("Number of iterations: " + str(iteration))
    print("Solution: " + str(xi))
    print()
