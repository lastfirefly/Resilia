#Crie duas listas de tamanho igual com valores numéricos de sua escolha;

lista1 = [1,2,3,4,6,7]

lista2 = [5,10,15,20,25,30]

#Crie uma nova lista vazia para armazenar a fusão das duas primeiras;

listaFusao = []

# Determinar o tamanho da lista menor
tamanho_menor = min(len(lista1), len(lista2))


#Utilize um laço de repetição para percorrer todos os índices das listas originais;


for indice in range(len(lista1)):
    elemento_lista1 = lista1[indice]
    elemento_lista2 = lista2[indice]
    #Para cada índice, adicione o elemento da primeira lista na nova lista e, em seguida, adicione o elemento correspondente da segunda lista na nova lista;
    listaFusao.append(elemento_lista1)
    listaFusao.append(elemento_lista2)


#Se as listas originais possuem tamanhos diferentes, adicione os elementos restantes da lista maior no final da nova lista;
# Adicionar elementos restantes da lista maior
if len(lista1) > len(lista2):
    listaFusao.extend(lista1[tamanho_menor:])
else:
    listaFusao.extend(lista2[tamanho_menor:])


# Imprimindo a nova lista combinada
print(listaFusao)