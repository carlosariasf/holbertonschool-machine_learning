#!/usr/bin/env python3
" Flip me over "


def mat_mul(mat1, mat2):
    " Ridin’ Bareback "
    if len(mat1[0]) == len(mat2):
        arr = [[sum(x*y for x, y in zip(mat1c, mat2c)) for mat2c in zip(*mat2)]
               for mat1c in mat1]
        return arr
    return None
