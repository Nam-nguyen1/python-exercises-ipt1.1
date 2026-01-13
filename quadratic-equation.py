#!/usr/bin/env python3

import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
d = b**2 - (4*a*c)


if d == 0:
	x = -b / (2*a)
	print(f"x = {x:.1f}")

elif d > 0:
	x1 = ((0-b) + (math.sqrt(d))) / (2*a)
	x2 = ((0-b) - (math.sqrt(d))) / (2*a)
	print(f"x1={x1:.1f}, x2={x2:.1f}")
else:
	print("keine lösung")
