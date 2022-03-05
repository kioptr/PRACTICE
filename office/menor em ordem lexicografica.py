def menor_string(string):
    menor = ""
    for caso in string:
        if caso.lower() < menor or menor == "":
            menor = caso
    return menor

n1 = ['Antônio', 'Enzo ', '      Ian    ', 'Otávio', 'Thomas']
n2 = ['AAAAAA', 'b']
n3 = ['oĺá', 'A', 'a', 'casa']

print(menor_string(n2))