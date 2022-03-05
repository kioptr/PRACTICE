import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
matriz = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    matriz.append(line)
for linha in range(height):
    for coluna in range(width):
        if matriz[linha][coluna] == '0':
            x1,y1 = coluna,linha
            if '0' in matriz[linha][coluna + 1:]:
                xy,y2 = matriz[linha][coluna + 1:].index('0'),linha
            else:
                x2,y2 = -1,-1
            if '0' in matriz[linha + 1:][coluna]:
                xy,y2 = matriz[linha][coluna + 1:].index('0'),linha
            else:
                x2,y2 = -1,-1

            # if '0' in matriz[linha][coluna + 1:]

                
# Three coordinates: a node, its right neighbor, its bottom neighbor
print("0 0 1 0 0 1")
