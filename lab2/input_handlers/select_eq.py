import data.data1_1, data.data1_2, data.data1_3
import eq_classes.equation


def select_eq():
    print("\nSelect equation:")
    print("1: x^3 + 4.81x^2 - 17.37x + 5.38")
    print("2: x^3 - x + 4")
    print("3: e^x + sin(x)")
    print()
    inp = 0
    while True:
        try:
            inp = int(input("Input number: "))
            if (inp == 1) or (inp == 2) or (inp == 3):
                e = eq_classes.equation.Equation()
                if inp == 1:
                    e.f = data.data1_1.f
                    e.df = data.data1_1.df
                    e.d2f = data.data1_1.d2f
                elif inp == 2:
                    e.f = data.data1_2.f
                    e.df = data.data1_2.df
                    e.d2f = data.data1_2.d2f
                else:
                    e.f = data.data1_3.f
                    e.df = data.data1_3.df
                    e.d2f = data.data1_3.d2f
                return e
            print("Wrong input! Try again")
        except ValueError:
            print("Wrong input! Try again")
