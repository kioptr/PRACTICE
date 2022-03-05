import numpy as np

def quadratic_intersections(p, q):
    """Given two quadratics p and q, determines the points of intersection"""
    x = np.roots(np.asarray(p) - np.asarray(q))
    y = np.polyval(p, x)
    return x, y