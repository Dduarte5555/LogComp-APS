# Importando bibliotecas
from abc import ABC, abstractmethod

# Implementando a classe SymbolTable

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def set_symbol(self, name, tipo, value):
        self.symbols[name] = (value, tipo)

    def get_symbol(self, name):
        result = self.symbols.get(name)
        return result


# Implementando a classe Node

class Node(ABC):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate():
        return

class BinOp(Node):

    def evaluate(self, SymbolTable):

        tipo1 = self.children[0].evaluate(SymbolTable)
        tipo2 = self.children[1].evaluate(SymbolTable)

        valor1 = tipo1[0]
        valor2 = tipo2[0]

        if tipo1[1] == tipo2[1]:
            if self.value == "+":
                return (valor1 + valor2, "INT")
            elif self.value == ".":
                 return ((str(valor1) + str(valor2)), "STR")
            elif self.value == "-":
                return (valor1 - valor2, "INT")
            elif self.value == "*":
                return (valor1 * valor2, "INT")
            elif self.value == "/":
                return (valor1 // valor2, "INT")
            elif self.value == "||":
                return (int(valor1 or valor2), "INT")
            elif self.value == "&&":
                return (int(valor1 and valor2), "INT")
            elif self.value == ">":
                return (int(valor1 > valor2), "INT")
            elif self.value == "<":
                return (int(valor1 < valor2), "INT")
            elif self.value == "==":
                return (int(valor1 == valor2), "INT")
        else:
            if self.value == ".":
                 return ((str(valor1) + str(valor2)), "STR")
            else:
                raise Exception()
        
class UnOp(Node):

    def evaluate(self, SymbolTable):

        if self.value == "+":
            return (self.children[0].evaluate(SymbolTable)[0], "INT")
        elif self.value == "-":
            return (-self.children[0].evaluate(SymbolTable)[0], "INT")
        elif self.value == "!":
            return (not self.children[0].evaluate(SymbolTable)[0], "INT")
    
class IntVal(Node):

    def evaluate(self, SymbolTable):
        return (self.value, "INT")
    
class StringVal(Node):

    def evaluate(self, SymbolTable):
        return (self.value, "STR")
    
class VarDec(Node):

    def evaluate(self, SymbolTable):
        
        if len(self.children) == 1:
            if self.children[0].value not in SymbolTable.symbols:
                SymbolTable.set_symbol(self.children[0].value, self.value, None)
            else:
                raise Exception()
        else:
            SymbolTable.set_symbol(self.children[0].value, self.value, self.children[1].evaluate(SymbolTable)[0])
        return

class Identifier(Node):

    def evaluate(self, SymbolTable):
        return SymbolTable.get_symbol(self.children[0])
        
class Assignment(Node):

    def evaluate(self , SymbolTable):
        valor, tipo = SymbolTable.get_symbol(self.children[0])
        
        tipo_a_ser_comparado = self.children[1].evaluate(SymbolTable)
        

        if tipo == "INT" and isinstance(tipo_a_ser_comparado, int):
            if self.value == "=":
                SymbolTable.set_symbol(self.children[0], tipo, self.children[1].evaluate(SymbolTable))
        elif tipo == "STR" and isinstance(tipo_a_ser_comparado, str):
            if self.value == "=":
                SymbolTable.set_symbol(self.children[0], tipo, self.children[1].evaluate(SymbolTable))

        elif isinstance(tipo_a_ser_comparado, tuple):
            if tipo == "INT" and isinstance(tipo_a_ser_comparado[0], int):
                if self.value == "=":
                    SymbolTable.set_symbol(self.children[0], tipo, self.children[1].evaluate(SymbolTable)[0])
            elif tipo == "STR" and isinstance(tipo_a_ser_comparado[0], str):
                if self.value == "=":
                    SymbolTable.set_symbol(self.children[0], tipo, self.children[1].evaluate(SymbolTable)[0])
        else:
            raise Exception()

class Block(Node):

    def evaluate(self, SymbolTable):
        for i in self.children:
            i.evaluate(SymbolTable)

class Program(Node):

    def evaluate(self, SymbolTable):
        for i in self.children:
            i.evaluate(SymbolTable)

class Escrever(Node):

    def evaluate(self, SymbolTable):
        resultado = self.children[0].evaluate(SymbolTable)[0]
        print(resultado)

class Se(Node):

    def evaluate(self, SymbolTable):

        if len(self.children) == 2:
            if self.children[0].evaluate(SymbolTable):
                self.children[1].evaluate(SymbolTable)

        else: 
            if self.children[0].evaluate(SymbolTable):
                self.children[1].evaluate(SymbolTable)
            else:
                self.children[2].evaluate(SymbolTable)

class Enquanto(Node):

    def evaluate(self, SymbolTable):
        self.children[0].evaluate(SymbolTable)
        while self.children[1].evaluate(SymbolTable)[0]:
            self.children[3].evaluate(SymbolTable)
            self.children[2].evaluate(SymbolTable)

class Escanear(Node):

    def evaluate(self, SymbolTable):
        return self.value
    
class Pousar(Node):

    def evaluate(self, SymbolTable):
        print("A nave está pousando")

class Decolar(Node):

    def evaluate(self, SymbolTable):
        print("A nave está decolando")

class Ajustarang(Node):

    def evaluate(self, SymbolTable):
        print("A nave está ajustando a sua angulação para o refencial predefinido")

class Ajustarpos(Node):

    def evaluate(self, SymbolTable):
        print(f"A nave está ajustando a sua posição para a coordenada ({self.children[0].evaluate(SymbolTable)[0]}, {self.children[1].evaluate(SymbolTable)[0]})")

class Ativar(Node):

    def evaluate(self, SymbolTable):
        print(f"A nave será ligada em {self.children[0].evaluate(SymbolTable)[0]} segundos")

    
class NoOp(Node):

    def evaluate(self, SymbolTable):
        return