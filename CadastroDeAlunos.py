class Aluno:
    
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
   
        
nome = str(input("Nome do aluno: "))
idade = float(input("Idade: "))
matricula = int(input("Matricula: "))


aluno1 = Aluno(nome, idade, matricula)

print("Nome:",aluno1.nome,"Idade:", aluno1.idade, "Matrícula:", aluno1.matricula)