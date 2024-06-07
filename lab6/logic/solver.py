from data_class.func_data import FuncData
from methods import milne as ml
from methods import euler as eu, adv_euler as ae
import numpy as np


def solve(fd: FuncData):
    fd = eu.perform(fd)
    fd = ae.perform(fd)
    try:
        fd = ml.perform(fd)
    except ValueError:
        print("Shit happens, IG")
        fd.plot(False)
        return
    fd.plot(True)
