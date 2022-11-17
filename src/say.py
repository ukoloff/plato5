from .poly import *

print("Amicus Plato...")

for p in Plato5:
    print(p.__doc__)
    v = p()
    print(v)
    e = edges(v)
    print(e.T)
    f = faces(e)
    print(*f)
