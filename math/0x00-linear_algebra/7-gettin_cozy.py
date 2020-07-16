#!/usr/bin/env python3
" Flip me over "


def cat_matrices2D(mat1, mat2, axis=0):
    " Howdy Partner "
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        arr = mat1 + mat2
    elif axis == 1 and len(mat1) == len(mat2):
        arr = [x+y for x, y in zip(mat1, mat2)]
    else:
        return None
    return arr
