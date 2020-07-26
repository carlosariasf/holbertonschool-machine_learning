#!/usr/bin/env python3
''' Sum '''


def summation_i_squared(n):
    ''' Sum function '''
    if not isinstance(n, int):
        return None
    return sum(map(sqrt, range(1, n + 1)))


def sqrt(x):
    ''' sqrt function '''
    return (x ** 2)
