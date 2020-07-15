#!/usr/bin/env python3
" Flip me over "


def matrix_transpose(matrix):
    " Shape of matrix "
    arr = [[matrix[j][i] for j in len(matrix)]
           for i in range(len(matrix[0]))]
    return arr
