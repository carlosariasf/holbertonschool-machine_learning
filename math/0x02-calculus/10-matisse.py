#!/usr/bin/env python3
''' Sum '''


def poly_derivative(poly):
    ''' Sum function '''
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    der = [poly[x]*x for x in range(1, len(poly))]
    return '[0]' if sum(der) == 0 else der
