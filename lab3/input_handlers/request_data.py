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
            a = float(input("RECT\TRAP\SIMPSON: Input lower bound a: "))
            b = float(input("RECT\TRAP\SIMPSON: Input upper bound b: "))
            if a < b:
                return a, b
            print("Wrong input! Try again")
        except ValueError:
            print("Wrong input! Try again")
