#!/usr/bin/env python3

import sys

a = float(sys.argv[1])
b = (sys.argv[2])


match b: 
	case "USD":
		c = a * 0.8
	case "EUR":
		c = a * 0.93
	case "GBP":
		c = a * 1.07

print(f"CHF {c: .2f}")
