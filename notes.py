"""Bloco de notas

$ notes.py new "minha Nota"
tag: tech
text:
Anotacao geral sobre carreita de tecnologia

$ notes.py read tag=tech
...
...

"""
__version__ = "0.1.0"

import os  #apartir do OS que chegamos nos caminhos de arquivo
import sys #apartir do SYS que podemos ler os comandos que o usuario vai passar na linha de comando

cmds = ("read", "new")
#caminho do arquivo onde vai ser salvo - diretorio atual
path = os.curdir
#diretorio atual 'path' + o arquivo chamado notes.txt
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]  #pegar os argumentos que vem do sys.argv, pegando do primeiro pra frente
if not arguments:              # se não tiver argumento, retorna a mensagem de invalido
    print("Invalid Usage")
    print(f"especifique o subcomando {cmds}")
    sys.exit(1)

#Lista de comando validos

if arguments[0] not in cmds:     #se o primeiro nao estiver dentro da lista de comandos validos, também retorna a mensagem de comando invalido
    print(f"Comando Invalido {arguments[0]}")  #Com isso eu sei que o subcomando ou é read ou é new

if arguments[0] == "read":
    #Leitura das notas, pegar cada uma das linhas
    for line in open(filepath):  # para cada linha em open, abrir filepath
        title, tag, text = line.split("\t")  #sei que as linha sao separadas por \t 
        if tag.lower() == arguments[1].lower(): #se a tag dentro do texto é igual a arguments[1] covertido para lower, mostre o titulo e o texto
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()


if arguments[0] == "new":
    #Criacao das notas
    title = arguments[1] #arguments 1 tem que exixtir #TODO: Tratar exception
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
# \t - tst
#abrir o arquivo filepath no modo de append porque vai ter várias notas, vou chama-lo de file_
with open(filepath, "a") as file_:
    file_.write("\t".join(text) + "\n")  #agora com o file_ eu posso chamar o write com listas separadas por tab \t e com isso dentro do join passo o texto

