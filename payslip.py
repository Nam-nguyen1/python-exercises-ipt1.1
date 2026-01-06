import sys



brutto = float(sys.argv[1])

AHV = brutto * 0.087
IV = brutto * 0.014
EO = brutto * 0.005
ALV = brutto * 0.011
NBU = brutto * 0.0073
PK = brutto * 8.9

nettolohn = brutto - AHV - IV - EO - ALV - NBU - PK


print(f"{Nettolohn}")
