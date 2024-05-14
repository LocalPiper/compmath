import data.funcs
from input_handlers import request_data


def select_format():
    print("\nSelect format:")
    print("1: input x and y data by hand")
    print("2: input x and y data by file")
    print("3: select predefined function")
    print()
    inp = 0

    while True:
        try:
            inp = int(input("Input number: "))
            match inp:
                case 1:
                    return request_data.request_by_hand()
                case 2:
                    return request_data.request_file()
                case 3:
                    return select_func()
                case _:
                    print("Wrong input! Try again")

        except ValueError:
            print("Wrong input! Try again")


def select_func():
    print("\nSelect function to generate data:")
    print("1: sin(x)")
    print("2: cos(x)")
    print("3: e^x")
    print("4: log(x)")
    print("5: please don't pick me")
    print()

    inp = 0

    while True:
        try:
            inp = int(input("Input number: "))
            match inp:
                case 1:
                    return request_data.request_auto(data.funcs.f_sin)
                case 2:
                    return request_data.request_auto(data.funcs.f_cos)
                case 3:
                    return request_data.request_auto(data.funcs.f_exp)
                case 4:
                    return request_data.request_auto(data.funcs.f_log2)
                case 5:
                    return request_data.request_auto(data.funcs.f_wtf)
                case _:
                    print("Wrong input! Try again")

        except ValueError:
            print("Wrong input! Try again")
