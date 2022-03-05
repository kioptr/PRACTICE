def conta_letras(frase, contar="vogais"):
    vogais = 0
    for letra in frase:
        if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
            vogais += 1
    if contar == "vogais":
        return vogais
    if contar == "consoantes":
        return len(frase) - vogais