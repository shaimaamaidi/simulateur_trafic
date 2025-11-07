# affichage_cython.pyx
cimport cython
import numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
def calculer_position(double x1, double y1, double x2, double y2, double L, double pos):
    print("Valeurs reçues :", x1, y1, x2, y2, L, pos)
    if L == 0.0:
        return x1, y1
    ratio = min(max(pos / L, 0), 1)
    x = x1 + ratio * (x2 - x1)
    y = y1 + ratio * (y2 - y1)
    return x, y
