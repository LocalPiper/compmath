from matrix import Matrix
import solvability


def check_diagonal_dominance(matrix: Matrix):
    for i in range(matrix.dimension):
        if abs(matrix.matrix[i][i]) < (
            sum([abs(x) for x in matrix.matrix[i]]) - abs(matrix.matrix[i][i])
        ):
            return False
    return True


def diagonal_dominant(l: list):
    for i in range(len(l)):
        if abs(l[i]) >= sum([abs(x) for x in l]) - abs(l[i]):
            return i
    return -1


def try_sort_by_diagonal(matrix: Matrix):
    # finding dominating elements
    sorting = [-1 for _ in range(matrix.dimension)]
    success = True

    for i in range(matrix.dimension):
        res = diagonal_dominant(matrix.matrix[i])
        sorting[i] = res

    # trying to sort the matrix
    raw_sorted_matrix = [[] for _ in range(matrix.dimension)]
    raw_sorted_matrix_expansion = [0 for _ in range(matrix.dimension)]
    buffer = []
    for i in range(len(sorting)):
        if sorting[i] != -1:
            if len(raw_sorted_matrix[sorting[i]]) == 0:
                raw_sorted_matrix[sorting[i]] = matrix.matrix[i]
                raw_sorted_matrix_expansion[sorting[i]] = matrix.expansion[i]
            else:
                buffer.append(i)
        else:
            buffer.append(i)

    # pushing leftovers into our matrix
    if len(buffer) != 0:
        success = False
    for i in range(len(buffer)):
        for j in range(matrix.dimension):
            if len(raw_sorted_matrix[j]) == 0:
                raw_sorted_matrix[j] = matrix.matrix[buffer[i]]
                raw_sorted_matrix_expansion[j] = matrix.expansion[buffer[i]]
                break

    # creating new matrix out of the monstrosity we just did
    new_matrix = Matrix()
    new_matrix.dimension = matrix.dimension
    new_matrix.presicion = matrix.presicion
    new_matrix.matrix = [x for x in raw_sorted_matrix]
    new_matrix.expansion = [x for x in raw_sorted_matrix_expansion]
    return new_matrix, success


def create_normalized_matrix(matrix: Matrix):
    n_matrix = Matrix()
    n_matrix.dimension = matrix.dimension
    for i in range(matrix.dimension):
        n_matrix.expansion.append(matrix.expansion[i] / matrix.matrix[i][i])
        m = []
        for j in range(matrix.dimension):
            if i == j:
                m.append(0)
            else:
                m.append(matrix.matrix[i][j] / matrix.matrix[i][i])
        n_matrix.matrix.append(m)

    return n_matrix


def simple_iteration(matrix: Matrix):
    # create a copy for solvability checks
    copy = Matrix()
    copy.dimension = matrix.dimension
    copy.presicion = matrix.presicion
    copy.expansion = [x for x in matrix.expansion]
    copy.matrix = [[y for y in x] for x in matrix.matrix]

    # run solvability checks
    if solvability.check_zeroes(copy) or solvability.check_linear_dependency(copy):
        print("Matrix cannot be solved!")
        return

    running = True
    it = 0
    # checking if matrix is already dominant
    if check_diagonal_dominance(matrix):
        print("Matrix is already diagonally dominant")
    else:
        # trying to transform matrix to diagonal dominance
        matrix, result = try_sort_by_diagonal(matrix)
        if not result:
            print("Matrix diverges! Trying to perform 100 computations...")

        print("After transforming, matrix looks like this:")
        matrix.print_matrix()
    try:
        # check main diagonal
        need_restructure = solvability.check_health(matrix)
        if need_restructure:
            matrix, success = rearrange_matrix(matrix)
            if not success:
                print("Matrix cannot be solved!")
                return

        # trying to normalize matrix
        n_matrix = create_normalized_matrix(matrix)
        print("After normalizing, matrix looks like this:")
        n_matrix.print_matrix()
        vector = [x for x in matrix.expansion]

        for i in range(matrix.dimension):
            matrix.solution.append(n_matrix.expansion[i])

        # running computations...
        while (running) and (it < 100):
            new_vector = []

            for i in range(matrix.dimension):
                val = n_matrix.expansion[i]
                for j in range(matrix.dimension):
                    val -= n_matrix.matrix[i][j] * vector[j]
                new_vector.append(val)

            for i in range(matrix.dimension):
                matrix.solution[i] = new_vector[i]

            matrix.print_solution()
            print()
            delta = []

            for i in range(matrix.dimension):
                delta.append(abs(new_vector[i] - vector[i]))

            vector = [x for x in new_vector]
            if max(delta) < matrix.presicion:
                running = False
            it += 1

        matrix.print_solution()
        print("Iterations performed: " + str(it))
        print("Errors: ")
        for i in range(len(delta)):
            print("delta x" + str(i + 1) + ": " + str(delta[i]))

    except ZeroDivisionError:
        print(
            "It seems like either you printed in the wrong matrix \nor my dumbass author screwed up while restructuring the matrix, therefore creating a zero division"
        )
    except IndexError:
        print("It seems like you printed in the wrong matrix. Check your input file")


def rearrange_matrix(m: Matrix):
    matrix = m.matrix
    n = len(matrix)

    sorted_matrix = sorted(matrix, key=lambda x: x.count(0))

    for i in range(n):
        if sorted_matrix[i][i] == 0:
            for j in range(i + 1, n):
                if sorted_matrix[j][i] != 0:
                    sorted_matrix[i], sorted_matrix[j] = (
                        sorted_matrix[j],
                        sorted_matrix[i],
                    )

                    break
            else:
                print(
                    "It's impossible to rearrange matrix - main diagonal still has zeroes"
                )
                return m, False

    m.matrix = sorted_matrix
    return m, True
