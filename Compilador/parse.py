# Importando bibliotecas
from tokenizer import Tokenizer, Token
from node import *


#Declarando a classe Token

class Parser:

    tokenizer = None

    # Método - Program

    def parse_program():
        node = Program(None, [])
        while Parser.tokenizer.next.type != 'EOF':
            filho = Parser.parse_statement()
            # print(filho)
            if filho is not None:
                node.children.append(filho)
        return node
    
    # Método - Block
    
    def parse_block():
        node = Block(None, [])
        if Parser.tokenizer.next.type == "CHAVES ABERTO":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PULA LINHA":
                Parser.tokenizer.select_next()

                while Parser.tokenizer.next.type != 'CHAVES FECHADO':
                    filho = Parser.parse_statement()
                    node.children.append(filho)

                Parser.tokenizer.select_next()
        return node
    
    # Método - Assignment

    def parse_assignment():
        variavel = Parser.tokenizer.next.value

        Parser.tokenizer.select_next()

        if Parser.tokenizer.next.type == "IGUAL":
            Parser.tokenizer.select_next()
            node = Assignment("=", [variavel, Parser.parse_bool_expression()])
            return node
        else:
            raise Exception()

    
    # Método - Statement

    def parse_statement():

        # print(Parser.tokenizer.next.type)

        # Apenas pula linha
        if Parser.tokenizer.next.type == "PULA LINHA":
            Parser.tokenizer.select_next()
            node = NoOp(None, None)
            return node
        
        if Parser.tokenizer.next.type == "POUSAR":
            Parser.tokenizer.select_next()
            node = Pousar(None, None)
            return node
        
        if Parser.tokenizer.next.type == "DECOLAR":
            Parser.tokenizer.select_next()
            node = Decolar(None, None)
            return node
        
        if Parser.tokenizer.next.type == "AJUSTARANG":
            Parser.tokenizer.select_next()
            node = Ajustarang(None, None)
            return node
        
        if Parser.tokenizer.next.type == "AJUSTARPOS":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PARENTESE ABERTO":
                Parser.tokenizer.select_next()
                node = Ajustarpos(None, [Parser.parse_bool_expression()])

                if Parser.tokenizer.next.type == "VIRGULA":
                    Parser.tokenizer.select_next()
                    node.children.append(Parser.parse_bool_expression())

                if Parser.tokenizer.next.type == "PARENTESE FECHADO":
                    Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type == "PULA LINHA":
                        Parser.tokenizer.select_next()
                        return node
        
        if Parser.tokenizer.next.type == "ATIVAR":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PARENTESE ABERTO":
                Parser.tokenizer.select_next()
                node = Ativar(None, [Parser.parse_bool_expression()])

                if Parser.tokenizer.next.type == "PARENTESE FECHADO":
                    Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type == "PULA LINHA":
                        Parser.tokenizer.select_next()
                        return node

        # Comando de print

        elif Parser.tokenizer.next.type == "PRINTAR":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PARENTESE ABERTO":
                Parser.tokenizer.select_next()
                node = Escrever(None, [Parser.parse_bool_expression()])

                if Parser.tokenizer.next.type == "PARENTESE FECHADO":
                    Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type == "PULA LINHA":
                        Parser.tokenizer.select_next()
                        return node
                    
                    else:
                        raise Exception()
                else:
                    raise Exception()
            else:
                raise Exception()
            
        elif Parser.tokenizer.next.type == "IDEN":
            resultado = Parser.parse_assignment()

            if Parser.tokenizer.next.type == "PULA LINHA":
                Parser.tokenizer.select_next()
                return resultado
            
        # Comando de if
        
        elif Parser.tokenizer.next.type == "IF":

            Parser.tokenizer.select_next()
            node = Se(None, [Parser.parse_bool_expression(), Parser.parse_block()])
            

            if Parser.tokenizer.next.type == "ELSE":
                Parser.tokenizer.select_next()
                node.children.append(Parser.parse_block())

                if Parser.tokenizer.next.type == "PULA LINHA":
                    Parser.tokenizer.select_next()
                    return node
                
                else:
                    raise Exception()
                
            elif Parser.tokenizer.next.type == "PULA LINHA":
                Parser.tokenizer.select_next()
                return node
                
            
            else:
                raise Exception()
            
        # Comando de for
        
        elif Parser.tokenizer.next.type == "FOR":
            Parser.tokenizer.select_next()
            node = Enquanto(None, [Parser.parse_assignment()])

            # print(Parser.tokenizer.next.type)
            
            if Parser.tokenizer.next.type == "PONTO E VIRGULA":
                Parser.tokenizer.select_next()
                node.children.append(Parser.parse_bool_expression())

                if Parser.tokenizer.next.type == "PONTO E VIRGULA":
                    Parser.tokenizer.select_next()
                    node.children.append(Parser.parse_assignment())
                    node.children.append(Parser.parse_block())
                    # print(Parser.tokenizer.next.type)

                    if Parser.tokenizer.next.type == "PULA LINHA":
                        Parser.tokenizer.select_next()
                        return node
                    
                    else:
                        raise Exception()
                
                else:
                    raise Exception()

            else:
                raise Exception()
            
        elif Parser.tokenizer.next.type == "VARIAVEL":
            node = VarDec(None, [])
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "IDEN":
                iden = Identifier(Parser.tokenizer.next.value, [])
                Parser.tokenizer.select_next()

                if Parser.tokenizer.next.type == "TYPE":
                    tipo = Parser.tokenizer.next.value
                    node.value = tipo
                    node.children.append(iden)
                    Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type == "IGUAL":
                        Parser.tokenizer.select_next()
                        node.children.append(Parser.parse_bool_expression())
                        # Parser.tokenizer.select_next()
                        # print(Parser.tokenizer.next.type)

                        if Parser.tokenizer.next.type == "PULA LINHA":
                            Parser.tokenizer.select_next()
                            return node
                        
                        else:
                            raise Exception()
                        
                    elif Parser.tokenizer.next.type == "PULA LINHA":
                        Parser.tokenizer.select_next()
                        return node
                    
                    else:
                        raise Exception()
                else:
                    raise Exception()
            else:
                raise Exception() 
        else:
            raise Exception()

    # Método - Expression

    def parse_expression():

        filho_esquerdo = Parser.parse_term()

        while Parser.tokenizer.next.type in ["PLUS" , "MINUS", "PONTO"]:

            if Parser.tokenizer.next.type == "PLUS":
                Parser.tokenizer.select_next()
                node = BinOp("+", [filho_esquerdo, Parser.parse_term()])
                filho_esquerdo = node

            elif Parser.tokenizer.next.type == "MINUS":
                Parser.tokenizer.select_next()
                node = BinOp("-", [filho_esquerdo, Parser.parse_term()])
                filho_esquerdo = node
            
            elif Parser.tokenizer.next.type == "PONTO":
                Parser.tokenizer.select_next()
                node = BinOp(".", [filho_esquerdo, Parser.parse_term()])
                filho_esquerdo = node

            else:
                raise Exception()
            
        return filho_esquerdo
    

    # Método - Term

    def parse_term():

        filho_esquerdo = Parser.parse_factor()
        while Parser.tokenizer.next.type in ["MULTIPLY" , "DIVIDE"]:

            if Parser.tokenizer.next.type == "MULTIPLY":
                Parser.tokenizer.select_next()
                node = BinOp("*", [filho_esquerdo, Parser.parse_factor()])
                filho_esquerdo = node

            elif Parser.tokenizer.next.type == "DIVIDE":
                Parser.tokenizer.select_next()
                node = BinOp("/", [filho_esquerdo, Parser.parse_factor()])
                filho_esquerdo = node
            else:
                raise Exception()
        
        return filho_esquerdo
    

    # Método - Factor

    def parse_factor():

        if Parser.tokenizer.next.type == "INT":
            resultado_int = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            return IntVal(resultado_int, [])
        
        elif Parser.tokenizer.next.type == "STRING":
            resultado_string = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            return StringVal(resultado_string, [])

        elif Parser.tokenizer.next.type == "PLUS":
            Parser.tokenizer.select_next()
            return UnOp("+", [Parser.parse_factor()])

        elif Parser.tokenizer.next.type == "MINUS":
            Parser.tokenizer.select_next()
            return UnOp("-", [Parser.parse_factor()])
        
        elif Parser.tokenizer.next.type == "NOT":
            Parser.tokenizer.select_next()
            return UnOp("!", [Parser.parse_factor()])
        
        elif Parser.tokenizer.next.type == "PARENTESE ABERTO":
            Parser.tokenizer.select_next()
            Parser.resultado_factor = Parser.parse_bool_expression()

            if Parser.tokenizer.next.type == "PARENTESE FECHADO":
                Parser.tokenizer.select_next()
                return Parser.resultado_factor
            
        elif Parser.tokenizer.next.type == "IDEN":
            retorno_iden = Identifier(None, [Parser.tokenizer.next.value])
            Parser.tokenizer.select_next()
            return retorno_iden
        
        elif Parser.tokenizer.next.type == "SCANEAR":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PARENTESE ABERTO":
                Parser.tokenizer.select_next()
                valor_scan = int(input())

                if Parser.tokenizer.next.type == "PARENTESE FECHADO":
                    Parser.tokenizer.select_next()
                    return Escanear(valor_scan, [])


        raise Exception() 
    
    # Método - Bool_expression
    
    def parse_bool_expression():

        filho_esquerdo = Parser.parse_bool_term()

        while Parser.tokenizer.next.type in ["OR"]:

            Parser.tokenizer.select_next()
            node = BinOp("||", [filho_esquerdo, Parser.parse_bool_term()])
            filho_esquerdo = node

        # print("return do bool expression")
        return filho_esquerdo


    # Método - Bool_term

    def parse_bool_term():

        filho_esquerdo = Parser.parse_rel_expression()

        while Parser.tokenizer.next.type in ["AND"]:

            Parser.tokenizer.select_next()
            node = BinOp("&&", [filho_esquerdo, Parser.parse_rel_expression()])
            filho_esquerdo = node
            
        return filho_esquerdo
    
    # Método - Rel_expression

    def parse_rel_expression():

        filho_esquerdo = Parser.parse_expression()

        while Parser.tokenizer.next.type in ["IGUAL IGUAL", "MAIOR QUE", "MENOR QUE"]:

            if Parser.tokenizer.next.type == "IGUAL IGUAL":
                Parser.tokenizer.select_next()
                node = BinOp("==", [filho_esquerdo, Parser.parse_expression()])
                filho_esquerdo = node

            elif Parser.tokenizer.next.type == "MAIOR QUE":
                Parser.tokenizer.select_next()
                node = BinOp(">", [filho_esquerdo, Parser.parse_expression()])
                filho_esquerdo = node

            elif Parser.tokenizer.next.type == "MENOR QUE":
                Parser.tokenizer.select_next()
                node = BinOp("<", [filho_esquerdo, Parser.parse_expression()])
                filho_esquerdo = node
        
        return filho_esquerdo
    
    # Método - run
    
    def run(code):
        Parser.tokenizer = Tokenizer(code, None)

        # Parser.tokenizer.select_next()
        # while Parser.tokenizer.next.type != 'EOF':
        #     print(Parser.tokenizer.next.type)
        #     Parser.tokenizer.select_next()

        Parser.tokenizer.select_next()
        resultado = Parser.parse_program()

        if Parser.tokenizer.next.type == 'EOF':
                return resultado
        else:
            raise Exception()