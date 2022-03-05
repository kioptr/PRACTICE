def cria_matriz(num_linhas,num_colunas):
    
    matriz = []
    
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(j)
        matriz.append(linha)
        
    return matriz


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
    
    return(str(linhas(matriz))+"X"+str(colunas(matriz)))


def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):
        
        m3 = cria_matriz(linhas(m1),colunas(m1))
        
        contador_linha = 0
        for i in m3:
            contador_coluna = 0
            for j in i:
                m3[contador_linha][contador_coluna] = m1[contador_linha][contador_coluna] + m2[contador_linha][contador_coluna]
                contador_coluna = contador_coluna + 1
            contador_linha = contador_linha + 1
        return m3
    
    else:
        return False