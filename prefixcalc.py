
#%%
"""Calculadora prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em prefixcalc.log
"""
_version_ = "0.1.0"

import os
import sys

from datetime import datetime

arguments = sys.argv[1:]

if not arguments:
    operacao = input("operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments =[operacao, n1, n2]

elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: sum 5 5")
    sys.exit(1)

operacao, *nums = arguments

valida_operacao = ("sum", "sub", "mul", "div")
if operacao not in valida_operacao:
    print("Operação inválida!")
    print(valida_operacao)
    sys.exit(1)

valida_numero = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    valida_numero.append(num)

n1, n2 = valida_numero

#TODO: USAR DICT DE FUNCOES
if operacao == "sum":
    resultado = n1 + n2
elif operacao == "sub":
    resultado = n1 - n2
elif operacao == "mul":
    resultado = n1 * n2
elif operacao == "div":
    resultado = n1 / n2

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anônimo")

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operacao}, {n1}, {n2} = {resultado}\n")

#print(f"{operation}, {n1}, {n2} = {resultado}", file=open(filename, "a"))

print(f"O resultado é {resultado}")



"""
verificando no prompt de comando o que foi salvo

Get-Content prefixcalc.py
Get-Content prefixcalc.log
"""