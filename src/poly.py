import itertools
import numpy as np


GR = (1 + 5 ** 0.5) / 2


def p4():
    """Tetrahedron vertices"""
    return np.vstack((np.eye(3), np.ones(3)))


def p6():
    """Cube vertices"""
    return np.array([*itertools.product(range(2), repeat=3)], float) * 2 - 1


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


Plato5 = [p4, p6, p8, p12, p20]


def edges(vertices):
    D = np.triu(np.linalg.norm(vertices[None] - vertices[:, None], axis=-1), 1)
    return np.array(np.nonzero(abs(D - D[0, 1:].min()) < 1e-3)).T


def faces_gen(edges):
    """Compute faces for edges"""
    Es = {}
    for a, b in edges:
        if a not in Es:
            Es[a] = []
        Es[a].append(b)
        if b not in Es:
            Es[b] = []
        Es[b].append(a)

    E = len(edges)
    V = len(Es)
    F = E - V + 2
    # Face's size
    Fi = 2 * E // F

    face = []

    def add(v):
        """
        Append a vertex to a face up to Vi ones
        """
        face.append(v)
        if len(face) >= Fi:
            if v > face[1] and face[0] in Es[v]:
                yield face[:]
        else:
            for z in Es[face[-1]]:
                if z > face[0]:
                    yield from add(z)
        face.pop()

    for v in Es.keys():
        yield from add(v)


def faces(edges):
    """Compute faces for edges"""
    return np.array([*faces_gen(edges)])
