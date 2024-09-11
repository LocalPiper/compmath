def request_proceed():
    while True:
        proceed = input("Continue despite warnings? (y/n): ")
        if proceed == "y":
            return True
        elif proceed == "n":
            return False
        print("Wrong input! Try again")
