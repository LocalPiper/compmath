from data_class.points import Points


def request_file():
    print("Your file contents should look like this:")
    print("n")
    print("x1 x2 x3 ... xn")
    print("y1 y2 y3 ... yn")
    print("If not, unexpected errors will occur")
    print()
    n = 0
    x = []
    y = []
    try:
        filename = input("Input file name: ")
        f = open(filename, "r")
        n = int(f.readline())
        x = [float(i) for i in f.readline().split(" ")]
        y = [float(j) for j in f.readline().split(" ")]
        if len(x) == len(y) and len(x) == n:
            points = Points()
            points.n = n
            points.x = x
            points.y = y
            return points
        else:
            raise Exception
    except Exception:
        print("File not found or corrupted!")
        raise FileNotFoundError


def request_by_hand():
    n = 0
    x = []
    y = []

    while True:
        try:
            n = int(input("Input number of points (should be positive integer): "))
            if n <= 2:
                raise ValueError
            print("Input exactly " + str(n) + " values of x:")
            for _ in range(n):
                x.append(float(input()))
            print("Input exactly " + str(n) + " values of y:")
            for _ in range(n):
                y.append(float(input()))
            points = Points()
            points.n = n
            points.x = x
            points.y = y
            return points
        except ValueError:
            print("Wrong input! Try again")


def request_auto(f):
    while True:
        try:
            n = int(input("Input number of points (positive integer): "))
            if n <= 2:
                raise ValueError
            a = float(input("Input lower bound: "))
            b = float(input("Input upper bound (should be GREATER than lower bound): "))
            if a >= b:
                raise ValueError
            points = Points()
            points.generate(f, a, b, n)
            return points
        except ValueError:
            print("Wrong input! Try again")


def request_target():
    while True:
        try:
            target = float(input("Input target: "))
            return target
        except ValueError:
            print("Wrong input! Try again")
