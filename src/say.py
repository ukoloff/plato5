from .poly import *

print("Amicus Plato...")

for p in Plato5:
    print(p.__doc__)
    v = p()
    print(v)
