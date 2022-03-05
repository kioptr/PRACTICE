"""
This program reads 2 user entries (lines and columns),
and creates a matching matrix in which each value will
equate to the sum of the squares of it's line's and column's indexes.
e.g.:
    2 and 3:
        [[0,1,4]
         [1,2,5]]
"""

import numpy as np

a = int(input("Digite o número de linhas: "))
b = int(input("Digite o número de colunas: "))

d = np.arange(a*b).reshape(a,b)

def soma_quadrados(indice1,indice2):
    """function that sums the squares of 2 entry values """
    return indice1 ** 2 + indice2 ** 2

LINHA = 0
COLUNA = 0

for i in d:
    for j in i:
        d[LINHA][COLUNA] = soma_quadrados(LINHA,COLUNA)
        COLUNA = COLUNA + 1
    COLUNA = 0
    LINHA = LINHA + 1

print()
print(np.array(d))
