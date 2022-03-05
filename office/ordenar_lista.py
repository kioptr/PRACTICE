def direta(lista):
    
    fim = len(lista)    
    for i in range(fim - 1):
        posicao_do_minimo = i        
        for j in range(i+1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo= j
        
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]


def bubble(lista):
    
    fim = len(lista)
    for i in range(fim-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def insercao(lista):
    
    for i in range(1, len(lista)):
        n = 0
        for j in range(1, i + 1):
            if lista[i] < lista[i - j]:
                n += 1
                
        if n > 0:
            temp = lista[i]
            lista[i-n +1: i +1] = lista[i-n: i]
            lista[i-n] = temp

def insertion_sort(lista):
  for i in range( 1, len( lista ) ):
    chave = lista[i]
    k = i
    while k > 0 and chave < lista[k - 1]:
        lista[k] = lista[k - 1]
        k -= 1
    lista[k] = chave