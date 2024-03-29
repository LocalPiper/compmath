import eq_classes.equation, eq_classes.system_eq
from input_handlers.request_data import *
from input_handlers.request_proceed import request_proceed
from utils.method_utils import *
import logic.verifier as verifier
from methods import hd
from methods import secant
from methods import si
from methods import newton


def prepare_hd(eq: eq_classes.equation.Equation):
    try:
        print("\nHD: Preparing to perform halving division...")

        e = request_presicion()
        a, b = request_bounds()
        eq.draw_graph(a, b)
        proceed = True
        if not verifier.analyze_root_existence(eq, a, b):
            proceed = request_proceed()

        if not proceed:
            return

        if hd.check_hd(e, a, b):
            hd.perform_hd(eq, e, a, b)
    except OverflowError:
        print(
            "ERROR: Numerical overflow occurred. Please, refrain from inputting large numbers"
        )


def prepare_secant(eq: eq_classes.equation.Equation):
    try:
        print("\nSECANT: Preparing to perform secant...")

        e = request_presicion()
        a, b = request_bounds()
        eq.draw_graph(a, b)
        proceed = True
        if not verifier.analyze_root_existence(eq, a, b):
            proceed = request_proceed()

        if not proceed:
            return

        res, x = calcultate_starting_approximation(eq, a, b)
        if not res:
            proceed = request_proceed()

        if not proceed:
            return

        x = a
        xi = request_next_approximation(a, b)

        secant.perform_secant(eq, x, xi, e)
    except OverflowError:
        print(
            "ERROR: Numerical overflow occurred. Please, refrain from inputting large numbers"
        )


def prepare_si(eq: eq_classes.equation.Equation):
    try:
        print("\nSI: Preparing to perform simple iteration...")
        e = request_presicion()
        a, b = request_bounds()
        eq.draw_graph(a, b)
        proceed = True
        if not verifier.analyze_root_existence(eq, a, b):
            proceed = request_proceed()

        if not proceed:
            return

        x = request_starting_approximation(a, b)
        l = calculate_lambda(eq, a, b)

        if si.check_si(eq, a, b, l):
            si.perform_si(eq, x, l, e)
    except OverflowError:
        print(
            "ERROR: Numerical overflow occurred. Please, refrain from inputting large numbers"
        )


def solve_eq(eq: eq_classes.equation.Equation):
    prepare_hd(eq)
    prepare_secant(eq)
    prepare_si(eq)


def prepare_newton(sys: eq_classes.system_eq.EqSystem):
    try:
        print("\nPreparing to perform Newton method")
        e = request_presicion()
        solver_matrix, roots = [[sys.dfx, sys.dfy], [sys.dgx, sys.dgy]], [sys.f, sys.g]
        x0, y0 = request_approximations()
        sys.draw_graph(x0, y0)
        newton.perform_newton(sys, x0, y0, solver_matrix, roots, e)
    except OverflowError:
        print(
            "ERROR: Numerical overflow occurred. Please, refrain from inputting large numbers"
        )
    except ZeroDivisionError:
        print("ERROR: Encountered unsolvable matrix - impossible to proceed")


def solve_sys(sys: eq_classes.system_eq.EqSystem):
    prepare_newton(sys)
