#!/usr/bin/env python3
" Flip me over "


def cat_matrices(mat1, mat2, axis=0):
    " The Whole Barn  "
    shape1, shape2 = recur(mat1), recur(mat2)
    if len(shape1) != len(shape2):
        return None
    if len(recur(mat1)) > 1:
        arr = [map(sum, zip(*t)) for t in zip(mat1, mat2)]
    else:
        arr = [mat1[i] + mat2[i] for i in range(len(mat1))]
    return arr


def recur(matrix):
    " shape "
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + recur(matrix[0])
