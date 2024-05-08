import data.data1, data.data2, data.data3
import eq_class.equation


def select_eq():
    print("\nSelect equation:")
    print("1: -2x^3 - 5x^2 + 7x - 13")
    print("2: 1/x + e^x")
    print("3: cos^2(3x)")
    print()
    inp = 0
    while True:
        try:
            inp = int(input("Input number: "))
            if (inp == 1) or (inp == 2) or (inp == 3):
                e = eq_class.equation.Equation()
                if inp == 1:
                    e.f = data.data1.f
                    e.I = data.data1.I
                elif inp == 2:
                    e.f = data.data2.f
                    e.I = data.data2.I
                else:
                    e.f = data.data3.f
                    e.I = data.data3.I
                return e
            print("Wrong input! Try again")
        except ValueError:
            print("Wrong input! Try again")
