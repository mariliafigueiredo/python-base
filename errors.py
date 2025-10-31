#%%
import os
import sys
names = open("names.txt").readlines()

#LBYL Look Before You Leap - Antes de fazer uma operacao verifique se é possivel fazer a operacao

if os.path.exixts("names.txt"):
    input("...") # Race Condition
    names = open("names.txt").readlines

else:
    print("[Error] File names.txt not found")
    sys.exit(1)

# Se o tamanho dos nomes que estou tentando acessar for maior ou igual a 3 eu vou poder acessar o item names sem ter erro - index error
# ou seja dou uma olhada LBYL
if len(names) >= 3:
    print(names[2])

# Incluindo esse else, não deixo o usuário ver qual erro do código e muitas vezes aparece o caminho de arquivo, dessa forma é mais seguro e não expomos o erro para o usuario

else:
    print("[Error] Missing name in the list")
    sys.exit(1)

#%%

