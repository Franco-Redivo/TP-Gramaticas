grammar Residuos;

program
    : function+ EOF
    ;

function
    : 'function' VARIABLE '(' parameterList? ')' block
    ;

parameterList
    : VARIABLE (',' VARIABLE)*
    ;

block
    : '{' statement* '}'
    ;

statement
    : assignStatement
    | ifStatement
    | returnStatement
    ;

assignStatement
    : VARIABLE '=' expression ';'
    ;

ifStatement
    : 'if' '(' booleanExpression ')' block ('else' block)?
    ;

functionCall
    : VARIABLE '(' argumentList? ')'
    ;

argumentList
    : expression (',' expression)*
    ;

returnStatement
    : 'return' expression ';'
    ;

booleanExpression
    : expression COMPARISON_OPERATOR expression
    ;

expression
    : expression '+' expression
    | functionCall
    | STRING
    | NUMBER
    | VARIABLE
    ;

COMPARISON_OPERATOR
    : '=='
    | '!='
    | '>'
    | '<'
    | '>='
    | '<='
    ;

VARIABLE
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

STRING
    : '"' .*? '"'
    ;

NUMBER
    : [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

