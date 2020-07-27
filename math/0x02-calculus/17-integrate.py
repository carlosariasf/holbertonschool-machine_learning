#!/usr/bin/env python3
''' integral '''


def poly_integral(poly, C=0):
    ''' integral function '''
    if not isinstance(poly, list) or len(poly) == 0 or not isinstance(C, int):
        return None
    elif poly == [0]:
        return [C]
    else:
        return [C] + list(map(type_n,
                              [poly[x]/(x + 1) for x in range(len(poly))]))


def type_n(x):
    ''' type'''
    return int(x) if x.is_integer() else x
