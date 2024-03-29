import eq_classes.system_eq
import data.data2_1, data.data2_2, data.data2_3


def select_sys():
    print("\nSelect system of equations:")
    print("1: x^3 + y^2 = 10")
    print("   2^x + y = 1")
    print()
    print("2: x^2 + y^2 = 4")
    print("   y = 3x^2")
    print()
    inp = 0
    while True:
        try:
            inp = int(input("Input number: "))
            if inp == 1:
                s = eq_classes.system_eq.EqSystem()
                s.f = data.data2_1.f
                s.g = data.data2_1.g
                s.dfx = data.data2_1.dfx
                s.dfy = data.data2_1.dfy
                s.dgx = data.data2_1.dgx
                s.dgy = data.data2_1.dgy
                return s
            elif inp == 2:
                s = eq_classes.system_eq.EqSystem()
                s.f = data.data2_2.f
                s.g = data.data2_2.g
                s.dfx = data.data2_2.dfx
                s.dfy = data.data2_2.dfy
                s.dgx = data.data2_2.dgx
                s.dgy = data.data2_2.dgy
                return s

            print("Wrong input! Try again")
        except ValueError:
            print("Wrong input! Try again")
