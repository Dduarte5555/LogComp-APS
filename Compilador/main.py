# Bibliotecas
import sys
from parse import Parser
from prepro import PrePro
from node import SymbolTable

# Código main

with open(sys.argv[1], 'r') as go_file:
        go_code = go_file.read()

prepro = PrePro()
texto_sem_espaco = prepro.filter(go_code)
dicionario = SymbolTable()


root = Parser.run(texto_sem_espaco)

root.evaluate(dicionario)