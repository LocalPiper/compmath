import eq_class.equation
from logic.verifier import runge_rule
from sympy import integrate, Symbol

MAX_DIV = 1000


def perform_simpson(eq: eq_class.equation.Equation, a, b, eps):
    print("\nSimping...")
    try:
        f = eq.f
        n = 4
        I = eq.I
        I_true = I(b) - I(a)
        while n < MAX_DIV:
            h = (b - a) / n
            x = [a + h * i for i in range(n)]
            x.append(b)

            y = [f(x[i]) for i in range(n)]

            sum1 = (
                h
                / 3
                * (
                    y[0]
                    + y[n - 1]
                    + 4 * sum([y[i] for i in range(1, n - 1) if i % 2 != 0])
                    + 3 * sum([y[i] for i in range(2, n - 2) if i % 2 == 0])
                )
            )
            if abs(sum1 - I_true) <= eps:
                break
            n += 2

        print("\nDivided by: " + str(n))
        print("Solution I: " + str(sum1))
    except Exception:
        print("Gap!")
