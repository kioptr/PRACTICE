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

import time
import ordenar_lista
import random

a = random.sample(range(0, 1000), 1000)

def test_eficiencia(tipo_ordenador):
    antes = time.time()
    tipo_ordenador(a[:])
    depois = time.time()
    return (depois - antes)
        
"""NÚMERO DE ITERAÇÕES"""

iteracoes = 2

print(
"\n",
test_eficiencia(ordenar_lista.direta),
"\n",
test_eficiencia(ordenar_lista.bubble),
"\n",
test_eficiencia(ordenar_lista.insercao),
"\n",
test_eficiencia(ordenar_lista.insertion_sort)
)

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

funcao(arranjo, 0.83*list_size)