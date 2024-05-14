from data_class.points import Points
from utils.newton import NewtonDivSolver


def mult(xl: list, x: float, k: int):
    res = 1
    for i in range(k):
        res *= x - xl[i]
    return res


def perform(pts: Points, x: float):
    print("\nPerforming Newton div...")
    nds = NewtonDivSolver()
    nds.x = pts.x
    nds.y = pts.y
    res = nds.subtraction_order(0, 0)
    for k in range(1, len(nds.x)):
        res += nds.subtraction_order(0, k) * mult(pts.x, x, k)
    print("f(x) = " + str(res))
