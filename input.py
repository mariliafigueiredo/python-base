#%%
#import sys

#sys.stdin.read(3)

nome = input("Qual o seu nome?")

nome

input("Pressione enter para sair")
# %%

idade = int(input("Qual sua idade?"))

if idade < 18:
    print("Você não pode comprar alcool!")
# %%
# Limpeza de espaços em branco no final

nome = input("Qual o seu nome?")

nome = input("Qual o seu nome?").strip()


# %%