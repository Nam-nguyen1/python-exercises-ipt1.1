import sys
import math

sek = int(sys.argv[1])
rests = sek % 60
min = sek // 60
restm = min % 60
h = min // 60

print(f"{h}h{restm}m{rests}s")
