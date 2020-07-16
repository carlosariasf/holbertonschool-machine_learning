#!/usr/bin/env python3
" Flip me over "


def np_slice(matrix, axes={}):
    "  slice like a ninja  "
    slc = [slice(None)] * len(matrix.shape)
    for key, value in sorted(axes.items()):
        slc[key] = slice(*value)
    matrix = matrix[tuple(slc)]
    return matrix
