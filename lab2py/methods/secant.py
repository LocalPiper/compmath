from eq_classes.equation import Equation

MAX_ITER = 100


def perform_secant(eq: Equation, x, xi, eps):
    print("\nPerforming secant method")
    f = eq.f
    iteration = 0
    while (abs(xi - x) > eps) and (iteration <= MAX_ITER):
        iteration += 1
        buf = xi
        xi = xi - (xi - x) / (f(xi) - f(x)) * f(xi)
        x = buf

    print("Number of iterations: " + str(iteration))
    print("Solution: " + str(xi))
    print()
