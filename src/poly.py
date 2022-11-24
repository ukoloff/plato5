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
        a = int(a)
        b = int(b)
        if a not in Es:
            Es[a] = set()
        Es[a].add(b)
        if b not in Es:
            Es[b] = set()
        Es[b].add(a)

    E = len(edges)
    V = len(Es)
    F = E - V + 2
    # Face's size
    Fi = 2 * E // F

    face = []
    faceset = set()

    def add(v):
        """
        Append a vertex to a face up to Vi ones
        """
        face.append(v)
        faceset.add(v)
        if len(face) < Fi:
            for z in Es[face[-1]]:
                if z > face[0] and z not in faceset:
                    yield from add(z)
        elif v > face[1] and face[0] in Es[v]:
            yield face[:]
        face.pop()
        faceset.remove(v)

    for v in Es.keys():
        yield from add(v)


def faces(edges):
    """Compute faces for edges"""
    return np.array([*faces_gen(edges)])


class Poly:
    def __init__(self, N: int):
        p = Plato5[N]
        self.name = p.__doc__.split()[0]
        self.v = v = p()
        self.e = e = edges(v)
        self.f = faces(e)
        self.scale()

    def scale(self):
        self.v -= self.v.mean(axis=0)
        self.v /= np.linalg.norm(self.v, axis=-1).max()

    def __str__(self):
        return f"""{self.name}:\t{
            self.v.shape[0]} - {self.e.shape[0]} + {self.f.shape[0]} = {
            self.v.shape[0] - self.e.shape[0]+ self.f.shape[0]
            }"""

    def edge1(self):
        """Make all edges of length=1"""
        self.v /= np.linalg.norm(self.v[1:] - self.v[0], axis=-1).min()

    def as_model(self, file):
        print(self.v.shape[0], file=file)
        print(self.e.shape[0], file=file)
        print(self.f.shape[0], file=file)
        for p in self.v:
            print(*p, file=file)
        for p in self.e:
            print(*p, file=file)
        for p in self.f:
            print(*p, file=file)

if __name__ == '__main__':
    for i in range(5):
        x = Poly(i)
        with open(f"{x.name}R1.txt", "w") as f:
            x.as_model(f)
        x.edge1()
        with open(f"{x.name}E1.txt", "w") as f:
            x.as_model(f)
