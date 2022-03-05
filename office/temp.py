def cria_matriz(num_i,num_j):
    
    matriz = []
    
    for i in range(num_i):
        coluna = 0
        linha = []
        for j in range(num_j):
            linha.append(int(input("Linha: ",i,"Coluna: "" - ")))