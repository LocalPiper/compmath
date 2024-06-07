from input_handlers.request_data import *
from logic.solver import solve
from logic.verifier import Verifier


def process():
    problem = select_func()
    verifier = Verifier()
    problem.solver = solve
    problem.solver(problem)
