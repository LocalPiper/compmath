from data_class.points import Points


def mult(xl: list, x: float, i: float):
    res_up = 1
    res_down = 1
    for j in range(len(xl)):
        if i != j:
            res_up *= x - xl[j]
            res_down *= xl[i] - xl[j]
    return res_up / res_down


def perform(pts: Points, x: float):
    print("\nPerforming Lagrange...")
    res = 0
    for i in range(len(pts.x)):
        try:
            res += pts.y[i] * mult(pts.x, x, i)
        except Exception:
            break
    print("f(x) = " + str(res))
