#!/usr/bin/env python3
''' integral '''


def poly_integral(poly, C=0):
    ''' integral function '''
    if not isinstance(poly, list) or len(poly) == 0 or not isinstance(C, int):
        return None
    intl = [C] + [poly[x]/(x + 1) for x in range(len(poly))]
    return intl
