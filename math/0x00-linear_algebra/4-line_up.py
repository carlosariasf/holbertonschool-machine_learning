#!/usr/bin/env python3
" Flip me over "


def add_arrays(arr1, arr2):
    " Shape of matrix "
    if len(arr1) != len(arr2):
        return None
    arr = [arr1[i] + arr2[i] for i in range(len(arr1))]
    return arr
