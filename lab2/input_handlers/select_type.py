def select_type():
    print("\nWhat would you like to solve?")
    print("1 - non-linear equation")
    print("2 - system of non-linear equations")
    print()
    inp = 0
    while True:
        try:
            inp = int(input("Input type: "))
            if (inp == 1) or (inp == 2):
                return inp
            print("Wrong input! Try again")
        except ValueError:
            print("Wrong input! Try again")
