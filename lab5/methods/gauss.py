from data_class.points import Points


def make_label_table(pts: Points):
    n = pts.n
    new_def = {}
    i = 0
    for j in range(-int(n / 2), int(n / 2) + 1):
        new_def[j] = i
        i += 1
    return new_def


def gauss1(t, y, st, label_table):
    n = len(y)
    k1 = t
    k2 = k1

    pattern = "Δ^1yi"
    res = y[label_table[0]] + k1 * st[pattern][label_table[0]]
    fac = 2
    ac = 1
    for i in range(-1, -int(n / 2) - 1, -1):
        try:
            k1 *= t + i
            k2 *= (t + i) * (t - i)
            pattern = "Δ^" + str(fac) + "yi"
            pattern2 = "Δ^" + str(fac + 1) + "yi"
            ac *= fac
            res += st[pattern][label_table[i]] * k1 / ac

            ac *= fac + 1
            res += st[pattern2][label_table[i]] * k2 / ac
            fac += 2
        except KeyError:
            break
        except IndexError:
            break

    return res


def gauss2(t, y, st, label_table):
    n = len(y)
    k1 = t

    pattern = "Δ^1yi"
    res = y[label_table[0]] + k1 * st[pattern][label_table[-1]]

    i = -1
    fac = 2
    ac = 1
    while i != -int(n / 2) - 1:
        try:
            k1 *= t - i
            ac *= fac
            pattern = "Δ^" + str(fac) + "yi"
            res += st[pattern][label_table[i]] * k1 / ac
            pattern2 = "Δ^" + str(fac + 1) + "yi"
            ac *= fac + 1
            k1 *= t + i
            i -= 1

            res += st[pattern2][label_table[i]] * k1 / ac
            fac += 2
        except KeyError:
            break
        except IndexError:
            break
    return res


def perform(pts: Points, target: float):
    print("\nPerforming Gauss...")
    x = pts.x
    y = pts.y
    st = pts.st
    label_table = make_label_table(pts)
    t = (target - x[label_table[0]]) / (x[label_table[1]] - x[label_table[0]])
    if t > 0:
        res = gauss1(t, y, st, label_table)
    else:
        res = gauss2(t, y, st, label_table)

    print("f(x) = " + str(res))
