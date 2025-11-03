# #%%
# # stderr onde vai os erros 

# import logging

# logging.critical("Deu problema geral") # root logger

# try:
#     1 / 0

# except ZeroDivisionError as e:
#     print(f"[Erro] Deu erro {str(e)}")
    
# #%%

# import logging

# logging.debug("Mensagem para o dev, qe, sysadmin")
# logging.info("Menagem geral para usuario")
# logging.warning("Aviso que nao causa erro")
# logging.error("Erro que afeta uma unica execucao")
# logging.critical("Erro geral ex: banco de dados sumiu")

# print("---")

# logging.critical("Deu problema geral") # root logger metodo que grava o logging

# try:
#     1 / 0

# except ZeroDivisionError as e:
#     #usando logging não pode usar a f string
#     logging.error("Deu erro %s", str(e))

#%%

import logging
""" DESSA PARTE """
# nossa instancia
log = logging.Logger("logs.py", logging.DEBUG)
#level
ch = logging.StreamHandler()    #Responsavel por escrever no distino que eu quiser
ch.setLevel(logging.DEBUG)
#formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
    #hora atual - nome do logger'logs.py' - qual estou 'debug, info,warning, error, critical' 
    # - numero da linha onde a mensagem ocorreu - nome do arquivo - mensagem
)
ch.setFormatter(fmt)
#destino
log.addHandler(ch)
""" ATE ESSA PARTE É SÓ PARA FORMATAÇÃO DO Logger"""

log.debug("Mensagem para o dev, qe, sysadmin")
log.info("Menagem geral para usuario")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")

print("---")

log.critical("Deu problema geral") # root logger metodo que grava o logging

try:
    1 / 0

except ZeroDivisionError as e:
    #usando logging não pode usar a f string
    logging.error("Deu erro %s", str(e))
    
#%%

import os
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

""" DESSA PARTE """
# nossa instancia
log = logging.Logger("logs.py", log_level)
#level
ch = logging.StreamHandler()    #Responsavel por escrever no distino que eu quiser
ch.setLevel(log_level)
#formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
    #hora atual - nome do logger'logs.py' - qual estou 'debug, info,warning, error, critical' 
    # - numero da linha onde a mensagem ocorreu - nome do arquivo - mensagem
)
ch.setFormatter(fmt)
#destino
log.addHandler(ch)
""" ATE ESSA PARTE É SÓ PARA FORMATAÇÃO DO Logger"""

log.debug("Mensagem para o dev, qe, sysadmin")
log.info("Menagem geral para usuario")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")

print("---")

log.critical("Deu problema geral") # root logger metodo que grava o logging

try:
    1 / 0

except ZeroDivisionError as e:
    #usando logging não pode usar a f string
    logging.error("Deu erro %s", str(e))