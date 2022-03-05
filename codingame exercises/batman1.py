import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
primeira = True
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if 'U' in bomb_dir:
        ymax = y0
        if primeira:
            ymin = 0
        y0 = y0 - (ymax - ymin)//2

    if 'D' in bomb_dir:
        ymin = y0
        if primeira:
            ymax = h
        y0 = y0 + (ymax - ymin)//2

    if 'R' in bomb_dir:
        xmin = x0
        if primeira:
            xmax = w
        x0 = x0 + (xmax - xmin)//2
    
    if 'L' in bomb_dir:
        xmax = x0
        if primeira:
            xmin = 0
        x0 = x0 - (xmax - xmin)//2

    primeira = False
    # the location of the next window Batman should jump to.
    print(x0,y0)