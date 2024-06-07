class NewtonDivSolver:
    def __init__(self):
        self.table = {}
        self.x = None
        self.y = None

    def subtraction_order(self, id1, id2):
        pattern = str(id1) + ":" + str(id2)
        if pattern in self.table.keys():
            return self.table[pattern]

        n = id2 - id1 + 1
        if n == 1:
            return self.y[id1]

        self.table[pattern] = (
            self.subtraction_order(id1 + 1, id2) - self.subtraction_order(id1, id2 - 1)
        ) / (self.x[id2] - self.x[id1])
        return self.table[pattern]
