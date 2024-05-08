from input_handlers.select_eq import *
from eq_class import *
from logic.solver import solve


def process():
    problem = select_eq()
    problem.solver = solve
    problem.solver(problem)
