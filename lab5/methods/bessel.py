from data_class.points import Points


def make_label_table(pts: Points):
    n = pts.n
    new_def = {}
    i = 0
    for j in range(-int(n / 2), int(n / 2) + 1):
        new_def[j] = i
        i += 1
    print(new_def)
    return new_def


def perform(pts: Points, target: float):
    print("\nPerforming Bessel...")
    x = pts.x
    y = pts.y
    n = pts.n
    st = pts.st
    label_table = make_label_table(pts)
    t = (target - x[label_table[0]]) / (x[label_table[1]] - x[label_table[0]])
    print(t)

    k1 = 1
    k2 = t - 1 / 2
    fac1 = 2
    fac2 = 3
    ac1 = 1
    ac2 = 1
    res = (y[label_table[0]] + y[label_table[1]]) / 2 + k2 * st["Δ^1yi"][label_table[0]]
    print(res)
    i = -1
    while i != -n:
        try:
            pattern = "Δ^" + str(fac1) + "yi"
            pattern2 = "Δ^" + str(fac2) + "yi"
            ac1 *= fac1
            ac2 *= fac2
            k1 *= (t - i + 1) * (t + i)
            k2 *= (t - i + 1) * (t + i)
            res += (
                k1
                / ac1
                * (st[pattern][label_table[i]] + st[pattern][label_table[i + 1]])
                / 2
                + k2 / ac2 * st[pattern2][label_table[i]]
            )
            ac1 *= fac1 + 1
            ac2 *= fac2 + 1
            print(pattern)
            print(pattern2)
            fac1 += 2
            fac2 += 2
            i -= 1
        except Exception:
            break

    print("f(x) = " + str(res))
