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