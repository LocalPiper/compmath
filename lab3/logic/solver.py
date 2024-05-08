import eq_class.equation
from input_handlers.request_data import *
from methods import rectangle
from methods import trap
from methods import simpson


def prepare_rect(eq: eq_class.equation.Equation):
    try:
        print("\nRECT: Preparing to perform rectangle...")

        e = request_presicion()
        a, b = request_bounds()
        rectangle.perform_rectangle(eq, a, b, e)
    except OverflowError:
        print(
            "ERROR: Numerical overflow occurred. Please, refrain from inputting large numbers"
        )


def prepare_trap(eq: eq_class.equation.Equation):
    try:
        print("\nTRAP: Preparing to perform trapezoid...")

        e = request_presicion()
        a, b = request_bounds()
        trap.perform_trapezoid(eq, a, b, e)
    except OverflowError:
        print(
            "ERROR: Numerical overflow occurred. Please, refrain from inputting large numbers"
        )


def prepare_simpson(eq: eq_class.equation.Equation):
    try:
        print("\nSIMPSON: Preparing to simp...")

        e = request_presicion()
        a, b = request_bounds()
        simpson.perform_simpson(eq, a, b, e)
    except OverflowError:
        print(
            "ERROR: Numerical overflow occurred. Please, refrain from inputting large numbers"
        )


def solve(eq: eq_class.equation.Equation):
    prepare_rect(eq)
    prepare_trap(eq)
    prepare_simpson(eq)
