grammar Miri;

/*
Created by: Ricardo Licea and Miguel Bazan
*/

//************************************************
//************************************************
//                SCANNER
//************************************************
//************************************************


//------------------------------------------------
//                RESERVED WORDS
//------------------------------------------------
PROGRAM: 'program';
END: 'end';
DECLARE: 'declare';
MAIN: 'main';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
DO_WHILE: 'do';
WRITE: 'write';
READ: 'read';
FUNCTION: 'funct';
ARCH: 'arch';
CIRCLE: 'circle';
SQUARE: 'square';
AND: 'and';
OR: 'or';
RETURN: 'return';
PAINT: 'paint';

//------------------------------------------------
//                dataTypeS
//------------------------------------------------

BOOL: ('true' | 'false');
FLOAT: ('0' .. '9')+ '.' ('0' .. '9')+;
ID: ('a' .. 'z')('a' .. 'z' | 'A' .. 'Z'|'0' .. '9')*;
INT: ('0'..'9')+;
STRING: '\'' ( ~( '\'' | '\\' ) | '\\' . )* '\'' | '"'  ( ~( '"'  | '\\' ) | '\\' . )* '"';
//VOID: ;



//------------------------------------------------
//                CHARACTERS
//------------------------------------------------
ASSGN: '=';
COMMA: ',';
SEMICOLON:';';
DOT: '.';
COLON: ':';
LEFTBRACK: '[';
RIGHTBRACK: ']';
LEFTPAR: '(';
RIGHTPAR: ')';
LEFTKEY: '{';
RIGHTKEY: '}';
QUOTE: '"';

//------------------------------------------------
//                OPERATORS
//------------------------------------------------
SUM: '+';
MINUS: '-';
MULTP: '*';
DIVIDE: '/';
GRTR: '>';
LESS: '<';
EQ: '==';
NOTEQ: '!=';
GRTREQ: '>=';
LESSEQ: '<=';



//************************************************
//************************************************
//                PARSER
//************************************************
//************************************************

program: PROGRAM ID SEMICOLON (DECLARE llamada_f | cuerpo ) END SEMICOLON;
declare: DECLARE dataType ID (COLON | SEMICOLON | array);
dataType: INT| FLOAT | STRING | BOOL;
array: LEFTBRACK exp (RIGHTBRACK LEFTBRACK exp RIGHTBRACK)? RIGHTBRACK SEMICOLON;
cuerpo: MAIN LEFTPAR RIGHTPAR LEFTKEY estatutos RIGHTKEY;
estatutos: conditional | cycle | READ | WRITE | assignment | llamada_f;
assignment: ID (array)? ASSGN (ID | FUNCTION) SEMICOLON;
conditional: IF LEFTPAR exp+ RIGHTPAR LEFTKEY estatutos RIGHTKEY (ELSE LEFTKEY estatutos RIGHTKEY)?;
cycle: while | do_while | for;
while: WHILE LEFTPAR exp RIGHTPAR LEFTKEY estatutos RIGHTKEY;
do_while: DO_WHILE LEFTKEY estatutos RIGHTKEY WHILE LEFTPAR exp RIGHTPAR;
for: FOR LEFTPAR (ID ASSGN ID (COMMA?))* SEMICOLON (exp (COMMA?))* SEMICOLON (ID arithmeticOperator arithmeticOperator(COMMA?))* RIGHTPAR LEFTKEY estatutos RIGHTKEY;
exp: (ID (array)? (GRTR | LESS | GRTREQ | LESSEQ | EQ | NOTEQ | AND | OR | arithmeticOperator))* ASSGN;
output: WRITE LEFTPAR (((QUOTE exp QUOTE | ID | geofig)+)  ) RIGHTPAR SEMICOLON;
inputData: READ LEFTPAR (ID (array)? (COMMA)?)+ RIGHTPAR SEMICOLON;
llamada_f:FUNCTION dataType ID LEFTPAR (dataType ID)? RIGHTPAR LEFTKEY estatutos RIGHTKEY;
arithmeticOperator: SUM | MINUS | MULTP | DIVIDE | ASSGN;
geofig: circle | square | arch;
circle: CIRCLE LEFTPAR exp COMMA exp COMMA exp COMMA exp COMMA exp RIGHTPAR SEMICOLON;
square: SQUARE LEFTPAR exp COMMA exp COMMA exp COMMA exp COMMA exp COMMA exp RIGHTPAR SEMICOLON;
arch: ARCH LEFTPAR exp COMMA exp COMMA exp COMMA exp COMMA exp RIGHTPAR SEMICOLON;









program::= PROGRAM ID SEMICOLON (DECLARE llamada_f | cuerpo ) END SEMICOLON;
declare::= DECLARE dataType ID (COLON | SEMICOLON | array);
dataType::= INT| FLOAT | STRING | BOOL;
array::= LEFTBRACK exp (RIGHTBRACK LEFTBRACK exp RIGHTBRACK)? RIGHTBRACK SEMICOLON;
cuerpo::= MAIN LEFTPAR RIGHTPAR LEFTKEY estatutos RIGHTKEY;
estatutos::= conditional | cycle | READ | WRITE | assignment | llamada_f;
assignment::= ID (array)? ASSGN (ID | FUNCTION) SEMICOLON;
conditional::= IF LEFTPAR exp+ RIGHTPAR LEFTKEY estatutos RIGHTKEY (ELSE LEFTKEY estatutos RIGHTKEY)?;
cycle::= while | do_while | for;
while::= WHILE LEFTPAR exp RIGHTPAR LEFTKEY estatutos RIGHTKEY;
do_while::= DO_WHILE LEFTKEY estatutos RIGHTKEY WHILE LEFTPAR exp RIGHTPAR;
for::= FOR LEFTPAR (ID ASSGN ID (COMMA?))* SEMICOLON (exp (COMMA?))* SEMICOLON (ID arithmeticOperator arithmeticOperator(COMMA?))* RIGHTPAR LEFTKEY estatutos RIGHTKEY;
exp::= (ID (array)? (GRTR | LESS | GRTREQ | LESSEQ | EQ | NOTEQ | AND | OR | arithmeticOperator))* ASSGN;
output::= WRITE LEFTPAR (((QUOTE exp QUOTE | ID | geofig)+)  ) RIGHTPAR SEMICOLON;
inputData::= READ LEFTPAR (ID (array)? (COMMA)?)+ RIGHTPAR SEMICOLON;
llamada_f::= FUNCTION dataType ID LEFTPAR (dataType ID)? RIGHTPAR LEFTKEY estatutos RIGHTKEY;
arithmeticOperator::= SUM | MINUS | MULTP | DIVIDE | ASSGN;
geofig::= circle | square | arch;
circle::= CIRCLE LEFTPAR exp COMMA exp COMMA exp COMMA exp COMMA exp RIGHTPAR SEMICOLON;
square::= SQUARE LEFTPAR exp COMMA exp COMMA exp COMMA exp COMMA exp COMMA exp RIGHTPAR SEMICOLON;
arch::= ARCH LEFTPAR exp COMMA exp COMMA exp COMMA exp COMMA exp RIGHTPAR SEMICOLON;


SSGN::= '=';
COMMA::= ',';
SEMICOLON::=';';
DOT::= '.';
COLON::= ':';
LEFTBRACK::= '[';
RIGHTBRACK::= ']';
LEFTPAR::= '(';
RIGHTPAR::= ')';
LEFTKEY::='{';
RIGHTKEY::= '}';
QUOTE::= '"';

SUM::= '+';
MINUS::= '-';
MULTP::= '*';
DIVIDE::= '/';
GRTR::= '>';
LESS::= '<';
EQ::= '==';
NOTEQ::= '!=';
GRTREQ::= '>=';
LESSEQ::= '<=';