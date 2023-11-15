%{
#include "y.tab.h"
%}

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
"("                        { return '('; }
")"                        { return ')'; }
"{"                        { return '{'; }
"}"                        { return '}'; }
","                        { return ','; }
"=="                       { return EQ; }
">"                        { return GT; }
"<"                        { return LT; }
"+"                        { return '+'; }
"-"                        { return '-'; }
"*"                        { return '*'; }
"/"                        { return '/'; }
"s"                        { return TIME_S; }
"m"                        { return TIME_M; }
"h"                        { return TIME_H; }
[0-9]+                     { yylval.floatval = atof(yytext); return NUMBER; }
[ \t\n]                    ;  // Ignorar espaços em branco e quebras de linha
[a-zA-Z_][a-zA-Z0-9_]*     { yylval.strval = strdup(yytext); return IDENTIFIER; }

%%