# idade = input("Insira a idade: ")

# def dirigirOuBeber(idade):
  
#     # Verifica se a idade é um número inteiro
#     if type(idade) == int:
#         # Compara a idade com 18
#         if idade >= 18:
#             # Retorna a mensagem para quem pode dirigir e beber
#             return "Já pode dirigir ou beber"
#         else:
#             # Retorna a mensagem para quem não pode dirigir nem beber
#             return "Não pode nem dirigir nem beber"
#     else:
#         # Retorna uma mensagem de erro se a idade não for um número inteiro
#         return "Idade inválida"


# print(dirigirOuBeber(idade))

# Suponha que você tenha dicionários de perguntas e respostas
questoes = {
    1: "Qual é a capital do Brasil?",
    2: "Quem escreveu 'Dom Quixote'?",
    3: "Qual é o maior planeta do sistema solar?"
}

respostas = {
    1: "a) Brasília",
    2: "b) Miguel de Cervantes",
    3: "c) Júpiter"
}

# Itere sobre as chaves das perguntas
for pk in questoes.keys():
    # Imprima a pergunta
    print(f'{pk}: {questoes[pk]}')
    
    # Verifique se há uma resposta correspondente
    if pk in respostas:
        # Imprima a resposta
        print(respostas[pk])

    # Aguarde a entrada do usuário antes de prosseguir para a próxima pergunta
    input("Pressione Enter para continuar...")

# Você pode personalizar a lógica de entrada para avançar apenas quando o usuário estiver pronto.
