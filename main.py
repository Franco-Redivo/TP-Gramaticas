from antlr4 import *

from ResiduosLexer import ResiduosLexer
from ResiduosParser import ResiduosParser

with open("test_correcto.txt") as f:
    texto = f.read()

##with open("test_error_sintactico.txt") as f:
##  texto = f.read()

##with open("test_error_sintactico2.txt") as f:
##    texto = f.read()

lexer = ResiduosLexer(InputStream(texto))
tokens = CommonTokenStream(lexer)

parser = ResiduosParser(tokens)

tree = parser.program()

print(tree.toStringTree(recog=parser))