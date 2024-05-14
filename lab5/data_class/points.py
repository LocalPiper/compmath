import numpy as np
import matplotlib.pyplot as plt


class Points:
    def __init__(self):
        self.n = None
        self.x = None
        self.y = None
        self.st = None

    def generate(self, f, a, b, n):
        self.n = n
        self.x = np.array(np.linspace(a, b, self.n))
        self.y = np.array([f(xi) for xi in self.x])

    def plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y)
        ax.set_aspect("auto")
        ax.grid(True, which="both")

        ax.axhline(y=0, color="k")
        ax.axvline(x=0, color="k")
        plt.show()

    def print_data(self):
        print("Contained data:")
        print("n: " + str(self.n))
        if self.n != 0:
            print("(x, y):")
            for i in range(self.n):
                print("(" + str(self.x[i]) + ", " + str(self.y[i]) + ")")

    def print_table(self):
        print("\nSubtraction table:")
        for key in self.st.keys():
            print(key + " : ")
            print(self.st[key])
        print()
