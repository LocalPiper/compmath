from input_handlers.select_type import *
from input_handlers.select_eq import *
from input_handlers.select_sys import *
from eq_classes import *
from logic.solver import solve_eq
from logic.solver import solve_sys


def process():
    t = select_type()
    problem = select_eq() if t == 1 else select_sys()
    if t == 1:
        problem.solver = solve_eq
        problem.solver(problem)
    else:
        problem.solver = solve_sys
        problem.solver(problem)
