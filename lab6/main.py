from logic import conveyor
import warnings


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    print("CompLab6 by LocalPiper")
    print("Variant #13: Euler, M_Euler, Milne")
    

    try:
        conveyor.process()
    except EOFError:
        print("\nLeaving")
    except KeyboardInterrupt:
        print("\nLeaving")
    except FileNotFoundError:
        print("\nLeaving")
    except Exception:
        print("\nLeaving")
