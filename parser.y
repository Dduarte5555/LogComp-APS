%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex();
void yyerror(const char* s);

%}

%token POUSAR DECOLAR AJUSTAR_ANGULO ATIVAR_FOGUETE ALINHAMENTO_ORBITA AJUSTAR_POSICAO
%token VAR PRINT IF ELSE LOOP EQ GT LT '+' '-' '*' '/' '(' ')' '{' '}' ',' NUMBER IDENTIFIER TIME_S TIME_M TIME_H

%left '+' '-'
%left '*' '/'

%nonassoc EQ GT LT

%%

program: statement { printf("Programa reconhecido com sucesso!\n"); }
       ;

statement: '\n'
         | assignment '\n'
         | print '\n'
         | variable '\n'
         | flight_controller '\n'
         | spacial_commands '\n'
         | if_statement
         | loop_statement
         ;

assignment: IDENTIFIER '=' expression { printf("Atribuição reconhecida: %s = %f\n", $1, $3); }
          ;

print: PRINT '(' expression ')' { printf("Comando de impressão reconhecido: %f\n", $3); }
     ;

variable: VAR IDENTIFIER { printf("Declaração de variável reconhecida: %s\n", $2); }
        ;

flight_controller: POUSAR
                | DECOLAR
                | AJUSTAR_ANGULO
                ;

spacial_commands: ATIVAR_FOGUETE '(' NUMBER ')' { printf("Comando espacial reconhecido: Ativar foguete com força %f\n", $3); }
               | ALINHAMENTO_ORBITA '(' NUMBER ')' { printf("Comando espacial reconhecido: Alinhamento de órbita com ângulo %f\n", $3); }
               | AJUSTAR_POSICAO '(' coordinates ')' { printf("Comando espacial reconhecido: Ajustar posição para (%f, %f)\n", $3.x, $3.y); }
               ;

coordinates: FLOAT ',' FLOAT { $$ = create_coordinates($1, $3); }
           ;

if_statement: IF '(' boolexp ')' '{' statement '}' { printf("Estrutura if reconhecida.\n"); }
            | IF '(' boolexp ')' '{' statement '}' ELSE '{' statement '}' { printf("Estrutura if-else reconhecida.\n"); }
            ;

loop_statement: LOOP '(' boolexp ')' '{' statement '}' { printf("Estrutura de loop reconhecida.\n"); }
              ;

boolexp: expression EQ expression { printf("Expressão booleana reconhecida: %f == %f\n", $1, $3); }
       | expression GT expression { printf("Expressão booleana reconhecida: %f > %f\n", $1, $3); }
       | expression LT expression { printf("Expressão booleana reconhecida: %f < %f\n", $1, $3); }
       ;

expression: term { $$ = $1; }
          | expression '+' term { $$ = $1 + $3; }
          | expression '-' term { $$ = $1 - $3; }
          ;

term: factor { $$ = $1; }
    | term '*' factor { $$ = $1 * $3; }
    | term '/' factor { $$ = $1 / $3; }
    ;

factor: NUMBER { $$ = $1; }
      | '-' factor { $$ = -$2; }
      | '(' expression ')' { $$ = $2; }
      | IDENTIFIER { $$ = get_variable_value($1); }
      ;

%%