# Crie uma tupla com 5 elementos de sua escolha;
tup = (1,2,3,4,5)

# Utilize a função len() para imprimir na tela o tamanho da tupla;
print (len(tup))

# Crie uma nova tupla que contenha os elementos da tupla original em ordem reversa, utilizando o fatiamento com parâmetro -1;

nwTup = tup[::-1]
print(nwTup)

# Utilize o método join() para imprimir na tela os elementos da nova tupla, separados por ""-"".

separador = "-".join(str(nwTup))

print(separador)
