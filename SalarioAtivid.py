# 1- Definir Valores Iniciais
salarioMinimo = 1320

#1.2 solicite o valor para teste
salarioFuncionario = float(input("Qual salário para calcular?"))


# 2- Calcular quantos salários mínimos tem em um valor X

qntSalMin = salarioFuncionario / salarioMinimo

# 3- Resultado do calculo total de reajuste

print("O funcionário que recebe R$", salarioFuncionario, 
      "recebe valor equivalente a", round(qntSalMin), "salário(s) minimo(s)")