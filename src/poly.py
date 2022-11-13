import itertools
import numpy as np


def p4():
    """Tetrahedron vertices"""
    return np.vstack((np.eye(3), np.ones(3)))


def p6():
    """Cube vertices"""
    return np.array([*itertools.product(range(2), repeat=3)]) * 2 - 1

def p8():
    """Octahedron vertices"""
    return np.vstack((np.eye(3), -np.eye(3)))
