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
""" SEMPRE DAR PREFERENCIA EM USAR O  """
import os
import sys

#EAFP - Easy to Ask Forgiveness than permission - É mais fácil tentar e depois tratar o erro, ou seja menos verificações e mais rápido
#(É mais fácil pedir perdão do que permissão)

try: #vem de tentar
    names = open("names.txt").readlines  #FileNotFoundError
    1 / 0 # ZeroDivisionError 
    print(names.banana) # AttributeError

except: #Bare except captura qualquer excessão que ocorrer
    print("[Error] File names.txt not found")
    sys.exit(1)

try:
    print(names[2])

except:
    print("[Error] Missing name in the list")
    sys.exit(1)


#%%
import os
import sys

#EAFP - Easy to Ask Forgiveness than permission - É mais fácil tentar e depois tratar o erro, ou seja menos verificações e mais rápido
#(É mais fácil pedir perdão do que permissão)

try: #vem de tentar
    names = open("names.txt").readlines  #FileNotFoundError
    1 / 0 # ZeroDivisionError 
    print(names.banana) # AttributeError

except FileNotFoundError: #Captura excessão especifica de error, ou seja dessa forma os error que não estão especificados ainda vão aparecer com o nome do erro deles
    print("[Error] File names.txt not found")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You cant divide by zero!")
    sys,exit(1)
except AttributeError:
    print("[Error] List doesn't have banana")
    sys.exit(1)


try:
    print(names[2])

except:
    print("[Error] Missing name in the list")
    sys.exit(1)

#%%
import os
import sys

#EAFP - Easy to Ask Forgiveness than permission - É mais fácil tentar e depois tratar o erro, ou seja menos verificações e mais rápido
#(É mais fácil pedir perdão do que permissão)

try: #vem de tentar
    names = open("names.txt").readlines  #FileNotFoundError

except (FileNotFoundError, ZeroDivisionError) as e: #Captura excessão especifica de error, ou seja dessa forma os error que não estão especificados ainda vão aparecer com o nome do erro deles
    #usando as e vamos ter o objeto do erro logo abaixo

    print(f"{str(e)}")
    sys.exit(1)
    #TODO: Usar Retry
    #retry tenta de novo daqui x segundos

else: #só executa se não tiver erro
    print("Sucesso!!!")
finally: #independente de ter erro ou não ele sempre executa
    print("Execute isso sempre")
try:
    print(names[2])

except:
    print("[Error] Missing name in the list")
    sys.exit(1)

#%%
# Por conta propria quero subir um erro
import os
import sys

#EAFP - Easy to Ask Forgiveness than permission - É mais fácil tentar e depois tratar o erro, ou seja menos verificações e mais rápido
#(É mais fácil pedir perdão do que permissão)

#RAISE significa subir um erro por conta propria
try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e: # except qualquer execeção como erro
    print(str(e)) # str da exececao

try: #vem de tentar
    names = open("names.txt").readlines  #FileNotFoundError

except (FileNotFoundError, ZeroDivisionError) as e: #Captura excessão especifica de error, ou seja dessa forma os error que não estão especificados ainda vão aparecer com o nome do erro deles
    #usando as e vamos ter o objeto do erro logo abaixo

    print(f"{str(e)}")
    sys.exit(1)
    #TODO: Usar Retry
    #retry tenta de novo daqui x segundos

else: #só executa se não tiver erro
    print("Sucesso!!!")
finally: #independente de ter erro ou não ele sempre executa
    print("Execute isso sempre")
try:
    print(names[2])

except:
    print("[Error] Missing name in the list")
    sys.exit(1)