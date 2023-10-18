#Crie duas listas de tamanho igual com valores numéricos de sua escolha;

lista1 = [1,2,3,4,6,7]

#Declare uma variável para armazenar a soma dos valores da lista;

somatorio = lista1[indice]

somaLista = []



#Utilize um laço de repetição para percorrer todos os elementos da lista e ir somando seus valores na variável criada no passo anterior;

for indice in range(len(lista1)):
    elemento_lista1 = lista1[indice]
    #Para cada índice, adicione o elemento da primeira lista na nova lista e, em seguida, adicione o elemento correspondente da segunda lista na nova lista;
    somaLista.append(elemento_lista1)


#Se as listas originais possuem tamanhos diferentes, adicione os elementos restantes da lista maior no final da nova lista;
# Adicionar elementos restantes da lista maior
if len(lista1) > len(lista2):
    listaFusao.extend(lista1[tamanho_menor:])
else:
    listaFusao.extend(lista2[tamanho_menor:])


# Imprimindo a nova lista combinada
print(listaFusao)