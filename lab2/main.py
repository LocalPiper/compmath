import logic.conveyor as conveyor

if __name__ == "__main__":
    print("CompLab2 by LocalPiper")
    print("Variant #13: HD, Newton, Simple Iteration")
    try:
        conveyor.process()
    except EOFError:
        print("\nLeaving")
    except KeyboardInterrupt:
        print("\nLeaving")
