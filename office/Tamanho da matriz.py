def linhas(matriz):
    a = 0
    for i in matriz:
        a = a + 1
    return a
def colunas(matriz):
    b = 0
    for j in matriz[0]:
        b = b + 1
    return b

def dimensoes(matriz):
    
    print(str(linhas(matriz))+"X"+str(colunas(matriz)))