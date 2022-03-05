def maiusculas(frase):
    pos = 0
    frase1 = ""
    while pos <= len(frase) - 1:
        if frase[pos] >= "A" and frase[pos] <= "Z":
            frase1 += frase[pos]
        pos += 1
    return frase1

print(maiusculas("teste"))
print(maiusculas("o ovo do avestruz"))
print(maiusculas("A CASA MUITO ENGRAÇADA"))
print(maiusculas("A TELEvisão queBROU"))
print(maiusculas("A Vaca Amarela"))