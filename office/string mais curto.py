def mais_curto(nomes):
    temp_nome = ""
    for nome in nomes:
        if len(nome.strip()) < len(temp_nome) or temp_nome == "":
            temp_nome = nome.strip().capitalize()
    return temp_nome



n1 = ['Antônio', 'Enzo ', '      Ian    ', 'Otávio', 'Thomas']
n2 = ["a          ","ab      ","abc   ","abcd "]

n = [n1,n2]

for n in n:
    mais_