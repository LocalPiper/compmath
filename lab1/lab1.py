from io_matrix import read_matrix
from simple_iteration import simple_iteration
if __name__=="__main__":
    print("CompLab1 by LocalPiper")
    print("#13: Simple Iteration method")
    try:
        matrix = read_matrix()
        simple_iteration(matrix)
    except FileNotFoundError:
        print("Requested file was not found")