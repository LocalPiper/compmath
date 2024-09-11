import eq_classes.problem
import matplotlib.pyplot as plt
import numpy as np


class Equation(eq_classes.problem.Problem):
    def __init__(self):
        super().__init__()
        self.f = None
        self.df = None
        self.d2f = None

    def draw_graph(self, l_b, r_b):
        if abs(l_b - r_b) > 100:
            print("PLOTTER: Interval too large for plotter to work")
            return
        x = np.linspace(l_b, r_b)
        y = []
        fig, ax = plt.subplots()
        for val in x:
            y.append(self.f(val))
        ax.plot(x, y)
        ax.set_aspect("auto")
        ax.grid(True, which="both")

        ax.axhline(y=0, color="k")
        ax.axvline(x=0, color="k")
        plt.show()
