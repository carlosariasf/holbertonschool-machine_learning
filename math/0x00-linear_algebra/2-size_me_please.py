#!/usr/bin/env python3
" Size me please "


def matrix_shape(matrix):
    " Shape of matrix "
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])
