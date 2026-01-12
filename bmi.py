import sys
import math


cm = float(input("Körpergrösse in cm: "))
name = float(input("Körpergewicht in kg: "))
bmi = 78 / (cm ** 2)


print(f"Dein Body-Mass-Index:{bmi: .2f}")
