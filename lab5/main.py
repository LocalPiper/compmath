from logic import conveyor
import warnings


if __name__ == "__main__":
    print("CompLab5 by LocalPiper")
    print("Variant #13: Interpolation")
    warnings.filterwarnings("ignore")
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
