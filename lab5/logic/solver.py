from data_class.points import Points
from utils.subtractor import find_subtraction
from input_handlers.request_data import request_target
import methods.lagrange as lg
import methods.newton_div as ntd
import methods.newton_end as nte
import methods.gauss as gs
import methods.stirling as st
import methods.bessel as bs

import numpy as np


def make_subtractions_table(pts: Points):
    st = {"xi": []}
    for i in range(0, pts.n):
        pattern = "Δ^" + str(i) + "yi"
        st[pattern] = []

    st["xi"] = pts.x
    st["Δ^0yi"] = pts.y
    for i in range(1, pts.n):
        pattern = "Δ^" + str(i) + "yi"
        st[pattern] = np.array(find_subtraction(pts.y, i))

    pts.st = st
    pts.print_table()


def solve(pts: Points):
    make_subtractions_table(pts)
    x = request_target()
    lg.perform(pts, x)
    ntd.perform(pts, x)
    nte.perform(pts, x)
    gs.perform(pts, x)
    st.perform(pts, x)
    bs.perform(pts, x)
