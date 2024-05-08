import eq_class.equation
from logic.verifier import runge_rule
from sympy import integrate, Symbol

MAX_DIV = 1000


def perform_rectangle(eq: eq_class.equation.Equation, a, b, eps):
    print("\nPerforming rectangle: ")
    try:
        f = eq.f
        n = 2
        I = eq.I
        I_true = I(b) - I(a)
        print(I_true)
        perform_left_rect(f, a, b, eps, n, I_true)
        perform_right_rect(f, a, b, eps, n, I_true)
        perform_mid_rect(f, a, b, eps, n, I_true)
    except Exception:
        print("Gap!")


def perform_left_rect(f, a, b, eps, n, tr):
    print("\nPerforming rectangle left: ")
    while n < MAX_DIV:
        n += 2
        h = (b - a) / n
        x = [a + h * i for i in range(0, n)]
        x.append(b)
        sum1 = h * sum([f(x[i]) for i in range(0, n - 1)])
        if abs(sum1 - tr) <= eps:
            break

    print("\nDivided by: " + str(n))
    print("Solution I: " + str(sum1))


def perform_right_rect(f, a, b, eps, n, tr):
    print("\nPerforming rectangle right: ")
    while n < MAX_DIV:
        n += 2
        h = (b - a) / n
        x = [a + h * i for i in range(n)]
        x.append(b)
        sum1 = h * sum([f(x[i]) for i in range(1, n)])
        if abs(sum1 - tr) <= eps:
            break

    print("\nDivided by: " + str(n))
    print("Solution I: " + str(sum1))


def perform_mid_rect(f, a, b, eps, n, tr):
    print("\nPerforming rectangle mid: ")
    while n < MAX_DIV:
        n += 2
        h = (b - a) / n

        x = [a + h * i for i in range(0, n)]
        x.append(b)

        xm = [(x[i] + x[i - 1]) / 2 for i in range(1, n)]

        sum1 = h * sum([f(xm[i]) for i in range(n - 1)])
        if abs(sum1 - tr) <= eps:
            break

    print("\nDivided by: " + str(n))
    print("Solution I: " + str(sum1))
