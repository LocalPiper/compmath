from eq_classes.system_eq import EqSystem
from utils import matrix_solver

MAX_ITER = 1000
LOW = 10e-9


def perform_newton(sys: EqSystem, x, y, solver_matrix, roots, eps):
    print("\nPerforming newton method")
    delta_x = 1000000
    delta_y = 1000000
    iteration = 0
    f = sys.f
    g = sys.g
    appr_buf = []
    while iteration < MAX_ITER:
        iteration += 1
        matrix = [
            [solver_matrix[0][0](x, y) + LOW, solver_matrix[0][1](x, y) + LOW],
            [solver_matrix[1][0](x, y) + LOW, solver_matrix[1][1](x, y) + LOW],
        ]
        vect = [-1 * roots[0](x, y), -1 * roots[1](x, y)]
        delta_x, delta_y = matrix_solver.solve_matrix(matrix, vect)
        xi = x + delta_x
        yi = y + delta_y
        if (abs(x - xi) <= eps) and (abs(y - yi) <= eps):
            x = xi
            y = yi
            break
        x = xi
        y = yi

    print("Number of iterations: " + str(iteration))
    print("Solution x: " + str(x))
    print("Solution y: " + str(y))
    print("Solution f(x,y): " + str(f(x, y)))
    print("Solution g(x,y): " + str(g(x, y)))
    print()
