from functools import lru_cache

import numpy as np


class MatrixHash:
    def __hash__(self):
        """
        A polynomial hash function with modification --
        the element is multiplied by the position indexes
        to add stability to permutations of elements,
        indexes are numbered starting from 1 to avoid zero hash
        """
        hash = 0
        p = 65539  # base
        M = 1e9 + 7  # module
        for i in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
                hash += (p * hash + (self.data[i][j] * (i + 1) * (j + 1))) % M

        return int(hash)


class Matrix(MatrixHash):
    def __init__(self, data):
        self.data = data
        self.shape = (len(data), len(data[0] if len(data) > 0 else 0))

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError(
                f"ValueError: operands could not be broadcast together with shapes {self.shape} {other.shape}")
        row_num, col_num = self.shape[0], self.shape[1]
        mul_data = [[self.data[i][j] * other.data[i][j] for j in range(0, col_num)] for i in range(0, row_num)]
        return Matrix(mul_data)

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError(
                f"ValueError: operands could not be broadcast together with shapes {self.shape} {other.shape}")
        row_num, col_num = self.shape[0], self.shape[1]
        add_data = [[self.data[i][j] + other.data[i][j] for j in range(0, col_num)] for i in range(0, row_num)]
        return Matrix(add_data)

    @lru_cache(maxsize=None)
    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError(
                f"shapes {self.shape} and {other.shape} not aligned: {self.shape[1]} (dim 1) != {other.shape[0]} (dim 0)")
        row_num_self, col_num_self = self.shape[0], self.shape[1]
        col_num_other = other.shape[1]
        matmul_data = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(0, col_num_self)) for j in range(0, col_num_other)]
            for i in range(0, row_num_self)]
        return Matrix(matmul_data)

    def __str__(self):
        return str("[" + '\n'.join(map(str, self.data)) + "]")

    def save(self, filename):
        file = open(filename, "w")
        file.write(self.__str__())
        file.close()

if __name__ == "__main__":
    np.random.seed(0)
    matrix1_data = np.random.randint(0, 10, (10, 10)).tolist()
    matrix2_data = np.random.randint(0, 10, (10, 10)).tolist()

    m1 = Matrix(matrix1_data)
    m2 = Matrix(matrix2_data)

    add_result = m1 + m2
    with open('artifacts/matrix+.txt', 'w') as f:
        f.write(str(add_result))

    mul_result = m1 * m2
    with open('artifacts/matrix*.txt', 'w') as f:
        f.write(str(mul_result))

    matmul_result = m1 @ m2
    with open('artifacts/matrix@.txt', 'w') as f:
        f.write(str(matmul_result))

    A = Matrix([[0, 0], [0, 1e9 + 7]])
    B = Matrix([[1, 2], [3, 4]])
    C = Matrix([[0, 0], [0, 0]])
    D = Matrix([[1, 2], [3, 4]])
    A.save('artifacts/A.txt')
    B.save('artifacts/B.txt')
    C.save('artifacts/C.txt')
    D.save('artifacts/D.txt')
    AB = A @ B
    AB.save('artifacts/AB.txt')
    CD = C @ D
    CD.save('artifacts/CD.txt')

    file = open('artifacts/hash.txt', "w")
    file.write(str(hash(AB)) + " " + str(hash(CD)))
    file.close()


