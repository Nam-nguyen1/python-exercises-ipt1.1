#!/usr/bin/env python3

import sys

letter = sys.argv[1]

match letter:
	case "a"|"i"|"o"|"u"|"e":
		print(f"'{letter}' ist ein Vokal")

	case "q"|"w"|"r"|"t"|"z"|"p"|"s"|"d"|"f"|"g"|"h"|"j"|"k"|"l"|"y"|"x"|"c"|"v"|"b"|"n"|"m":
		print(f" '{letter}' ist kein Vokal")

	case other:
		print(f" '{letter}' ist unbekannt")
