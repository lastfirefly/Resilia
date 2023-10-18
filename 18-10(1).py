class Animal:
    def __init__(self, nome, som, objeto):
        self.nome = nome
        self.som = som
        self.objeto = objeto

    def falar(self):
        print(f"\n{self.nome} fez '{self.som}'\n")

    def comer(self):
        print(f'\n{self.nome} comeu\n')

    def brinquedo(self):
        print(f'\n{self.nome} brincou com {self.objeto}\n')


nome = str(input("Nome: "))
som = "auau"
dataNasc = str(input("Data de nascimento: "))
objeto = str(input("Qual brinquedo preferido? "))

# Crie um objeto "animal" a partir da classe "Animal" e defina um nome para ele;
animal1 = Animal(nome,som,objeto)


while True:
    
    acao = input("Escolha uma ação: \n[1]-Latir\n[2]-Comer\n[3]-Brincar")

    if acao == "1":
        animal1.falar()
    elif acao == "2":
        animal1.comer()
    elif acao == "3":
        animal1.brinquedo()
    else:
        print(f"\n{nome} fainted\n")
        False
        break