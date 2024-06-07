from data_class.func_data import FuncData
import matplotlib.pyplot as plt

def perform(fd: FuncData):
    print("\nPerforming Advanced Euler...")
    x = fd.a
    y = fd.y0
    c = fd.fc(x, y)
    y_arr = []
    step = 0
    print(f"N    {'x_i':<10} {'y_i':<10} {'f(x_i, y_i)':<15} {'точное решение':<15} |y_тoчн - y_i|")

    while x <= fd.b:
        fi = fd.f(x, y)
        xi = x + fd.h
        fi_2 = fd.f(xi, y + fd.h * fi)
        fi_3 = fi + fi_2
        yi = y + fd.h/2 * fi_3
        
        fs = fd.fs(x, c)
        error = abs(fs - y)
        y_arr.append(y)
        print(f"{step:<2}   {x:<10.5f} {y:<10.5f} {fi:<15.5f} {fs:<15.5f} {error:<15.5f}")

        x = xi
        y = yi
        step += 1

    fs = fd.fs(x, c)
    y_arr.append(y)
    error = abs(fs - y)
    fd.adv_euler = y_arr
    print(f"{step:<2}   {x:<10.5f} {y:<10.5f} {fd.f(x, y):<15.5f} {fs:<15.5f} {error:<15.5f}")
    return fd

