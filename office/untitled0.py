import time

def pesquisa_linear_index(arranjo, item):
    try:
        return arranjo.index(item)
    except ValueError:
        return -1
    



def pesquisa_linear_in(arranjo, item):
    for i in range(len(arranjo)):
        if arranjo[i] == item:
            return i
    return -1



def pesquisa_binaria(arranjo, item):
    esquerda, direita = 0, len(arranjo) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arranjo[meio] == item:
            return meio
        elif arranjo[meio] > item:
            direita = meio - 1
        else: esquerda = meio + 1
    return -1

"""TAMANHO DA LISTA"""
list_size = 10**7
arranjo = list(range(1, list_size))


def testa_tempo(funcao):
    antes = time.time()
    funcao
    return time.time() - antes



pesquisa_linear_index(arranjo, 0.83*list_size)

pesquisa_linear_in(arranjo, 0.83*list_size)

# funcao(arranjo, 0.83*list_size)