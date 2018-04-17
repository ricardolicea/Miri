# coding=utf-8
import ply.yacc as yacc
import os
import codecs
import re
from lexer import tokens
from sys import stdin
from semantico import *

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
dirProc = {}
nombrePrograma = ""
varsGlobalesDir = {}
auxVarsDir = {}
varsList = {}
tipo = ""

def p_program(p):
    '''program : PROGRAM createDirProc ID altaPrograma SEMICOLON program2 cuerpo END SEMICOLON''' 
    print("program")

def p_createDirProc(p):
    '''createDirProc : '''

def p_altaPrograma(p):
    '''altaPrograma : empty'''
    global nombrePrograma
    global dirProc
    nombrePrograma = p[-1]
    dirProc[nombrePrograma] = {}
    dirProc[nombrePrograma] = {'Tipo': 'programa', 'Vars': {'Tipo': ""}}
    
    print dirProc
    

def p_program2(p):
    '''program2 : declare program3'''
    print("program2")

def p_declare(p):
    '''declare : DECLARE declareRecursivo '''
    print("declare")

def p_declareRecursivo(p):
    '''declareRecursivo : type ID altaVar declare2 declare3 SEMICOLON declareRecursivo'''
    print "declareRecursivo"

def p_declare2(p):
    '''declare2 : array'''
    print("declare2")

def p_declare3(p):
    '''declare3 : COMMA  ID altaVar declare3 '''
    print("declare3")

def p_program2Empty(p):
    '''program2 : empty'''
    print("program2 empty)")

def p_program3(p):
    '''program3 : funct program3'''
    print("program3")

def p_funct(p):
    '''funct : FUNCTION type ID altaModulo LEFTPAR funct2  RIGHTPAR LEFTKEY est RIGHTKEY'''
    print("funct")

def p_altaModulo(p):
    '''altaModulo : '''
    global tipo
    global dirProc
    nombreModulo = p[-1]
    print "-------" + str(nombreModulo)
    dirProc[nombreModulo] += {'Tipo': tipo, 'Vars': {'Tipo': ""}}

def p_funct2(p):
    '''funct2 : type ID funct3'''
    print "funct2"

def p_funct3(p):
    '''funct3 : COMMA funct type ID funct3'''
    print("funct3")

def p_funct2Empty(p):
    '''funct2 : empty'''
    print("funct2Empty")

def p_funct3Empty(p):
    '''funct3 : empty'''
    print "funct3 emty"

# def p_altaFunct(p):
#     '''altaFunct :'''
#     nombreFunc = p[-1]
#     dirProc[nombreFunc] = {}
#     dirProc[nombreFunc] = {'Tipo': 'void', 'Vars': {}}
#     print "-------------------"
#     print dirProc
#     print "-------------------"

def p_program3Empty(p):
    '''program3 : empty'''
    print("program3 empty")


def p_altaVar(p):
    '''altaVar : '''
    global dirProc
    global tipo
    nombreVar = p[-1]
    dirProc[nombrePrograma]['Vars'] = nombreVar
    dirProc[nombrePrograma][nombreVar] = {'Tipo': tipo, 'Scope': "global"}
    print nombrePrograma + " " + str(dirProc)
   
	

def p_declareResursivoEmpty(p):
    '''declareRecursivo : empty'''
    print "declare Recursivo Empty"

def p_declareEmpty(p):
    '''declare : empty'''
    print "declareEmpty"


def p_declar2Empty(p):
    '''declare2 : empty'''
    print("declare2 Empty")


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
    '''type : type2'''
    print("type")

def p_type2(p):
    '''type2 : INT'''
    global tipo 
    tipo = p[1]
    print("type2INT")

def p_type2Float(p):
    '''type2 : FLOAT'''
    global tipo 
    tipo = p[1]
    print("type2FLOAT")

def p_type2String(p):
    '''type2 : STRING'''
    global tipo 
    tipo = p[1]
    print("type2STRING")

def p_type2Bool(p):
    '''type2 : BOOL'''
    global tipo 
    tipo = p[1]
    print("type2BOOL")

def p_type2Void(p):
    '''type2 : VOID'''
    global tipo 
    tipo = p[1]
    print("type2VOID")

def p_cuerpo(p):
    '''cuerpo : MAIN LEFTPAR RIGHTPAR LEFTKEY  est RIGHTKEY'''
    print("cuerpo")



def p_est(p):
    '''est : conditional'''
    print("estCONDITIONAL")

def p_estVars(p):
    '''est : declare'''
    print "est Vars"


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

def p_estEmpty(p):
    '''est : empty'''
    print "estEmpty"

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
    p[0] = doWhile(p[3], p[7], "do-while")

def p_whileClass(p):
    '''while : WHILE LEFTPAR while2 RIGHTPAR WHILE LEFTKEY est RIGHTKEY'''
    print("while")

def p_while2(p):
    '''while2 : exp while2'''
    print("while2")

def p_while2Empty(p):
    '''while2 : empty'''
    print("while2Empty")

def p_forClass(p):
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

def traducir(result):
	graphFile = open('graphviztrhee.vz','w')
	graphFile.write(result.traducir())
	graphFile.close()
	print "El programa traducido se guardo en \"graphviztrhee.vz\""
#directorio de la mac
#directorio = '/Users/ricardolicea/OneDrive/Tecnológico de Monterrey/8vo Semestre/EM18 Diseño de Compiladores/MIRI/Analysis/test/'
#directorio de la compu del trabajo
#directorio = 'C:/Users/rlicea/Documents/compiladores/Miri/Analysis/test/'
#directorio de miguel
#directorio = '/Users/miguelbazan/Documents/ITC 2014/Semestres/8 Octavo Semestre/Compiladores/Miri/Analysis/test/'
directorio = '/Users/ricardolicea/Desktop/Analysis/test/'
archivo  = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test,"r","utf-8")
cadena  = fp.read()
fp.close()

yacc.yacc()
result = yacc.parse(cadena)

#rent result.traducir()
#traducir(result)

print result