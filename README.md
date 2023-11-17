# LogComp-APS

Criação de uma linguagem de programação voltada para missões espaciais. Essa ideia saiu de uma pesquisa de qual linguagem criar, e me deparei com esta, em que 
a minha motivação principal seria querer simplificar a parte programática das naves espaciais, já que este assunto de exploração espacial está cada vez mais presente em nosso cotidiano.

Feito por Diogo Duarte


## EBNF

PROGRAM = STATEMENT;

BLOCK = "{" STATEMENT "}";

STATEMENT = ( λ | ASSIGNMENT | PRINT | VARIABLE | FLIGHT_CONTROLLER | SPACIAL_COMANDS), "\n";

FLIGHT_CONTROLLER ::= "pousar" | "decolar" | "ajustar-ângulo";

SPACIAL_COMANDS = "ativar-foguete", "(", INT, ")" | "alinhamento-orbita", "(", INT, ")" | "ajustar-posição", "(", COORDINATES, ")";

VARIABLE = "var", IDENTIFIER, <tipo-dado>;

ASSIGNMENT = IDENTIFIER, "=", EXPRESSION;

PRINT = "Print", "(", EXPRESSION, ")";

IF = "if", "(", BOOLEXP, ")", BLOCK, ("else", BLOCK)?;

LOOP = "loop", "(", BOOLEXP, ")", BLOCK;

BOOLEXP = EXPRESSION, { ("<" | ">" | "==" ), EXPRESSION } ;

EXPRESSION = TERM, { ("+" | "-"), TERM };

TERM = FACTOR, { ("*" | "/"), FACTOR };

FACTOR = (("+" | "-"), FACTOR) | INT | "(", EXPRESSION, ")" | IDENTIFIER;

TYPE = INT | COORDINATES | TIME;

COORDINATES = "(", INT, ",", INT, ",", ")";

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

TIME = INT, "s" | INT, "m" | INT, "h";

INT = DIGIT, { DIGIT };

LETTER = ( a | ... | z | A | ... | Z );

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );
