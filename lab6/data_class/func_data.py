import numpy as np
import matplotlib.pyplot as plt


class FuncData:
    def __init__(self):
        self.f = None
        self.fs = None
        self.fc = None
        self.y0 = None
        self.a = None
        self.b = None
        self.h = None
        self.eps = None
        self.x_data = None
        self.euler = None
        self.adv_euler = None
        self.milne = None
        self.y_true = None

    def plot(self, flag):
        _, ax = plt.subplots()
        ax.grid(True, which="both")
        ax.axhline(y=0, color="k")
        ax.axvline(x=0, color="k")
        ax.plot(self.x_data, self.y_true, label="True")
        ax.plot(self.x_data, self.euler, label="Euler")
        ax.plot(self.x_data, self.adv_euler, label="Advanced Euler")
        if flag:
            ax.plot(self.x_data, self.milne, label="Milne")
        ax.legend()
        plt.show()
