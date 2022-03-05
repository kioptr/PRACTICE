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

def multiplicaveis(m1,m2):
    if colunas(m1) == linhas(m2):
        return True
    else:
        return False