def cria_matriz(num_linhas,num_colunas):
    
    matriz = []
    
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            print("Linha: ",i,"Coluna: ",j," - ")
            linha.append(int(input()))
        matriz.append(linha)
        
    for i in matriz:
        print(i)
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
    
    print(str(linhas(matriz))+"X"+str(colunas(matriz)))
    
    
    