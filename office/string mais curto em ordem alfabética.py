def mais_curto(nomes):
    temp_nome = ""
    for nome in nomes:
        if len(nome.strip()) < len(temp_nome) or temp_nome == "":
            temp_nome = nome.strip().capitalize()
    return temp_nome



def mais_curto_teste(indice,nomes,resposta):
    if mais_curto(nomes) == resposta:
        print("ok para ",indice)
    else:
        print("BAAAAAD para",indice)



n1 = ['Antônio', 'Enzo ', '      Ian    ', 'Otávio', 'Thomas']
n2 = ["a          ","ab      ","abc   ","abcd "]
n3 = ["advark","bola","joção","  new        "]
n4 = ["a","b","c","d"]



mais_curto_teste("N1",n1,"Ian")
mais_curto_teste("N2",n2,"A")
mais_curto_teste("N3",n3,"New")
mais_curto_teste("N4",n4,"A")