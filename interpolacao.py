
# email_tmpl = """
#  Olá, %(nome)s

#  Tem interesse em comprar %(produto)s?

#  Este produto é ótimo para %(texto)s

#  Clique agora em %(link)s

#  Apenas %(quantidade)d disponível!

#  Preço promocional %(preco).2f

#  """
# import sys
# import os

# arguments = sys.argv[1:]
# if not arguments:
#     print("Informe o nome do arquivo de emails")
#     sys.exit(1)

# filename = arguments[0]

# path = os.curdir
# filepath = os.path.join(path, filename)  #recebendo parametro de linha de comando

# clientes = []
# for line in open(filepath):
#     name, email = line.split(",")
#     clientes.append((name, email))

# clientes = ["Marília", "João", "Bruno"]

# for cliente in clientes:
#     print(
#         email_tmpl
#         % {
#             "nome": cliente,
#             "produto": "caneta",
#             "texto": "Escrever muito bem",
#             "link": "https://canetaslegais.com",
#             "quantidade": 1,
#             "preco": 50.5,
#             }
#             )
# #%%
# email_tmpl = """
#  Olá, %(nome)s

#  Tem interesse em comprar %(produto)s?

#  Este produto é ótimo para %(texto)s

#  Clique agora em %(link)s

#  Apenas %(quantidade)d disponível!

#  Preço promocional %(preco).2f

#  """
# import sys
# import os

# arguments = sys.argv[1:]
# if not arguments:
#     print("Informe o nome do arquivo de emails")
#     sys.exit(1)

# filename = arguments[0]

# path = os.curdir
# filepath = os.path.join(path, filename)  #recebendo parametro de linha de comando

# clientes = []
# for line in open(filepath):
#     # TODO: Substituir por list comprehension
#     name, email = line.split(",")

# clientes = ["Marília", "João", "Bruno"]

# for name,  email in clientes:
#     # TODO Subtituir por envio de email
#     print(f"Enviando email para: {email}")
#     print(
#         email_tmpl
#         % {
#             "nome": name,
#             "produto": "caneta",
#             "texto": "Escrever muito bem",
#             "link": "https://canetaslegais.com",
#             "quantidade": 1,
#             "preco": 50.5,
#         }
#     )
#     print("-" * 50)
# #%%

# import sys
# import os

# arguments = sys.argv[1:]
# if not arguments:
#     print("Informe o nome do arquivo de emails")
#     sys.exit(1)

# filename = arguments[0]
# tempatename = arguments[1]

# path = os.curdir
# filepath = os.path.join(path, filename)  #recebendo parametro de linha de comando
# templatepath = os.path.join(path, tempatename)

# clientes = []
# for line in open(filepath):
#     # TODO: Substituir por list comprehension
#     name, email = line.split(",")

# clientes = ["Marília", "João", "Bruno"]

# for name,  email in clientes:
#     # TODO Subtituir por envio de email
#     print(f"Enviando email para: {email}")
#     print(
#         open(templatepath).read()
#         % {
#             "nome": name,
#             "produto": "caneta",
#             "texto": "Escrever muito bem",
#             "link": "https://canetaslegais.com",
#             "quantidade": 1,
#             "preco": 50.5,
#         }
#     )
#     print("-" * 50)
#%%


#%% 
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""
__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)  # emails.txt #recebendo parametro de linha de comando
templatepath = os.path.join(path, templatename)  # email_tmpl.txt

for line in open(filepath):
    name, email = line.split(",")

    # TODO Subtituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print("-" * 50)

#propt de comando python interpolacao.py emails.txt email_tmpl.txt
# %%

