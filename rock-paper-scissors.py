#!/usr/bin/env python3

import sys
import random

computer = random.randint(0, 2)

match computer:
	case 0:
		cm = "Paper"
	case 1:
		cm = "Rock"
	case 2: 
		cm = "Scissors"

Spieler = sys.argv[1]

match Spieler:
	case "paper":
		pm = 0
	case "rock":
		pm = 1
	case "scissors":
		pm = 2

Result = (pm - computer) %3

if Result == 0:
	print(f"Spieler: {cm}")
	print(f"Computer: {cm}")
	print("Unentschiedet")


elif Result == 2:
	print(f"Spieler: {Spieler}")
	print(f"Computer: {cm}")
	print("Der Spieler gewinnt!")

elif Result == 1:
	print(f"Spieler: {Spieler}")
	print(f"Computer: {cm}")
	print("Der Computer gewinnt!")
