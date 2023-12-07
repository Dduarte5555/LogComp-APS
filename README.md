# LogComp-APS

Criação de uma linguagem de programação voltada para missões espaciais. Essa ideia saiu de uma pesquisa de qual linguagem criar, e me deparei com esta, em que 
a minha motivação principal seria querer simplificar a parte programática das naves espaciais, já que este assunto de exploração espacial está cada vez mais presente em nosso cotidiano.

Feito por Diogo Duarte


## EBNF

PROGRAM = STATEMENT

BLOCK = "{" STATEMENT "}"

STATEMENT = ( λ | ASSIGNMENT | PRINT | VARIABLE | FLIGHT_CONTROLLER | SPACIAL_COMANDS), "\n"

FLIGHT_CONTROLLER = "pousar" | "decolar" | "ajustar_ângulo"

SPACIAL_COMANDS = "ativar_foguete", "(", INT, ")" | "alinhamento-orbita", "(", INT, ")" | "ajustar_posição", "(", INT, ",", INT, ")"

VARIABLE = "var", IDENTIFIER, TYPE

ASSIGNMENT = IDENTIFIER, "=", EXPRESSION

PRINT = "Print", "(", EXPRESSION, ")"

IF = "if", "(", BOOLEXP, ")", BLOCK, ("else", BLOCK)?

LOOP = "loop", "(", BOOLEXP, ")", BLOCK

BOOLEXP = EXPRESSION, { ("<" | ">" | "==" ), EXPRESSION }

EXPRESSION = TERM, { ("+" | "-"), TERM }

TERM = FACTOR, { ("*" | "/"), FACTOR }

FACTOR = (("+" | "-"), FACTOR) | INT | "(", EXPRESSION, ")" | IDENTIFIER

TYPE = INT | STR 

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" }

INT = DIGIT, { DIGIT }

STR = LETTER, { LETTER | DIGIT}; 

LETTER = ( a | ... | z | A | ... | Z );

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );
