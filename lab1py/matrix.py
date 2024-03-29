class Matrix:
    def __init__(self):
        self.dimension = 0
        self.presicion = 0
        self.matrix = []
        self.expansion = []
        self.solution = []


    def print_matrix(self):
        print("Matrix of dimension: " + str(self.dimension))
        for i in range(self.dimension):
            s = ""
            for j in range(self.dimension):
                s += str(self.matrix[i][j]) + " "
            s += "| " + str(self.expansion[i])
            print(s)
        print("\n")

    def get_diagonal(self):
        diag = []
        for i in range(self.dimension):
            diag.append(self.matrix[i][i])
        return diag
    
    def print_solution(self):
        print("Solution:")
        for i in range(self.dimension):
            print("x" + str(i+1) + " = " + str((self.solution[i])) + "+-" + str(self.presicion))