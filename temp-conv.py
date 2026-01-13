#!/usr/bin/env python3
import sys

a = float(sys.argv[1])
b = (sys.argv[2])


if b == 'C' or b == 'c':
	temp = a * (9/5) + 32
	print(f"{a}°C = {temp: .2f}°F")
	
elif b == 'F' or b == 'f':
	temp = (a-32) * (5/9)
	print(f"{a}°F = {temp: .2f}°C")

else:
	print("Error")
