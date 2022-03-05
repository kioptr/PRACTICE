def cria_matriz(num_linhas,num_colunas):
    
    matriz = []
    
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)
        
    return matriz


def multiplicacao(m1,m2):
    m3 = cria_matriz(len(m1),len(m2[0]))
    a = 0
    b = 0
    c = 0
    for linha in m3:
        for item in linha:
            for i in m1[0]:
                m3[a][b] += m1[a][c] * m2[c][b]
                c += 1
            b += 1
            c = 0
        a += 1
        b = 0
    return m3