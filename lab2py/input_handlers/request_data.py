def request_presicion():
    while True:
        try:
            eps = float(input("Input presicion: "))
            if (eps < 1) and (eps > 2 * pow(10, -308)):
                return eps
            print("Wrong input! Try again")
        except ValueError:
            print("Wrong input! Try again")


def request_bounds():
    while True:
        try:
            a = float(input("HD\SECANT\SI: Input lower bound a: "))
            b = float(input("HD\SECANT\SI: Input upper bound b: "))
            if a < b:
                return a, b
            print("Wrong input! Try again")
        except ValueError:
            print("Wrong input! Try again")


def request_starting_approximation(a, b):
    while True:
        try:
            x = float(input("SI: Input starting approximation: "))
            if (x >= a) and (x <= b):
                return x
            print("Wrong input! Try again")
        except ValueError:
            print("Wrong input! Try again")


def request_next_approximation(a, b):
    while True:
        try:
            x = float(input("SECANT: Input next approximation: "))
            if (x >= a) and (x <= b):
                return x
            print("Wrong input! Try again")
        except ValueError:
            print("Wrong input! Try again")


def request_approximations():
    while True:
        try:
            x = float(input("NEWTON: Input starting x: "))
            y = float(input("NEWTON: Input starting y: "))
            return x, y
        except ValueError:
            print("Wrong input! Try again")
