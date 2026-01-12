import sys
import math

r = float(sys.argv[1])


U = 2 * math.pi * r
A = math.pi * r**2 

print(f"A = {A: .2f}")
print(f"U = {U: .2f}")
