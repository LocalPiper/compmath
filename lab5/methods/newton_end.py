from data_class.points import Points


def perform(pts: Points, x: float):
    print("\nPerforming Newton end...")
    t = (x - pts.x[0]) / (pts.x[1] - pts.x[0])
    res = pts.y[0]
    k1 = t
    pattern = "Δ^1yi"
    k2 = pts.st[pattern]
    for i in range(1, len(pts.x)):
        try:
            res += k1 * k2[0]
            k1 *= t - i
            pattern = "Δ^" + str(i + 1) + "yi"
            k2 = pts.st[pattern]
        except Exception:
            break

    print("f(x) = " + str(res))
