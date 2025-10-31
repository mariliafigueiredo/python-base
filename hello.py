# #%%
# """
# Hello World Multi Linguas.

# Dependendo da lingua configurada no ambiente o programa 
# exibe a mensagem correspondente.

# Como usar:
# Tenha a variavel LANG devidamente configurada exemplo:
# export LANG=pt_BR

# Execução: python3 hello.py ou .hello.py
# """
# _version_ = "0.1.0"
# _autor_   = "Marília Figueiredo"
# _license_ = "Unlicense"

# import os

# current_language = os.getenv("LANG", "en_US")[:5]

# msg = "Hello, World!"

# # sets (Hash Table) - O(1) - contante
# #Ordem Compexidade O(n)
# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde"
    
# print(msg)
# #%%
# import os

# current_language = os.getenv("LANG", "en_US")[:5]

# msg = {
#      "en_US": "Hello, World!",
#      "pt_BR": "Olá, Mundo!",
#      "it_IT": "Ciao, Mondo!",
#      "es_SP": "Hola Mundo!",
#      "fr_FR": "Bonjour Monde",
# }
    
# print(msg[current_language])
# # %%
# lang = "pt_BR.utf8"

# len (lang)

# lang[:5]

# lang.split(".")

# lang.split(".")[0]

# # %%
# _version_ = "0.0.1"
# _autor_   = "Marília Figueiredo"
# _license_ = "Unlicense"

# import os

# import sys

# """dessa forma consigo fazer Debugging

# print(f"{sys.argv=}")  

# """


# arguments = {"lang": None,
#              "count": None,}           #dicionario acumulador
# for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
#     print(f"{arg=}")                   #pega o Debugging e passa pra dentro do for


# current_language = os.getenv("LANG", "en_US")[:5]

# msg = "Hello, World!"

# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde"
    
# print(msg)
# # %%
# # %%
# _version_ = "0.0.1"
# _autor_   = "Marília Figueiredo"
# _license_ = "Unlicense"

# import os

# import sys

# """dessa forma consigo fazer Debugging

# print(f"{sys.argv=}")  

# """

# arguments = {"lang": None,
#              "count": None,}           #dicionario acumulador
# for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
#     print(arg.split("="))               #separa a chave e o valor pelo igual


# current_language = os.getenv("LANG", "en_US")[:5]

# msg = "Hello, World!"

# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde"
    
# print(msg)

# # %%
# _version_ = "0.0.1"
# _autor_   = "Marília Figueiredo"
# _license_ = "Unlicense"

# import os

# import sys

# """dessa forma consigo fazer Debugging

# print(f"{sys.argv=}")  

# """

# arguments = {"lang": None,
#              "count": None,}           #dicionario acumulador
# for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
#     #TODO: Tratar ValueError
#     key, value = arg.split("=")              #separa a chave e o valor pelo igual
#     if key not in arguments:
#         print(f"Opção Inválida {key}")
#     print(key. value)

# current_language = os.getenv("LANG", "en_US")[:5]

# msg = "Hello, World!"

# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde"
    
# print(msg)

# # %%
# #opçoes para remover tracinhos -verifiquei no ipython

# key = "--nome-composto--"

# key[2:]

# key.replace("-","")

# key.strip("-")

# key.lstrip("-")  #tita os tracinho somente da esquerda
# # %%
# _version_ = "0.0.1"
# _autor_   = "Marília Figueiredo"
# _license_ = "Unlicense"

# import os

# import sys

# """dessa forma consigo fazer Debugging

# print(f"{sys.argv=}")  

# """

# arguments = {"lang": None,
#              "count": None,}           #dicionario acumulador
# for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
#     #TODO: Tratar ValueError
#     key, value = arg.split("=")        #separa a chave e o valor pelo igual
#     key = key.lstrip("-").strip()     #Reatribuindo a própria variável key para o valor dela mesma sem os tracinhos e outro strip pra retirar os espaços em branco do inicio e do fim
#     value = value.strip()
#     if key not in arguments:
#         print(f"Opção Inválida {key}")
#         sys.exit()
#     print(key. value)

# current_language = os.getenv("LANG", "en_US")[:5]

# msg = "Hello, World!"

# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde"
    
# print(msg)

# %%
_version_ = "0.0.1"
# _autor_   = "Marília Figueiredo"
# _license_ = "Unlicense"

# import os

# import sys

# """dessa forma consigo fazer Debugging

# print(f"{sys.argv=}")  

# """

# arguments = {"lang": None,
#              "count": None,}           #dicionario acumulador
# for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
#     #TODO: Tratar ValueError
#     key, value = arg.split("=")        #separa a chave e o valor pelo igual
#     key = key.lstrip("-").strip()     #Reatribuindo a própria variável key para o valor dela mesma sem os tracinhos e outro strip pra retirar os espaços em branco do inicio e do fim
#     value = value.strip()
#     if key not in arguments:
#         print(f"Opção Inválida {key}")
#         sys.exit()
#     arguments[key] = value

# current_language = os.getenv("LANG", "en_US")[:5]

# msg = "Hello, World!"

# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde"
    
# print(msg)
# %%
# _autor_   = "Marília Figueiredo"
# _license_ = "Unlicense"

# import os

# import sys

# """dessa forma consigo fazer Debugging

# print(f"{sys.argv=}")  

# """

# arguments = {"lang": None, "count": 1,}           #dicionario acumulador
# for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
#     #TODO: Tratar ValueError
#     key, value = arg.split("=")        #separa a chave e o valor pelo igual
#     key = key.lstrip("-").strip()     #Reatribuindo a própria variável key para o valor dela mesma sem os tracinhos e outro strip pra retirar os espaços em branco do inicio e do fim
#     value = value.strip()
#     if key not in arguments:
#         print(f"Opção Inválida {key}")
#         sys.exit()
#     arguments[key] = value

# current_language = arguments["lang"]

# if current_language is None:
#     current_language = os.getenv("LANG", "pt_BR")[:5]

# msg = {
#      "en_US": "Hello, World!",
#      "pt_BR": "Olá, Mundo!",
#      "it_IT": "Ciao, Mondo!",
#      "es_SP": "Hola Mundo!",
#      "fr_FR": "Bonjour Monde!",
# }
    
# print(msg[current_language] * int(arguments["count"]))
# #python hello.py --lang=pt_BR --count=10
# %%
# """
# Hello World Multi Linguas.

# Dependendo da lingua configurada no ambiente o programa 
# exibe a mensagem correspondente.

# Como usar:
# Tenha a variavel LANG devidamente configurada exemplo:
# export LANG=pt_BR

# Ou informe atráves do CLI argument lang

# Ou o usuário terá que digitar

# Execução: python3 hello.py ou .hello.py
# """
# _version_ = "0.1.3"
# _autor_   = "Marília Figueiredo"
# _license_ = "Unlicense"

# import os

# import sys

# """dessa forma consigo fazer Debugging

# print(f"{sys.argv=}")  

# """

# arguments = {"lang": None, "count": 1,}           #dicionario acumulador
# for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
#     #TODO: Tratar ValueError
#     key, value = arg.split("=")        #separa a chave e o valor pelo igual
#     key = key.lstrip("-").strip()     #Reatribuindo a própria variável key para o valor dela mesma sem os tracinhos e outro strip pra retirar os espaços em branco do inicio e do fim
#     value = value.strip()
#     if key not in arguments:
#         print(f"Opção Inválida {key}")
#         sys.exit()
#     arguments[key] = value

# current_language = arguments["lang"]

# if current_language is None:
#     # TODO: Usar repetição
#     if "LANG" in os.environ:
#         current_language = os.getenv("LANG")
#     else:
#         current_language = input("Qual a linguagem:")

# current_language = current_language[:5]

# msg = {
#      "en_US": "Hello, World!",
#      "pt_BR": "Olá, Mundo!",
#      "it_IT": "Ciao, Mondo!",
#      "es_SP": "Hola Mundo!",
#      "fr_FR": "Bonjour Monde!",
# }
    

# print(msg[current_language] * int(arguments["count"]))
# # %%
# # %%
# #TRATANDO TODO COM LBYL
# """
# Hello World Multi Linguas.

# Dependendo da lingua configurada no ambiente o programa 
# exibe a mensagem correspondente.

# Como usar:
# Tenha a variavel LANG devidamente configurada exemplo:
# export LANG=pt_BR

# Ou informe atráves do CLI argument lang

# Ou o usuário terá que digitar

# Execução: python3 hello.py ou .hello.py
# """
# _version_ = "0.1.3"
# _autor_   = "Marília Figueiredo"
# _license_ = "Unlicense"

# import os

# import sys

# """dessa forma consigo fazer Debugging

# print(f"{sys.argv=}")  

# """

# arguments = {"lang": None, "count": 1,}           #dicionario acumulador
# for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
#     #TODO: Tratar ValueError 
#     # dessa forma estou tratando o erro com LBYL
#     if "=" in arg:                     # se 
#         key, value = arg.split("=")        #separa a chave e o valor pelo igual
#     else:
#         print("Voce precisa usar o `=`")
#         sys.exit(1)

#     key = key.lstrip("-").strip()     #Reatribuindo a própria variável key para o valor dela mesma sem os tracinhos e outro strip pra retirar os espaços em branco do inicio e do fim
#     value = value.strip()
#     if key not in arguments:
#         print(f"Opção Inválida {key}")
#         sys.exit()
#     arguments[key] = value

# current_language = arguments["lang"]

# if current_language is None:
#     # TODO: Usar repetição
#     if "LANG" in os.environ:
#         current_language = os.getenv("LANG")
#     else:
#         current_language = input("Qual a linguagem:")

# current_language = current_language[:5]

# msg = {
#      "en_US": "Hello, World!",
#      "pt_BR": "Olá, Mundo!",
#      "it_IT": "Ciao, Mondo!",
#      "es_SP": "Hola Mundo!",
#      "fr_FR": "Bonjour Monde!",
# }
    

# print(msg[current_language] * int(arguments["count"]))

# %%

"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa 
exibe a mensagem correspondente.

Como usar:
Tenha a variavel LANG devidamente configurada exemplo:
export LANG=pt_BR

Ou informe atráves do CLI argument lang

Ou o usuário terá que digitar

Execução: python3 hello.py ou .hello.py
"""
_version_ = "0.1.3"
_autor_   = "Marília Figueiredo"
_license_ = "Unlicense"

import os

import sys

"""dessa forma consigo fazer Debugging

print(f"{sys.argv=}")  

"""

arguments = {"lang": None, "count": 1,}           #dicionario acumulador
for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
    #TODO: Tratar ValueError 
    # dessa forma estou tratando o erro com EAFP
    try:                    
        key, value = arg.split("=")        #separa a chave e o valor pelo igual
    except ValueError as e:
        # TODO: Logging
        print(f"[Error] {str(e)}")
        print("Voce precisa usar o `=`")
        sys.exit(1)

    key = key.lstrip("-").strip()     #Reatribuindo a própria variável key para o valor dela mesma sem os tracinhos e outro strip pra retirar os espaços em branco do inicio e do fim
    value = value.strip()
    if key not in arguments:
        print(f"Opção Inválida {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
#forma de realizar debugging   -  print(f"current_language=}"")

if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Qual a linguagem:")

current_language = current_language[:5]

msg = {
     "en_US": "Hello, World!",
     "pt_BR": "Olá, Mundo!",
     "it_IT": "Ciao, Mondo!",
     "es_SP": "Hola Mundo!",
     "fr_FR": "Bonjour Monde!",
}
 
#LBYL
if current_language in msg:
    message = msg[current_language] 
else:
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))
# %%
# %%

"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa 
exibe a mensagem correspondente.

Como usar:
Tenha a variavel LANG devidamente configurada exemplo:
export LANG=pt_BR

Ou informe atráves do CLI argument lang

Ou o usuário terá que digitar

Execução: python3 hello.py ou .hello.py
"""
_version_ = "0.1.3"
_autor_   = "Marília Figueiredo"
_license_ = "Unlicense"

import os

import sys

"""dessa forma consigo fazer Debugging

print(f"{sys.argv=}")  

"""

arguments = {"lang": None, "count": 1,}           #dicionario acumulador
for arg in sys.argv[1:]:               #Fatiamento, para cada um dos argumentos em sys.argv começando do item 1 pra frente
    #TODO: Tratar ValueError 
    # dessa forma estou tratando o erro com EAFP
    try:                    
        key, value = arg.split("=")        #separa a chave e o valor pelo igual
    except ValueError as e:
        # TODO: Logging
        print(f"[Error] {str(e)}")
        print("Voce precisa usar o `=`")
        sys.exit(1)

    key = key.lstrip("-").strip()     #Reatribuindo a própria variável key para o valor dela mesma sem os tracinhos e outro strip pra retirar os espaços em branco do inicio e do fim
    value = value.strip()
    if key not in arguments:
        print(f"Opção Inválida {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
#forma de realizar debugging   -  print(f"current_language=}"")

if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Qual a linguagem:")

current_language = current_language[:5]

msg = {
     "en_US": "Hello, World!",
     "pt_BR": "Olá, Mundo!",
     "it_IT": "Ciao, Mondo!",
     "es_SP": "Hola Mundo!",
     "fr_FR": "Bonjour Monde!",
}
 
#EAFP
try:
    message = msg[current_language] 
except KeyError as e:
    print(f"[Error] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))