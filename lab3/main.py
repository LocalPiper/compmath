from logic import conveyor

if __name__ == "__main__":
    print("CompLab3 by LocalPiper")
    print("Variant #13: Integration")
    try:
        conveyor.process()
    except EOFError:
        print("\nLeaving")
    except KeyboardInterrupt:
        print("\nLeaving")
