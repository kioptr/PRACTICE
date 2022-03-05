import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

MENOR = 6000

n = int(input())
if n != 0:    
    for i in input().split():
        t = int(i)
        
        if abs(t) < abs(MENOR):
            b = t
        
        if abs(t) == abs(MENOR):
            if t > MENOR:
                b = t
            else:
                b = MENOR
        
        MENOR = b

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(MENOR)
else:
    print(0)