#Declarando a classe Token
class Token:
    
    def __init__(self, type: str, value: int):
        self.type = type
        self.value = value

#Declarando a classe Tokenizer
class Tokenizer:

    def __init__(self, source: str, next: Token):
        self.source = source
        self.position = 0
        self.next = next

    def select_next(self):

        #Tokens
        while self.position < len(self.source):
            
            caracter = self.source[self.position]
            numero = ""
            
            # print(f'Tamanho da palavra: {len(self.source)}')
            # print(caracter)
            # print(f'Posição: {self.position}')
            # print(caracter.isspace())

            if caracter.isnumeric():
                while caracter.isnumeric():

                    tipo = "INT"
                    numero += caracter
                    self.position += 1
                    if self.position >= len(self.source):
                        self.next = Token(tipo, int(numero))
                        return
                    caracter = self.source[self.position]
                valor = int(numero)
                self.next = Token(tipo, valor)
                return
            
            elif caracter == "+":
                tipo = "PLUS"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return

            elif caracter == "-":
                tipo = "MINUS"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == "*":
                tipo = "MULTIPLY"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return

            elif caracter == "/":
                tipo = "DIVIDE"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == "(":
                tipo = "PARENTESE ABERTO"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == ")":
                tipo = "PARENTESE FECHADO"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == "{":
                tipo = "CHAVES ABERTO"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == "}":
                tipo = "CHAVES FECHADO"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == ">":
                tipo = "MAIOR QUE"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == "<":
                tipo = "MENOR QUE"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == "!":
                tipo = "NOT"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == ",":
                tipo = "VIRGULA"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == ";":
                tipo = "PONTO E VIRGULA"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == ".":
                tipo = "PONTO"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == '"':
                palavra = ""
                self.position +=1
                caracter = self.source[self.position]
                while caracter != '"':
                    caracter = self.source[self.position]
                    if caracter == '"':
                        self.position +=1
                        break
                    palavra += caracter
                    self.position +=1
                tipo = "STRING"
                valor = palavra
                self.next = Token(tipo, valor)
                return
            
            elif caracter == "=":
                
                self.position += 1
                caracter = self.source[self.position]

                if caracter == "=":
                    tipo = "IGUAL IGUAL"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return

                self.position -= 1
                caracter = self.source[self.position]


                tipo = "IGUAL"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter == "\n":
                tipo = "PULA LINHA"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif caracter in [",", "[", "]"]:
                raise Exception()
            
            
            elif type(caracter) == str:
                palavra = ""

                # print(f'Tamanho da palavra: {len(self.source)}')
                # print(caracter)
                # print(f'Posição: {self.position}')
                # print(caracter.isnumeric())

                # if palavra == " ":
                #     self.position += 1
                #     return
                
                while ((caracter.isidentifier()) or (caracter.isdigit())):

                    caracter = self.source[self.position]
                    # print(caracter)
                    # print(f'Posição: {self.position}')

                    if not ((caracter.isidentifier()) or (caracter.isdigit())):
                        self.position -= 1
                        # print(f'Posição: {self.position}')
                        # print("Breakaeado")
                        break
                    
                    # print("AQUI N PODE SER 19")
                    # print(f'Posição: {self.position}')
                    palavra += caracter
                    self.position += 1
                
                # print("FORA DO WHILE")
                # print(f'Posição: {self.position}')
                
                if palavra == "Println":
                    tipo = "PRINTAR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "pousar":
                    tipo = "POUSAR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "decolar":
                    tipo = "DECOLAR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "ajustar_angulo":
                    tipo = "AJUSTARANG"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "ajustar_posicao":
                    tipo = "AJUSTARPOS"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "ativar_foguete":
                    tipo = "ATIVAR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "for":
                    tipo = "FOR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "if":
                    tipo = "IF"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "else":
                    tipo = "ELSE"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "Scanln":
                    tipo = "SCANEAR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "var":
                    tipo = "VARIAVEL"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
            
                elif palavra == "int":
                    tipo = "TYPE"
                    valor = "INT"
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "string":
                    tipo = "TYPE"
                    valor = "STR"
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif caracter in ["|", "&"]:
                    while caracter in ["|", "&"]:
                        
                        if palavra == "||":
                            tipo = "OR"
                            valor = 0
                            self.position += 1
                            self.next = Token(tipo, valor)
                            return
                        
                        elif palavra == "&&":
                            tipo = "AND"
                            valor = 0
                            self.position += 1
                            self.next = Token(tipo, valor)
                            return
                        
                        palavra += caracter
                        self.position += 1

                elif palavra == "":
                    self.position += 1

                # elif caracter.isspace():
                #     self.position += 1
                #     continue

                # elif caracter == ")":
                #     print("Aqui")
                #     tipo = "IDEN"
                #     valor = palavra
                #     self.position += 1
                #     self.next = Token(tipo, valor)
                #     return

                else:
                    # print("iden")
                    # print(palavra)
                    tipo = "IDEN"
                    valor = palavra
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return

            else:
                self.position += 1

        if self.position >= len(self.source):
            tipo = "EOF"
            self.next = Token(tipo, 0)
            return