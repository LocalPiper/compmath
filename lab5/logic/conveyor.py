from input_handlers.get_points import *
from logic.solver import solve
from logic.verifier import Verifier


def process():
    problem = select_format()
    verifier = Verifier()
    verifier.n = problem.n
    verifier.x = problem.x
    verifier.y = problem.y
    verifier.perform_validation()
    problem.n = verifier.n
    problem.x = verifier.x
    problem.y = verifier.y
    problem.print_data()
    # problem.plot()
    problem.solver = solve
    problem.solver(problem)
