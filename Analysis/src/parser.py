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
    '''program : PROGRAM ID  SEMICOLON program2 cuerpo END SEMICOLON''' 
    #p[0] = program(p[4], p[5], "program")
    print("program")

def p_program2(p):
    '''program2 : declare program3'''
    #p[0] = program2(p[1],p[2], "program2")
    print("program2")

def p_program2Empty(p):
    '''program2 : empty'''
    #p[0] = null()
    print("program2 empty)")

def p_program3(p):
    '''program3 : funct program3'''
    #p[0] = program3(p[1], p[2], "program3")
    print("program3")

def p_program3Empty(p):
    '''program3 : empty'''
    #p[0] = null()
    print("program3 empty")

def p_declare(p):
    '''declare : DECLARE declareRecursivo '''
    #p[0] = declare(p[2], "declare")
    print("declare")

def p_declareRecursivo(p):
    '''declareRecursivo : type ID declare2 declare3 SEMICOLON declareRecursivo'''
    #p[0] = declareRecursivo(p[1], p[3], p[4], p[6], "declareRecursivo")
    print "declareRecursivo"

def p_declareResursivoEmpty(p):
    '''declareRecursivo : empty'''
    #p[0] = null()
    print "declare Recursivo Empty"

def p_declareEmpty(p):
    '''declare : empty'''
    #p[0] = null()
    print "declareEmpty"

def p_declare2(p):
    '''declare2 : array'''
    #p[0] = declare2(p[1])
    print("declare2")

def p_declar2Empty(p):
    '''declare2 : empty'''
    #p[0] = null()
    print("declare2 Empty")

def p_declare3(p):
    '''declare3 : COMMA  ID declare3 '''
    #p[0] = declare3(p[3], "declare3")
    print("declare3")

def p_declare3Empty(p):
    '''declare3 : empty'''
    #p[0] = null()
    print("declare3 Empty")

def p_array(p):
    '''array : LEFTBRACK exp RIGHTBRACK array'''
    #p[0] = array(p[2], p[4], "array")
    print("array")

def p_arrayEmpty(p):
    '''array : empty'''
    #p[0] = null()
    print("array Empty")

def p_type(p):
    '''type : type2'''
    #p[0] = typeClass(p[1], "typeClass")
    print("type")

def p_type2(p):
    '''type2 : INT'''
    #p[0] = type2(Int(p[1]), "type2")
    print("type2INT")

def p_type2Float(p):
    '''type2 : FLOAT'''
    #p[0] = type2Float(Float(p[1]),"type2Float")
    print("type2FLOAT")

def p_type2String(p):
    '''type2 : STRING'''
    #p[0] = type2String(String(p[1]), "type2String")
    print("type2STRING")

def p_type2Bool(p):
    '''type2 : BOOL'''
    #p[0] = type2Bool(Bool(p[1]), "type2Bool")
    print("type2BOOL")

def p_type2Void(p):
    '''type2 : VOID'''
    #p[0] = type2Void(Void(p[1]), "type2Void")
    print("type2VOID")

def p_cuerpo(p):
    '''cuerpo : MAIN LEFTPAR RIGHTPAR LEFTKEY cuerpo2 est RIGHTKEY'''
    #p[0] = cuerpo(p[5], p[6], "cuerpo")
    print("cuerpo")

def p_cuerpo2(p):
    '''cuerpo2 : cuerpo'''
    #p[0] = cuerpo2(p[1], "cuerpo2")
    print("cuerpo2")

def p_cuerpo2Empty(p):
    '''cuerpo2 : empty'''
    #p[0] = null()
    print("cuerpo2 empty")

def p_est(p):
    '''est : conditional'''
    #p[0] = est(p[1], "est")
    print("estCONDITIONAL")

def p_estCycle(p):
    '''est : cycles'''
    #p[0] = estCycle(p[1], "estCycle")
    print("estCYLE")

def p_estRead(p):
    '''est : input'''
    #p[0] = estRead(p[1], "estRead")
    print("estREAD")

def p_estWrite(p):
    '''est : output'''
    #p[0] = estWrite(p[1], "estWrite")
    print("estWRITE")

def p_estAassignment(p):
    '''est : assignment'''
    #p[0] = estAassignment(p[1], "estAssignment")
    print("estASSIGNMENT")

def p_estFunct(p):
    '''est : funct'''
    #p[0] = estFunct(p[1], "estFunct")
    print("estFUNCT")
def p_estEmpty(p):
    '''est : empty'''
    #p[0] = null()
    print "estEmpty"

def p_assignment(p):
    '''assignment : ID ASSGN ID SEMICOLON'''
    #p[0] = assignment(Id(p[1]), Assign(p[2]), Id(p[3]), "assignment")
    print("assignment")

def p_conditional(p):
    '''conditional : IF LEFTPAR conditional2 RIGHTPAR LEFTKEY est RIGHTKEY ELSE est RIGHTKEY'''
    #p[0] = conditional(p[3], p[6], p[9], "conditional")
    print("conditional")

def p_conditional2(p):
    '''conditional2 : exp conditional2'''
    #p[0] = conditional2(p[1], [p2], "conditional2")
    print("conditional2")

def p_conditional2Empty(p):
    '''conditional2 : empty'''
    #p[0] = null()
    print("conditional Empty")

def p_cycles(p):
    '''cycles : while'''
    #p[0] = cycles(p[1], "cycles")
    print("cyclesWhile")

def p_cyclesFor(p):
    '''cycles : for'''
    #p[0] = cyclesFor(p[1], "cyclesFor")
    print("cyclesFor")

def p_cyclesDoWhile(p):
    '''cycles : do-while'''
    #p[0] = cyclesDoWhile(p[1], "cyclesDoWhile")
    print("cyclesDoWhile")

def p_doWhile(p):
    '''do-while : DO LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPAR'''
    #p[0] = doWhile(p[3], p[7], "do-while")
def p_whileClass(p):
    '''while : WHILE LEFTPAR while2 RIGHTPAR WHILE LEFTKEY est RIGHTKEY'''
    #p[0] = whileClass(p[3], p[7], "while")
    print("while")

def p_while2(p):
    '''while2 : exp while2'''
    #p[0] = while2(p[1], p[2], "while2")
    print("while2")

def p_while2Empty(p):
    '''while2 : empty'''
    #p[0] = null()
    print("while2Empty")

def p_forClass(p):
    '''for : FOR LEFTPAR for2 SEMICOLON for3 SEMICOLON ID arithmeticOp arithmeticOp RIGHTPAR LEFTKEY est RIGHTKEY'''
    #p[0] = forClass(p[3], p[5], p[7], p[8], p[11], "for")
    print("for")

def p_arithmeticOpPlus(p):
    '''arithmeticOp : SUM'''
    #p[0] = arithmeticOp(Sum(p[1), "arithmeticOp")
    print("arithmeticOpPlus")

def p_arithmeticOpMinus(p):
    '''arithmeticOp : MINUS'''
    #p[0] = arithmeticOpMinus(Minus(p[1]), "arithmeticOperatoriMinus")
    print("ArithmeticOpMinus")

    #FALTA AGREGAR LAS DE MULTP Y DIIVDE

def p_for2(p):
    '''for2 : ID ASSGN ID for2'''
    #p[0] = for2(Id(p[1]), Assign(p[2]), Id(p[3]), p[4], "for2")
    print("for2")

def p_for2empty(p):
    '''for2 : empty'''
    #p[0] = null()
   #print("for2EMPTY")

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
    print "Empty"
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
#directorio = 'C:/Users/rlicea/Documents/compiladores/Miri/Analysis/test/'
#directorio de miguel
directorio = '/Users/miguelbazan/Documents/ITC 2014/Semestres/8 Octavo Semestre/Compiladores/Miri/Analysis/test/'
archivo  = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test,"r","utf-8")
cadena  = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print result