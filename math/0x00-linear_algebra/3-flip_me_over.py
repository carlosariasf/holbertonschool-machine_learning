#!/usr/bin/env python3
" Flip me over "


def matrix_transpose(matrix):
    " Shape of matrix "
    arr = []
    for j in range(len(matrix)):
        if j >= len(matrix[0]):
            break
        arr.append([])
        for i in range(len(matrix)):
            arr[j] += [matrix[i][j]]
            if i == len(matrix) - 1:
                break
    return arr
