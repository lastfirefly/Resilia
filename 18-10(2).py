# Atividade: Organizando as entrevistas
# ➔ O QUE FAZER?
# Em um arquivo .py, desenvolva uma classe com os seguintes requisitos:
# 1. Tenha os atributos: idade, cidade, estado, salário atual e escolaridade
# 2. Tenha um método imprimirDados que devolva as informações do entrevistado
# em uma string com os atributos separados por vírgula (Ex: 20,Rio de
# Janeiro,RJ,1000,Ensino Médio Completo)


class Entrevista:
    def __init__(self, idade, cidade, estado, salarioAtual, escolaridade):
        self.idade = idade
        self.cidade = cidade
        self.estado = estado
        self.salarioAtual = salarioAtual
        self.escolaridade = escolaridade

    def display(self):
        print([self.idade, self.cidade, self.estado, self.salarioAtual, self.escolaridade])


candidato1 = Entrevista("25","Rio de Janeiro","RJ", "2300", "Ensino Médio Completo")
candidato2 = Entrevista("30","Rio de Janeiro","RJ", "2600", "Superior Completo")
candidato3 = Entrevista("31","Duque de Caxias","RJ", "1900", "Superior Completo")
candidato4 = Entrevista("25","Rio de Janeiro","RJ", "1600", "Ensino Fundamental Completo")

candidato3.display()
candidato4.display()
