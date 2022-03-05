def mais_curto(nomes):
    temp_nome = ""
    temp_nome1 = ""
    for nome in nomes:
        if len(nome) < len(temp_nome) or temp_nome == "":
            temp_nome = nome.capitalize()
        elif len(temp_nome) == len(nome):
            if temp_nome1 == "":
                temp_nome1 = temp_nome + " - " + nome.capitalize()
            else 
    if temp_nome1 == "":
        return temp_nome
    else:
        return temp_nome1
mais_curto(["Alexandre","Eduardo","Henrique","Murilo","Theo","André","Enrico","Henry","Nathan","Thiago","Antônio","Enzo","Otávio","Thomas","Augusto","Erick","Isaac","Pietro","Vicente","Breno","Felipe","João","Rafael","Vinícius","Bruno","Fernando","Kaique","Raul","Vitor","Caio","Francisco","Leonardo","Rian","Yago","Cauã","Frederico","Luan","Ricardo","Ygor","Daniel","Guilherme","Lucas","Rodrigo","Yuri","Danilo","Gustavo","Mathias","Samuel"])