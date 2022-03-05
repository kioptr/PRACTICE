import numpy as np

a = int(input("Digite o número de linhas: "))
b = int(input("Digite o número de colunas: "))

A = np.empty((a,b))

def f(x,y):
    return x**2+y**2

i=0
j=0

while i < a:
    while j < b:
        A[i][j] = f(i,j)
        j = j + 1
    i = i + 1