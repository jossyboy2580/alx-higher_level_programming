#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, row)))
    return new_matrix

if __name__ == "__main__":
    square_matrix_simple(matrix)
