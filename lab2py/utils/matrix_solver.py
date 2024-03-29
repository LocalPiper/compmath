def calc_det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def solve_matrix(a, b):
    if calc_det(a) == 0:
        raise ZeroDivisionError
    delta_y = (b[1] - a[1][0] * b[0] / a[0][0]) / (
        a[1][1] - a[1][0] * a[0][1] / a[0][0]
    )
    delta_x = b[0] / a[0][0] - delta_y * a[0][1] / a[0][0]
    return delta_x, delta_y
