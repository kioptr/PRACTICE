def menor_string(string):
    menor = ""
    for caso in string:
        if caso.lower().strip() < menor or menor == "":
            menor = caso.lower().strip()
    return menor

n1 = ['Antônio', 'Enzo ', '      Ian    ', 'Otávio', 'Thomas']
print(menor_string(n1))



def teste_menor_string(string,resposta):
    if menor_string(string) == resposta:
        print("ok para esse caso")
    else:
        print("BAAAAAD para esse caso")



n1 = ['Antônio', 'Enzo ', '      Ian    ', 'Otávio', 'Thomas']
n2 = ["a          ","ab      ","abc   ","abcd "]
n3 = ["advark","bola","joção","  new        "]


teste_menor_string(n1,"antônio")
teste_menor_string(n2,"a")
teste_menor_string(n3,"advark")