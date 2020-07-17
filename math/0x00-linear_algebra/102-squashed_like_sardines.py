#!/usr/bin/env python3
" Flip me over "


def cat_matrices(mat1, mat2, axis=0):
    " The Whole Barn  "
    shape1, shape2 = recur(mat1), recur(mat2)
    if len(shape1) != len(shape2) and shape1 != shape2:
        return None
    if axis == 0:
        arr = mat1 + mat2
    else:
        arr = cat_matrices2D(mat1, mat2, axis)
    return arr


def recur(matrix):
    " shape "
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + recur(matrix[0])


def matrix_transpose(matrix):
    " Shape of matrix "
    arr = [[matrix[j][i] for j in range(len(matrix))]
           for i in range(len(matrix[0]))]
    return arr


def cat_matrices2D(mat1, mat2, axis=0):
    " Howdy Partner "
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        arr = mat1 + mat2
    elif axis == 1 and len(mat1) == len(mat2):
        arr = [x+y for x, y in zip(mat1, mat2)]
    else:
        return None
    return arr
