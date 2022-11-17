from .poly import *

print("Amicus Plato sed...")

for p in Plato5:
    v = p()
    e = edges(v)
    f = faces(e)
    print(f"{p.__doc__.split()[0]}:\t{v.shape[0]} - {e.shape[0]} + {f.shape[0]} = {v.shape[0] - e.shape[0] + f.shape[0]}")
