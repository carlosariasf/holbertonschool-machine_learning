#!/usr/bin/env python3
" Flip me over "

import numpy as np


def np_cat(mat1, mat2, axis=0):
    "  Cat's Got Your Tongue  "
    return np.concatenate((mat1, mat2), axis)
