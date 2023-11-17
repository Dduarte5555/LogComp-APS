%{
#include "parser.tab.h"
%}

%option noyywrap

DIGIT [0-9]
LETTER [a-zA-Z]

%%
"pousar"                   { return POUSAR; }
"decolar"                  { return DECOLAR; }
"ajustar-ângulo"           { return AJUSTAR_ANGULO; }
"ativar-foguete"           { return ATIVAR_FOGUETE; }
"alinhamento-orbita"       { return ALINHAMENTO_ORBITA; }
"ajustar-posição"          { return AJUSTAR_POSICAO; }
"var"                      { return VAR; }
"Print"                    { return PRINT; }
"if"                       { return IF; }
"else"                     { return ELSE; }
"loop"                     { return LOOP; }
"<"                        { return LESS_THAN; }
">"                        { return GREATER_THAN; }
"=="                       { return EQUAL; }
"+"                        { return PLUS; }
"-"                        { return MINUS; }
"*"                        { return MULTIPLY; }
"/"                        { return DIVIDE; }
"("                        { return LPAREN; }
")"                        { return RPAREN; }
","                        { return COMMA; }
"{"                        { return LBRACE; }
"}"                        { return RBRACE; }
"\n"                       { return NEWLINE; }
{DIGIT}+                   { yylval.intValue = atoi(yytext); return INT; }
{LETTER}({LETTER}|{DIGIT}|"_"|)* { yylval.strValue = strdup(yytext); return IDENTIFIER; }
%%

int yywrap() {
    return 1;
}