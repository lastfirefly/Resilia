from time import sleep

#index  0       1           2           3        4 
fila = ["","Andressa", "Beatriz", "Ederson", "Hernandi"]



# for i in fila:

#     if i == "":
#         continue
#     else:
#         print(f"{i} você está na posição {fila.index(i)}")
#         sleep(1)


recemChegados = ["Rômulo", "Cristiane"]

filaNova = fila + recemChegados

facilitadores = ["Rômulo", "Cristiane", "Simone"]



for facilitadores in filaNova:
    if facilitadores in filaNova:
        print(True)
        break
    else:
        print(False)
        break