#Escreva um programa em Python que exiba o desconto do INSS segundo seu salário. Por exemplo, se o usuário possuir salário inferior ou igual a R$: 600,00 ele será isento, em caso de maior que R$: 600,00 e menor ou igual a R$:1.200,00, o desconto é de 20%; em caso de Maior que R$: 1.200,00 e menor ou igual a R$: 2.000,00, o desconto é de 25%; e em caso de maior que R$: 2.000,00, o desconto é de 30%.

salario = float(input("Informe seu salário: "))
# Inicializar a variável que armazenará o cálculo do desconto


def inss():
    descontoinss = 0
    # Verificar em qual faixa de salário o usuário se encaixa e calcular o desconto do INSS
    if salario <= 600.00:
        descontoINSS = 0.0
        if salario <= 1200.00:
            descontoINSS = (salario) * 0.20
            if salario <= 2000.00:
                descontoINSS = (salario) * 0.25
    else:
        descontoINSS = (salario) * 0.30
        
    print(f"O desconto do INSS para um salário de R$ {salario:.2f} é de R$ {descontoinss:.2f}")

# Exibir o valor do desconto do INSS para o usuário
inss()