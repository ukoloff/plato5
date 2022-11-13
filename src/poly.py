import itertools
import numpy as np


GR = (1 + 5 ** 0.5) / 2


def p4():
    """Tetrahedron vertices"""
    return np.vstack((np.eye(3), np.ones(3)))


def p6():
    """Cube vertices"""
    return np.array([*itertools.product(range(2), repeat=3)]) * 2 - 1


def p8():
    """Octahedron vertices"""
    return np.vstack((np.eye(3), -np.eye(3)))


def twelve(Y):
    """Make 12 vertices from one"""
    b = p6()[4:] * [0, Y, GR]
    return np.vstack([np.roll(b, i, axis=1) for i in range(3)])


def p12():
    """Icosahedron vertices"""
    return twelve(1)


def p20():
    """Dodecahedron vertices"""
    return np.vstack((p6(), twelve(GR-1)))
