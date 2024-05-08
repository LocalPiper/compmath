import eq_class.equation
from logic.verifier import runge_rule
from sympy import integrate, Symbol

MAX_DIV = 1000


def perform_trapezoid(eq: eq_class.equation.Equation, a, b, eps):
    print("\nPerforming trapezoid: ")
    try:
        f = eq.f
        n = 2
        I = eq.I
        I_true = I(b) - I(a)
        while n < MAX_DIV:
            n += 2
            h = (b - a) / n
            x = [a + h * i for i in range(n)]
            x.append(b)

            sum1 = (
                h
                / 2
                * (f(x[0]) + f(x[-1]) + 2 * sum([f(x[i]) for i in range(1, n - 1)]))
            )
            if abs(sum1 - I_true) <= eps:
                break

        print("\nDivided by: " + str(n))
        print("Solution I: " + str(sum1))
    except Exception:
        print("Gap")
