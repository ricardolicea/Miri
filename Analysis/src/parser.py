# coding=utf-8
import ply.yacc as yacc
import os
import codecs
import re
from lexer import tokens
from sys import stdin

#precedence = (
#    ('right', 'ASSGN'),
#    ('left', 'AND'),
#    ('left', 'OR'),
#    ('left', 'NOTEQ'),
#    ('left', 'EQ'),
#    ('left', 'GRTR', 'GRTREQ', 'LESS', 'LESSEQ'),
#    ('left', 'SUM', 'MINUS'),
#    ('left', 'MULTP', 'DIVIDE'),
#    ('left', 'LEFTPAR', 'RIGHTPAR')

#)

def p_program(p):
    '''program : PROGRAM ID SEMICOLON program2 cuerpo END SEMICOLON''' 
    print "program"

def p_program2(p):
    '''program2 : declare program3'''
    print "program2"

def p_program2Empty(p):
    '''program2 : empty'''
    print "program2 empty"

def p_program3(p):
    '''program3 : funct program3'''
    print "program3" 

def p_program3Empty(p):
    '''program3 : empty'''
    print("program3 empty")

def p_declare(p):
    '''declare : DECLARE type ID declare2 declare3 SEMICOLON'''
    print("declare")

def p_declare2(p):
    '''declare2 : array'''
    print("declare2")

def p_declar2Empty(p):
    '''declare2 : empty'''
    print("declare2 Empty")

def p_declare3(p):
    '''declare3 : COMMA declare3'''
    print("declare3")

def p_declare3Empty(p):
    '''declare3 : empty'''
    print("declare3 Empty")

def p_array(p):
    '''array : LEFTBRACK exp RIGHTBRACK array'''
    print("array")

def p_arrayEmpty(p):
    '''array : empty'''
    print("array Empty")

def p_type(p):
    '''type : TYPE type2'''
    print("type")

def p_type2(p):
    '''type2 : INT'''
    print("type2INT")

def p_type2Float(p):
    '''type2 : FLOAT'''
    print("type2FLOAT")

def p_type2String(p):
    '''type2 : STRING'''
    print("type2STRING")

def p_type2Bool(p):
    '''type2 : BOOL'''
    print("type2BOOL")

def p_type2Void(p):
    '''type2 : VOID'''
    print("type2VOID")

def p_cuerpo(p):
    '''cuerpo : MAIN LEFTPAR RIGHTPAR LEFTKEY cuerpo2 RIGHTKEY'''
    print("cuerpo")

def p_cuerpo2(p):
    '''cuerpo2 : est'''
    print("cuerpo2")

def p_cuerpo2Empty(p):
    '''cuerpo2 : empty'''
    print("cuerpo2 empty")

def p_est(p):
    '''est : conditional'''
    print("estCONDITIONAL")

def p_estCycle(p):
    '''est : cycles'''
    print("estCYLE")

def p_estRead(p):
    '''est : input'''
    print("estREAD")

def p_estWrite(p):
    '''est : output'''
    print("estWRITE")

def p_estAassignment(p):
    '''est : assignment'''
    print("estASSIGNMENT")

def p_estFunct(p):
    '''est : funct'''
    print("estFUNCT")

def p_assignment(p):
    '''assignment : ID ASSGN ID SEMICOLON'''
    print("assignment")

def p_conditional(p):
    '''conditional : IF LEFTPAR conditional2 RIGHTPAR LEFTKEY est RIGHTKEY ELSE est RIGHTKEY'''
    print("conditional")

def p_conditional2(p):
    '''conditional2 : exp conditional2'''
    print("conditional2")

def p_conditional2Empty(p):
    '''conditional2 : empty'''
    print("conditional Empty")

def p_cycles(p):
    '''cycles : while'''
    print("cyclesWhile")

def p_cyclesFor(p):
    '''cycles : for'''
    print("cyclesFor")

def p_cyclesDoWhile(p):
    '''cycles : do-while'''
    print("cyclesDoWhile")

def p_doWhile(p):
    '''do-while : DO LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPAR'''

def p_while(p):
    '''while : WHILE LEFTPAR while2 RIGHTPAR WHILE LEFTKEY est RIGHTKEY'''
    print("while")

def p_while2(p):
    '''while2 : exp while2'''
    print("while2")

def p_while2Empty(p):
    '''while2 : empty'''
    print("while2Empty")

def p_for(p):
    '''for : FOR LEFTPAR for2 SEMICOLON for3 SEMICOLON ID arithmeticOp arithmeticOp RIGHTPAR LEFTKEY est RIGHTKEY'''
    print("for")

def p_arithmeticOpPlus(p):
    '''arithmeticOp : SUM'''
    print("arithmeticOpPlus")

def p_arithmeticOpMinus(p):
    '''arithmeticOp : MINUS'''
    print("ArithmeticOpMinus")

    #FALTA AGREGAR LAS DE MULTP Y DIIVDE

def p_for2(p):
    '''for2 : ID ASSGN ID for2'''
    print("for2")

def p_for2empty(p):
    '''for2 : empty'''
    print("for2EMPTY")

def p_for3(p):
    '''for3 : exp for3'''
    print("for3")

def p_for3empty(p):
    '''for3 : empty'''
    print("empty")

def p_exp(p):
   '''exp : ID array exp2 SEMICOLON'''
   print("exp")

def p_exp2(p):
    '''exp2 : LESS'''
    print("exp2LESS")

def p_expr2Grtr(p):
    '''exp2 : GRTR'''
    print("exp2GRTR")


def p_exp2Equal(p):
    '''exp2 : EQ'''
    print("exp2EQUAL")

def p_exp2NotEq(p):
    '''exp2 : NOTEQ'''
    print("exp2NOTEQU")

def p_exp2And(p):
    '''exp2 : AND'''
    print("exp2AND")

def p_exp2OR(p):
    '''exp2 : OR'''
    print("exp2OR")

def p_exp2Arithemti(p):
    '''exp2 : arithmeticExp'''
    print("exp2ArithmeticExp")

def p_arithmeticExp(p):
    '''arithmeticExp : ID EQ ID arithmeticOp ID arithmeticExp'''
    print("arithmeticexp")

def p_arithmeticExpEmpty(p):
    '''arithmeticExp : empty'''
    print("Arithmetic Exp Empty")

def p_exp2Empty(p):
    '''exp2 : empty'''
    print("exp2Empty")

def p_output(p): 
    '''output : WRITE LEFTPAR output2 QUOTE exp QUOTE RIGHTPAR SEMICOLON'''
    print("output")

def p_output2(p):
    '''output2 : ID output2'''
    print("output2")

def p_output2Empty(p):
    '''output2 : empty'''
    print("exp2Empty")

def p_input(p):
    '''input : READ LEFTPAR ID RIGHTPAR SEMICOLON'''
    print("input")

def p_funct(p):
    '''funct : FUNCTION type ID LEFTPAR type ID funct2 RIGHTPAR LEFTKEY est RIGHTKEY'''
    print("funct")

def p_funct2(p):
    '''funct2 : COMMA funct type ID funct2'''
    print("funct2")

def p_funct2Empty(p):
    '''funct2 : empty'''
    print("funct2Empty")

def p_empty(p):
    '''empty :'''
    pass
def p_error(p):
    print("Error de sintxis", p)
    print("Error en la linea " + str(p.lineno))

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    contador = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    for file in files: 
        print str(contador) + ". " + file
        contador = contador + 1

    while respuesta == False:
        numArchivo = raw_input('\nNumero de test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break
    
    print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]
    return files[int(numArchivo)-1]
#directorio de la mac
#directorio = '/Users/ricardolicea/OneDrive/Tecnológico de Monterrey/8vo Semestre/EM18 Diseño de Compiladores/MIRI/Analysis/test/'
#directorio de la compu del trabajo
directorio = 'C:/Users/rlicea/Documents/compiladores/Miri/Analysis/test/'
archivo  = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test,"r","utf-8")
cadena  = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print result