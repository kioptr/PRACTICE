def main():
    Jett = Valorant('Jett', 24, 'wind')
    Brimstone = Valorant('Brimstone', 54, 'sandstorm')
    Viper = Valorant('Viper', 35, 'poison')
    
    Viper.envelhecer(10)

class Valorant:
    def __init__(self,nome,idade,habilidade):
        self.nome       = nome
        self.idade      = idade
        self.habilidade = habilidade
        
    def imprima(self):
        print(self.nome+'; Idade:',self.idade,"; Habilidade: ",self.habilidade)
    
    def envelhecer(self,anos):
        self.idade += anos
        self.imprima()

main()