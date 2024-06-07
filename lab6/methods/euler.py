from data_class.func_data import FuncData

def perform(fd: FuncData):
    print("\nPerforming Euler...")
    x = fd.a
    y = fd.y0
    c = fd.fc(x, y)
    x_arr = []
    y_arr = []
    y_true = []
    step = 0
    print(f"N    {'x_i':<10} {'y_i':<10} {'f(x_i, y_i)':<15} {'точное решение':<15} |y_тoчн - y_i|")

    while x <= fd.b:
        fi = fd.f(x, y)
        yi = y + fd.h * fd.f(x, y)
        xi = x + fd.h
        fs = fd.fs(x, c)
        error = abs(fs - y)
        x_arr.append(x)
        y_arr.append(y)
        y_true.append(fs)
        print(f"{step:<2}   {x:<10.5f} {y:<10.5f} {fi:<15.5f} {fs:<15.5f} {error:<15.5f}")

        x = xi
        y = yi
        
        step += 1

    x_arr.append(x)
    y_arr.append(y)
    fs = fd.fs(x, c)
    y_true.append(fs)
    fd.x_data = x_arr
    fd.euler = y_arr
    error = abs(fs - y)
    fd.y_true = y_true
    print(f"{step:<2}   {x:<10.5f} {y:<10.5f} {fd.f(x, y):<15.5f} {fs:<15.5f} {error:<15.5f}")

    return fd
