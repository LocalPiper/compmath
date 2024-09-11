from matrix import Matrix

FILE_MODE = "f"
CONSOLE_MODE = "m"


def read_matrix_from_file():
    print("Your file structure should look like this:")
    print("n p")
    print("a11 a12 ... a1n b1 ")
    print("a21 a22 ... a2n b2 ")
    print("... ... ... ... ...")
    print("an1 an2 ... ann bn ")
    print("where n - dimension of matrix, p - presicion")
    print("Example:")
    print("3 0.00001")
    print("1 2 3 1")
    print("4 5 6 2")
    print("7 8 9.1 3\n")
    
    done = False
    while not done:
        filename = input("Input file name: ")
        matrix = Matrix()
        try:
            with open(filename, "r") as f:
                data = f.readline().strip().split(" ")
                matrix.dimension = int(data[0])
                if matrix.dimension <= 0:
                    print("Wrong dimension value!")
                    raise ValueError
                matrix.presicion = float(data[1])
                if matrix.presicion >= 1 or matrix.presicion <= 2.2e-308:
                    print("Wrong presicion value!")
                    raise ValueError
                for _ in range(matrix.dimension):
                    row = [float(x) for x in f.readline().strip().split(" ")]
                    res = row.pop()
                    matrix.expansion.append(res)
                    matrix.matrix.append(row)
            done = True
        except IndexError:
            print("Wrong file format")
        except ValueError:
            print("Wrong file format")
    matrix.print_matrix()
    return matrix
    
def read_matrix_from_console():
    matrix = Matrix()
    done = False
    while not done:
        try:
            matrix.dimension = int(input("Input dimension: "))
            if matrix.dimension <= 0:
                raise ValueError
        except ValueError:
            print("Wrong dimension value! Try again")
            continue

        try:
            matrix.presicion = float(input("Input presicion: "))
            if (matrix.presicion >= 1) or (matrix.presicion <= 2.2e-308):
                raise ValueError
        except ValueError:
            print("Wrong presicion value! Try again")
            continue
        
        try:
            for i in range(matrix.dimension):
                row = [float(x) for x in input("Input " + str(i + 1) + " row of matrix: ").split(" ")]
                if len(row) != matrix.dimension:
                    raise ValueError
                matrix.matrix.append(row)
        except ValueError:
            print("Wrong values! Try again")
            continue

        res = [float(x) for x in input("Input vector of answers: ").split(" ")]
        for a in res:
            matrix.expansion.append(a)
        done = True

    matrix.print_matrix()
    return matrix

def read_matrix():
    print("Choose preferred option:")
    print("m - input matrix manually (for experienced users only)")
    print("f - input matrix by file")

    running = True
    mode = ''
    while (running):
        mode = input()
        if ((mode != FILE_MODE) and (mode != CONSOLE_MODE)):
            print("Wrong input! Try again")
        else:
            running = False
    
    if (mode == FILE_MODE):
        return read_matrix_from_file()
    else:
        return read_matrix_from_console()