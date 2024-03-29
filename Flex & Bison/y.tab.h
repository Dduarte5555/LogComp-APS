/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    POUSAR = 258,                  /* POUSAR  */
    DECOLAR = 259,                 /* DECOLAR  */
    AJUSTAR_ANGULO = 260,          /* AJUSTAR_ANGULO  */
    ATIVAR_FOGUETE = 261,          /* ATIVAR_FOGUETE  */
    ALINHAMENTO_ORBITA = 262,      /* ALINHAMENTO_ORBITA  */
    AJUSTAR_POSICAO = 263,         /* AJUSTAR_POSICAO  */
    VAR = 264,                     /* VAR  */
    PRINTLN = 265,                 /* PRINTLN  */
    IF = 266,                      /* IF  */
    ELSE = 267,                    /* ELSE  */
    LOOP = 268,                    /* LOOP  */
    LESS_THAN = 269,               /* LESS_THAN  */
    GREATER_THAN = 270,            /* GREATER_THAN  */
    EQUAL = 271,                   /* EQUAL  */
    PLUS = 272,                    /* PLUS  */
    MINUS = 273,                   /* MINUS  */
    MULTIPLY = 274,                /* MULTIPLY  */
    DIVIDE = 275,                  /* DIVIDE  */
    LPAREN = 276,                  /* LPAREN  */
    RPAREN = 277,                  /* RPAREN  */
    COMMA = 278,                   /* COMMA  */
    LBRACE = 279,                  /* LBRACE  */
    RBRACE = 280,                  /* RBRACE  */
    NEWLINE = 281,                 /* NEWLINE  */
    INT = 282,                     /* INT  */
    IDEN = 283,                    /* IDEN  */
    TIME = 284                     /* TIME  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define POUSAR 258
#define DECOLAR 259
#define AJUSTAR_ANGULO 260
#define ATIVAR_FOGUETE 261
#define ALINHAMENTO_ORBITA 262
#define AJUSTAR_POSICAO 263
#define VAR 264
#define PRINTLN 265
#define IF 266
#define ELSE 267
#define LOOP 268
#define LESS_THAN 269
#define GREATER_THAN 270
#define EQUAL 271
#define PLUS 272
#define MINUS 273
#define MULTIPLY 274
#define DIVIDE 275
#define LPAREN 276
#define RPAREN 277
#define COMMA 278
#define LBRACE 279
#define RBRACE 280
#define NEWLINE 281
#define INT 282
#define IDEN 283
#define TIME 284

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 23 "parser.y"

    int intValue;
    char* strValue;

#line 130 "y.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
