from matrix import Matrix

def check_zeroes(matrix: Matrix):
    for i in range(matrix.dimension):
        if sum(matrix.matrix[i]) == 0:
            print("Seems like this matrix has a full-zero row: " + str(i + 1))
            return True
    return False

def check_linear_dependency(matrix: Matrix):
    m = matrix.matrix
    det = determinant_fast(m)
    if det == 0:
        print("Seems like this matrix has a linear dependency")
        return True
    return False

def determinant_fast(A : list):
    n = len(A)
    AM = A
    for fd in range(n):
        for i in range(fd+1,n):
            if AM[fd][fd] == 0:
                AM[fd][fd] = 1.0e-18
            crScaler = AM[i][fd] / AM[fd][fd] 
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    product = 1.0
    for i in range(n):
        product *= AM[i][i] 
 
    return product



def check_health(matrix: Matrix):
    diag = matrix.get_diagonal()
    if diag.count(0) != 0:
        return True
    return False
    