import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
    """
    Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

    :param dense_matrix: 2D list representing a dense matrix
    :return: A tuple containing (values array, column indices array, row pointer array)
    """
    A = np.array(dense_matrix)

    rows, cols = np.nonzero(A)
    values = A[rows, cols]

    counts = np.count_nonzero(A, axis=1)
    row_ptr = np.concatenate(([0], np.cumsum(counts)))

    return values.tolist(), cols.tolist(), row_ptr.tolist()

