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

Plato5 = [p4, p6, p8, p12, p20]

def faces(n: int, vertices):
  """Compute (n-fold) faces for vertices"""
  for vs in itertools.permutations(range(len(vertices)), n):
    if vs[0] != min(vs) or vs[1] > vs[-1]:
      continue
    pts = vertices[list(vs)]
    edges = pts - np.roll(pts, 1, axis=0)
    ls = np.linalg.norm(edges, axis=1)
    if ls.max() > ls.min() * 1.001:
      continue
    if np.linalg.matrix_rank(edges) > 2:
      continue
    yield vs

def edges(vertices):
  D = np.triu(np.linalg.norm(vertices[None] - vertices[:, None], axis=-1), 1)
  return np.array(np.nonzero(abs(D - D[0, 1:].min()) < 1e-3)).T
