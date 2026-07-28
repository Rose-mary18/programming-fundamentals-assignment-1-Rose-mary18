# Function to read a matrix
from typing import List


def read_matrix(rows: int, cols: int) -> List[List[int]]:
    """Read a matrix of given dimensions from stdin."""
    matrix: List[List[int]] = []
    for i in range(rows):
        values = list(map(int, input(f"Enter row {i + 1}: ").split()))
        # If user provides fewer or more values than expected, adjust/truncate
        if len(values) < cols:
            # pad with zeros
            values += [0] * (cols - len(values))
        elif len(values) > cols:
            values = values[:cols]
        matrix.append(values)
    return matrix


# Function to display a matrix
def display_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


# Part A: Transpose a matrix
def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0

    transpose: List[List[int]] = []
    for j in range(cols):
        new_row: List[int] = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


# Part B: Add two matrices
def add_matrices(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    rows = len(matrix1)
    cols = len(matrix1[0]) if rows else 0

    result: List[List[int]] = []
    for i in range(rows):
        row: List[int] = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# Part C: Multiply two matrices
def multiply_matrices(matrixA: List[List[int]], matrixB: List[List[int]]) -> List[List[int]]:
    rowsA = len(matrixA)
    colsA = len(matrixA[0]) if rowsA else 0
    colsB = len(matrixB[0]) if matrixB else 0

    result: List[List[int]] = []

    for i in range(rowsA):
        row: List[int] = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matrixA[i][k] * matrixB[k][j]
            row.append(total)
        result.append(row)

    return result


# ---------------- Main Program ----------------

if __name__ == "__main__":
    # Part A
    print("PART A - Transpose Matrix")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    print("\nTransposed Matrix:")
    display_matrix(transpose_matrix(matrix))

    # Part B
    print("\nPART B - Add Two Matrices")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter Matrix 1:")
    matrix1 = read_matrix(rows, cols)

    print("Enter Matrix 2:")
    matrix2 = read_matrix(rows, cols)

    print("\nSum of Matrices:")
    display_matrix(add_matrices(matrix1, matrix2))

    # Part C
    print("\nPART C - Multiply Two Matrices")

    rowsA = int(input("Enter rows of Matrix A: "))
    colsA = int(input("Enter columns of Matrix A: "))

    print("Enter Matrix A:")
    matrixA = read_matrix(rowsA, colsA)

    rowsB = int(input("Enter rows of Matrix B: "))
    colsB = int(input("Enter columns of Matrix B: "))

    if colsA != rowsB:
        print("Matrix multiplication is not possible.")
    else:
        print("Enter Matrix B:")
        matrixB = read_matrix(rowsB, colsB)

        print("\nProduct of Matrices:")
        display_matrix(multiply_matrices(matrixA, matrixB))
