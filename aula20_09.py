  to  Everyone
# >>>> FUNÇÃO <<<<
# Em Python, uma função é definida usando a palavra-chave " def " :
# Para chamar uma função, use o nome da função seguido de parênteses
# Argumentos - As informações podem ser passadas para funções como argumentos.
# Os argumentos são especificados após o nome da função, e entre parênteses. 
# Você pode adicionar quantos argumentos quiser, basta separá-los com vírgula.

# <<< EXEMPLO 1 >>>
def my_function01():
    print("Hello from a function")

my_function01()

# <<< ==== PARÂMETRO OU ARGUMENTO? ==== >>>
# Os termos parâmetro e argumento podem ser usados ​​para a mesma coisa: 
# informações que são passadas para uma função. Da perspectiva de uma função:
# <<< EXEMPLO 2 >>>

def my_function02(fname): # Um parâmetro é a variável listada entre parênteses na definição da função.
    print(fname + " Refsnes")

my_function02("Emil") # Um argumento é o valor enviado à função quando ela é chamada.
my_function02("Tobias")
my_function02("Linus")
# <<< EXEMPLO 3 >>>
def my_function03(fname, lname): # Esta função espera 2 argumentos e obtém 2 argumentos:
    print(fname + " " + lname)
my_function03("Emil", "Refsnes")

# <<< ==== ARGUMENTO DE PALAVRAS-CHAVES ==== >>>
# Você também pode enviar argumentos com a sintaxe chave = valor .
# Desta forma, a ordem dos argumentos não importa.
# <<< EXEMPLO 4 >>>
def my_function04(child3, child2, child1):
  print("The youngest child is " + child3)
my_function04(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# <<< ==== VALOR DO PARÂMETRO PADRÃO ==== >>>
# O exemplo a seguir mostra como usar um valor de parâmetro padrão.
# Se chamarmos a função sem argumento, ela usará o valor padrão:
# <<< EXEMPLO 5 >>>
def my_function05(country = "Norway"):
  print("I am from " + country)

my_function05("Sweden")
my_function05("India")
my_function05()
my_function05("Brazil")
# <<< ==== VALOR DE RETORNO ==== >>>
# Para permitir que uma função retorne um valor, use a instrução return:
# <<< EXEMPLO 6 >>>
def my_function06(x):
  return 5 * x

print(my_function06(3))
print(my_function06(5))
print(my_function06(9))