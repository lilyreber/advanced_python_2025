import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class MatrixStr:
    def __str__(self):
        return str(self._data)


class MatrixSaveFile:
    def save(self, filename):
        file = open(filename, "w")
        file.write(self.__str__())
        file.close()


class MatrixMixins(NDArrayOperatorsMixin, MatrixSaveFile, MatrixStr):
    def __init__(self, data):
        self._data = data
        self.shape = (len(data), len(data[0] if len(data) > 0 else 0))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        new_input = [x._data for x in inputs]
        result = getattr(ufunc, method)(*new_input, **kwargs)

        if method == '__call__':
            return MatrixMixins(result)
        else:
            return result


if __name__ == "__main__":
    np.random.seed(0)
    matrix1_data = np.random.randint(0, 10, (10, 10))
    matrix2_data = np.random.randint(0, 10, (10, 10))

    m1 = MatrixMixins(matrix1_data)
    m2 = MatrixMixins(matrix2_data)

    add_result = m1 + m2
    with open('artifacts/matrix_mixins+.txt', 'w') as f:
        f.write(str(add_result))

    mul_result = m1 * m2
    with open('artifacts/matrix_mixins*.txt', 'w') as f:
        f.write(str(mul_result))

    matmul_result = m1 @ m2
    with open('artifacts/matrix_mixins@.txt', 'w') as f:
        f.write(str(matmul_result))
