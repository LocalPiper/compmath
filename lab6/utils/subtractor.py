from functools import lru_cache


class Subtractor:
    def __init__(self):
        self.y = None

    @lru_cache
    def find_subtraction_recursive(self, i: int, layer: int):
        if layer == 1:
            return self.y[i + 1] - self.y[i]
        return self.find_subtraction_recursive(
            i + 1, layer - 1
        ) - self.find_subtraction_recursive(i, layer - 1)


def find_subtraction(y: list, layer: int):
    res = []
    sb = Subtractor()
    sb.y = y
    for i in range(0, len(y) - layer):
        res.append(sb.find_subtraction_recursive(i, layer))
    return res
