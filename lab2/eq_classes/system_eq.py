import eq_classes.problem
import numpy as np
import matplotlib.pyplot as plt


class EqSystem(eq_classes.problem.Problem):
    def __init__(self):
        super().__init__()
        self.f = None
        self.g = None
        self.dfx = None
        self.dfy = None
        self.dgx = None
        self.dgy = None

    def draw_graph(self, l_b, r_b):
        # TODO: fix this shit
        """
        if abs(l_b - r_b) > 100:
            print("PLOTTER: Interval too large for plotter to work")
            return
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection="3d")
        x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
        z = self.f(x, y)
        ax.plot_surface(x, y, z)
        plt.show()
        """
