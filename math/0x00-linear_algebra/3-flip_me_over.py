#!/usr/bin/env python3
" Flip me over "

import time


def matrix_transpose(matrix):
    " Shape of matrix "
    arr = []
    j = 0
    while j < len(matrix):
        arr.append([])
        for i in range(len(matrix)):
            if j >= len(matrix[i]):
                arr.pop(len(arr) - 1)
                return arr
            arr[j] += [matrix[i][j]]
            if i == len(matrix) - 1:
                j += 1
                break
    return arr
