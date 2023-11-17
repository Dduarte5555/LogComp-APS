%{
#include "parser.tab.h"
%}

%%
"pousar"                   { return POUSAR; }
"decolar"                  { return DECOLAR; }
"ajustar-ângulo"           { return AJUSTAR_ANGULO; }
"ativar-foguete"           { return ATIVAR_FOGUETE; }
"alinhamento-orbita"       { return ALINHAMENTO_ORBITA; }
"ajustar-posição"          { return AJUSTAR_POSICAO; }
"var"                      { return VAR; }
"Println"                    { return PRINTLN; }
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
[0-9]+                   { yylval.intValue = atoi(yytext); return INT; }
[ \t\n]                    ;  // Ignorar espaços em branco e quebras de linha
[a-zA-Z_][a-zA-Z0-9_]*     { yylval.strValue = strdup(yytext); return IDEN; }
[0-9]+:[0-9]+:[0-9]+		{ yylval.strValue = strdup(yytext); return TIME;}
%%
