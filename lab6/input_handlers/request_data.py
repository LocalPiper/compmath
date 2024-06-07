import data.funcs
from data_class.func_data import FuncData


def select_func():
    print("\nSelect differential equation:")
    print("1: y' = y + (1 + x)y^2")
    print("2: (x + y)y' + y = 0")
    print("3: y' = x + y")
    print()

    inp = 0

    while True:
        try:
            inp = int(input("Input number: "))
            fd = FuncData()
            match inp:
                case 1:
                    fd.f = data.funcs.f1
                    fd.fs = data.funcs.f1_s
                    fd.fc = data.funcs.f1_c
                    return request_by_hand(fd)
                case 2:
                    fd.f = data.funcs.f2
                    fd.fs = data.funcs.f2_s
                    fd.fc = data.funcs.f2_c
                    return request_by_hand(fd)
                case 3:
                    fd.f = data.funcs.f3
                    fd.fs = data.funcs.f3_s
                    fd.fc = data.funcs.f3_c
                    return request_by_hand(fd)
                case _:
                    print("Wrong input! Try again")

        except ValueError:
            print("Wrong input! Try again")


def request_by_hand(fd):
    y0 = None
    a = None
    b = None
    h = None
    eps = None
    while True:
        try:
            y0 = float(input("Input y0 (or y(x0)): "))
            a = float(input("Input lower bound: "))
            b = float(input("Input upper bound (should be GREATER than lower bound): "))
            if a >= b:
                raise ValueError
            h = float(input("Input step (should be greater than 0): "))
            if h <= 0:
                raise ValueError
            eps = float(
                input("Input presicion (should be GREATER than 0 and LESS than 1): ")
            )
            if (eps <= 0) or (eps >= 1):
                raise ValueError
            fd.y0 = y0
            fd.a = a
            fd.b = b
            fd.h = h
            fd.eps = eps
            return fd

        except ValueError:
            print("Wrong input! Try again")
