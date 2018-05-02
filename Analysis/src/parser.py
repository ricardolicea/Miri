# coding=utf-8
import ply.yacc as yacc
import os
import codecs
import re
from lexer import tokens
from sys import stdin
# from semantico import *
from cuadruplos import *
from MemoriaV import * 
from structs import *
from VirtualMachine import *




# precedence = (
#     ('right','DO'),
#     ('right','FOR'),
#     ('right','WHILE'),
#     ('right','ID'),
#     ('right','WRITE'),
#     ('right','READ'),
#     ('right','IF'),
#     ('right','MAIN'),
#     ('left','COMMA'),
#     ('right','FUNCTION'),
#     ('right', 'ASSGN'),
#     ('left', 'AND'),
#     ('left', 'OR'),
#     ('left', 'NOTEQ'),
#     ('left', 'EQ'),
#     ('left', 'GRTR', 'GRTREQ', 'LESS', 'LESSEQ'),
#     ('left', 'SUM', 'MINUS'),
#     ('left', 'MULTP', 'DIVIDE'),
#     ('left', 'LEFTPAR', 'RIGHTPAR')

#  )

dirProc = {}
nombrePrograma = ""
nombreModulo = ""
nombreModuloCuad = ""
varsGlobalesDir = {}
auxVarsDir = {}
varsList = {}
tipo = ""
cuad = Cuadruplo("", "", "", "")
Modulos = []
nombreVar = ""
r = 0
iContMat = 0
nombreArr = ""
m1 = 0

def p_program(p):
    '''program : goToMainQuad PROGRAM ID altaPrograma SEMICOLON program2 cuerpo END SEMICOLON''' 
   
def p_goToMainQuad(p):
    '''goToMainQuad : '''
    #print "go to Main Quad"
    goToMainQuad()

# def llamaMV(p):
#     '''llamaMV : '''
#     global dirProc
#     print "hola"
#     MaquinaVirtual(dirProc)


def p_altaPrograma(p):
    '''altaPrograma : '''
    global nombrePrograma
    global dirProc
    nombrePrograma = p[-1]
    dirProc[nombrePrograma] = {}
    dirProc[nombrePrograma] = {'Tipo': 'programa', 'Vars': {}}  
    #print "DIRECTORIO DE PROCEDIMIENTOS VACIO" 
    #print dirProc
    
def p_program2(p):
    '''program2 : declare program3'''

def p_program2Empty(p):
    '''program2 : empty'''
    
def p_declare(p):
    '''declare : DECLARE declareRecursivo '''
    #print "declare"

def p_declareEmpty(p):
    '''declare : empty'''
   
def p_declareRecursivo(p):
    '''declareRecursivo : type ID altaVarGlobal assignmentDecl declare2 declare3 SEMICOLON declareRecursivo'''
    #print "ID"

def p_declare2(p):
    '''declare2 : array '''

def p_dim1(p):
    '''dim1 : '''
    global dirProc
    global iContMat
    var = nombreVar
    if iContMat == 0:
        dirProc[nombreModulo]['Vars'][var]['Dim'] = {'lInf' : 0, 'lSup': 0, 'm': 0, 'dim': None}
    print dirProc

def p_array(p):
    '''array : dim1 LEFTBRACK exp getTam RIGHTBRACK array'''
    #print "[]"
def p_getTam(p):
    '''getTam : '''
    global nombreVar
    global r
    global iContMat
    global dirProc
    global m1

    if iContMat == 1:
        tam = int(pilaOperandos.pop())
        r2 = r
        r = r * (tam - 0 + 1)
        
        lInf = dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['lInf']
        lSup = dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['lSup']
        m1 = r/(lSup - lInf + 1)

        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['m'] = m1
        
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['dim'] = {'lInf' : 0, 'lSup': 0, 'm': 0, 'dim': None}
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['dim']['lInf'] = 0
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['dim']['lSup'] += tam
        
        lInf = dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['dim']['lInf']
        lSup = dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['dim']['lSup']
        
        m2 = m1/(lSup - lInf + 1)
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['dim']['m'] = m2
        tipoArre = dirProc[nombreModulo]['Vars'][nombreVar]['TipoVar']
        scope = dirProc[nombreModulo]['Vars'][nombreVar]['Scope']
        r = r - r2
        actMemoria(r, tipoArre, scope)
        print memFloatTemp
        print dirProc
        iContMat = 0
    else:
        tam = int(pilaOperandos.pop())
        r = 1 * (tam - 0 + 1)
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['lInf'] = 0
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['lSup'] += tam
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['m'] = r
        iContMat += 1
        
        tipoArre = dirProc[nombreModulo]['Vars'][nombreVar]['TipoVar']
        scope = dirProc[nombreModulo]['Vars'][nombreVar]['Scope']

        actMemoria(r, tipoArre, scope)
        print memFloatTemp
    

def p_declare3(p):
    '''declare3 : COMMA  ID altaVarGlobal declare3 '''
    #print ", ID"

def p_program3(p):
    '''program3 : funct program3'''
    
def p_funct(p):
    '''funct : FUNCTION type ID altaModulo LEFTPAR funct2  RIGHTPAR LEFTKEY guardaSalto est functReturn endproc RIGHTKEY'''
    #print "FUNCTION ID"

def p_endProc(p):
    '''endProc : '''
    endproc()

def p_guardaSalto(p):
    '''guardaSalto : '''
    salto = guardaSalto()
    dirProc[nombreModulo]['Cuad'] = salto
    print dirProc

def p_endproc(p):
    '''endproc : '''
    endproc()

def p_functReturn(p):
    '''functReturn : RETURN NUMBER generaRet SEMICOLON'''
    #print "RETURN NUMBER"

def p_functReturnID(p):
    '''functReturn : RETURN ID generaRet SEMICOLON'''
    #print "RETURN ID"

def p_generaRet(p):
    '''generaRet : '''
    generaRet(p[-1])

def p_functReturnEmpty(p):
    '''functReturn : empty'''

def p_altaModulo(p):
    '''altaModulo : '''
    global tipo
    global dirProc
    global nombreModulo
    nombreModulo = p[-1]
    
    #print "-------" + str(nombreModulo)
    dirProc[nombreModulo] = {'Tipo': tipo, 'Vars': {}, 'Cuad': None}
    Modulos.append(nombreModulo)
    #print "DIRECTORIO DE PROCEDIMIENTOS CON MODULOS"
    #print dirProc

def p_funct2(p):
    '''funct2 : type ID altaVarLocal funct3'''
    #print "ID"

def p_funct3(p):
    '''funct3 : COMMA type ID  altaVarLocal funct3'''
    #print ", ID"

def p_funct2Empty(p):
    '''funct2 : empty'''
    
def p_funct3Empty(p):
    '''funct3 : empty'''

def p_program3Empty(p):
    '''program3 : empty'''
   
def p_altaVarGlobal(p):
    '''altaVarGlobal : '''
    global dirProc
    global tipo
    nombreVar = p[-1]
    direccion = set_dir_global(tipo,1)
    dirProc[nombrePrograma]['Vars'][nombreVar] = {'TipoVar': tipo, 'Scope': "global", 'Dir': direccion, 'Dim': None}
    setValueGlobal(direccion,None)
    #print "DIRECTORIO DE PROCEDIMIENTOS CON VARIABLES GLOBALES"
    #print nombreModulo +  " " + str(dirProc)
   
def p_declareResursivoEmpty(p):
    '''declareRecursivo : empty'''
   
def p_declare3Empty(p):
    '''declare3 : empty'''
    

def p_arrayEmpty(p):
    '''array : empty'''
    
def p_type(p):
    '''type : type2'''
   
def p_type2(p):
    '''type2 : INT'''
    global tipo 
    tipo = p[1]
    #print "INT"

def p_type2Float(p):
    '''type2 : FLOAT'''
    global tipo 
    tipo = p[1]
    #print "FLOAT"

def p_type2String(p):
    '''type2 : STRING'''
    global tipo 
    tipo = p[1]
    #print "STRING" 

def p_type2Bool(p):
    '''type2 : BOOL'''
    global tipo 
    tipo = p[1]
    #print "BOOL"

def p_type2Void(p):
    '''type2 : VOID'''
    global tipo 
    tipo = p[1]
    #print "VOID"

def p_cuerpo(p):
    '''cuerpo : MAIN LEFTPAR RIGHTPAR LEFTKEY llenaMain altaModuloMain est endProc RIGHTKEY'''
    #print "MAIN()"

def p_llenaMain(p):
    '''llenaMain : '''
    llenaMain()



def p_altaModuloMain(p):
    '''altaModuloMain : '''
    global tipo
    global dirProc
    global nombreModulo
    nombreModulo = "main"
    dirProc[nombreModulo] = {'Tipo': "Main", 'Vars': {}}
    #print "DIRECTORIO DE PROCEDIMIENTOS CON MODULO MAIN"
    #print dirProc

def p_est(p):
    '''est : conditional est '''
    
def p_estVars(p):
    '''est : declareLocal est'''
    
def p_estCycle(p):
    '''est : cycles est'''
    
def p_estRead(p):
    '''est : input est'''
    
def p_estWrite(p):
    '''est : output est'''
   
def p_estAassignment(p):
    '''est : assignment est'''
   
def p_estFunct(p):
    '''est : llamadaAFunct est'''

    
def p_estEmpty(p):
    '''est : empty'''
    
def p_llamadaAFunct(p):
    '''llamadaAFunct :  ID cuadERA LEFTPAR llamadaAFunct2 gosubCuad  generaCuadFunct RIGHTPAR'''
    

def p_cuadERA(p):
    '''cuadERA : '''
    global nombreModuloCuad
    cuadERA(p[-1])
    nombreModuloCuad = p[-1]
    print nombreModuloCuad

def p_cuadParam(p):
    '''cuadParam : '''
    quadParam()

def p_gosubCuad(p):
    '''gosubCuad : '''
    global dirProc
    global NombreModuloCuad
    salto = dirProc[nombreModuloCuad]['Cuad']
    gosubCuad(p[-5], salto)

def p_llamadaAFunctEmpty(p):
    '''llamadaAFunct : empty'''

def p_llamadaAFunct2(p):
    '''llamadaAFunct2 : exp cuadParam llamadaAFunct3'''
    #print "FUNCT(ID)" 

def p_llamadaAFunct3(p):
    '''llamadaAFunct3 : COMMA llamadaAFunct2'''
    #print "FUCNT(ID,ID)"

def p_llamadaAFunct3Empty(p):
  '''llamadaAFunct3 : empty'''

def p_llamadaAFunct2Empty(p):
    '''llamadaAFunct2 : empty'''
    
def p_declareLocal(p):
    '''declareLocal : DECLARE declareRecursivoLocal '''
    #print "declare" 

def p_declareRecursivoLocal(p):
    '''declareRecursivoLocal : type ID  altaVarLocal assignmentDecl declare2Local declare3Local SEMICOLON declareRecursivoLocal'''
    #print "declareRecursivo"

def p_assignmentDeclare(p):
    '''assignmentDecl : ASSGN meteAssign exp generaCuad'''
    #print "="
def p_meteAssign(p):
    '''meteAssign : '''
    meteAssign(p[-1], p[-3])

def p_number(p):
    '''number : INTEGER meteNum'''
    #print "INT"

def p_numberFloat(p):
    '''number : FLOAT meteNum'''

def p_numberEmpty(p):
    '''number : empty'''


def p_assignmentDeclareEmpty(p):
    '''assignmentDecl : empty'''

def p_declare2Local(p):
    '''declare2Local : array '''
   
def p_declare3Local(p):
    '''declare3Local : COMMA ID altaVarLocal assignmentDecl declare2Local declare3Local '''
   
def p_declareResursivoEmptyLocal(p):
    '''declareRecursivoLocal : empty'''
   
def p_declareEmptyLocal(p):
    '''declareLocal : empty'''
    
def p_declar2EmptyLocal(p):
    '''declare2Local : empty'''
  
def p_declare3EmptyLocal(p):
    '''declare3Local : empty'''
   
def p_altaVarLocal(p):
    '''altaVarLocal : '''
    global dirProc
    global tipo
    global nombreModulo
    global nombreVar
    nombreVar = p[-1]
    direccion = set_dir_local(tipo,1)
    dirProc[nombreModulo]['Vars'][nombreVar] = {'TipoVar': tipo, 'Scope': "local", 'Dir': direccion, 'Dim': None}
    setValueLocal(direccion,None)
    Info = Direc(nombreVar,nombreModulo,direccion)
    pushInfo(Info)
    

    #print "DIRECTORIO DE PROCEDIMIENTOS CON VARIABLES LOCALES"
    #print nombreModulo +  " " + str(dirProc)

def p_assignment(p):
    '''assignment : ID ASSGN  meteVar exp generaCuad SEMICOLON'''
    #print "ID = EXP" 


def p_assignmentFUNCT(p):
    '''assignment : ID ASSGN meteVar llamadaAFunct SEMICOLON'''
    
    #print "ID = EXP" 
    #print "ID = FUNCT()" 
def p_generaCuadFunct(p):
    '''generaCuadFunct : '''
    generaCuadFunct(p[-5])

def p_meteVar(p):
    '''meteVar : '''
    var = p[-2]
    eq = p[-1]
    global nombrePrograma
    #Buscar variable en el modulo
    try:
        temp_dir = dirProc[nombreModulo]['Vars'][var]['Dir']
        temp_tipoVar = dirProc[nombreModulo]['Vars'][var]['TipoVar']
   #Buscar variable en globales
    except KeyError as key:
        try:
            temp_dir = dirProc[nombrePrograma]['Vars'][var]['Dir']
            temp_tipoVar = dirProc[nombrePrograma]['Vars'][var]['TipoVar']
        except KeyError as key:
            print "Variable no %s esta declarada" %key
            sys.exit()
    # print "==============================="
    # print "Var= " + str(var) + "  Tipo= " + str(temp_tipoVar) + "  Dir= " + str(temp_dir)
    # print "==============================="
    quadAssign(eq, var, temp_tipoVar)

def p_assignmentEmpty(p):
    '''assignment : empty'''

def p_conditional(p):
    '''conditional : IF LEFTPAR exp generaCuad RIGHTPAR gotoFCuad LEFTKEY est RIGHTKEY  conditionalElse '''
    #print "IF(){ }"


def p_gotoFCuad(p):
    '''gotoFCuad : '''
    gotoF()

def p_goToCuad(p):
    '''gotoCuad : '''
    gotoCuad()

def p_conditionalElse(p):
    '''conditionalElse : gotoCuad ELSE LEFTKEY est RIGHTKEY llenaGoto '''
    #print "ELSE { }"

def p_llenaGoto(p):
    '''llenaGoto : '''
    llenaGoto()

def p_conditionalElseEmpty(p):
    '''conditionalElse : empty'''
    
def p_conditional2(p):
    '''conditional2 : exp conditional2'''
    
def p_conditional2Empty(p):
    '''conditional2 : empty'''
   
def p_cycles(p):
    '''cycles : while'''
    
def p_cyclesEmpty(p):
    '''cycles : empty'''
    
# def p_cyclesFor(p):
#     '''cycles : for'''
    
def p_cyclesDoWhile(p):
    '''cycles : do-while'''
    
def p_doWhile(p):
    '''do-while : DO meteSalto LEFTKEY est RIGHTKEY WHILE LEFTPAR while2 RIGHTPAR gotoVCuad '''
    
def p_gotoVCuad(p):
    '''gotoVCuad : '''
    gotoVCuad()

def p_meteSalto(p):
    '''meteSalto : '''
    meteSalto()

def p_whileClass(p):
    '''while :  WHILE LEFTPAR while2 RIGHTPAR  gotoFCuad LEFTKEY est RIGHTKEY llenaCuadF '''
    
def p_llenaCuadF(p):
    '''llenaCuadF : '''
    llenaCuadF()

def p_while2(p):
    '''while2 : exp '''
    
def p_while2Empty(p):
    '''while2 : empty'''
    
def p_exp(p):
    '''exp : ID meteExp exp2'''
    #print "ID"

def p_expPar(p):
    '''exp : LEFTPAR metePar exp RIGHTPAR sacaPar exp2 generaCuad'''

def p_metePar(p):
    '''metePar : '''
    metePar(p[-1])

def p_sacaPar(p):
    '''sacaPar : '''
    sacaPar()

def p_meteExp(p):
    '''meteExp : '''
    var = p[-1]

    global nombreModulo
    #Buscar variable en el modulo
    try:
        temp_dir = dirProc[nombreModulo]['Vars'][var]['Dir']
        temp_tipoVar = dirProc[nombreModulo]['Vars'][var]['TipoVar']
   #Buscar variable en globales
    except KeyError as key:
        try:
            temp_dir = dirProc[nombrePrograma]['Vars'][var]['Dir']
            temp_tipoVar = dirProc[nombrePrograma]['Vars'][var]['TipoVar']
        except KeyError as key:
            print "Variable no %s esta declarada" % key
            sys.exit()
    # print "==============================="
    # print "Var= " + str(var) + "  Tipo= " + str(temp_tipoVar) + "  Dir= " + str(temp_dir)
    # print "==============================="
    # print "ID = EXP" 
    quadExp(var, temp_tipoVar)

def p_generaCuad(p):
    '''generaCuad : '''
    generaCuadruplo()

def p_expNUMERO(p):
    '''exp : number exp2'''
    
def p_expArreglo(p):
    '''exp : arreglo exp2'''

def p_expBool(p):
    '''exp : BOOL exp2'''

def p_arreglo(p):
    '''arreglo : ID LEFTBRACK exp cuadVer RIGHTBRACK arreglo2 '''

def p_arreglo2(p):
    '''arreglo2 : LEFTBRACK exp cuadVer2 RIGHTBRACK'''

def p_arreglo2Empty(p):
    '''arreglo2 : empty'''

def p_cuadVer(p):
    '''cuadVer : '''
    global nombreArr
    nombreArr = p[-3]
    lSup = dirProc[nombreModulo]['Vars'][p[-3]]['Dim']['lSup']
    dire = dirProc[nombreModulo]['Vars'][p[-3]]['Dir']
    m = dirProc[nombreModulo]['Vars'][p[-3]]['Dim']['m']
    dim2 = dirProc[nombreModulo]['Vars'][p[-3]]['Dim']['dim']
    cuadVer(p[-3], lSup, dire, m, dim2)

def p_cuadVer2(p):
    '''cuadVer2 : '''
    global nombreArr
    lSup = dirProc[nombreModulo]['Vars'][nombreArr]['Dim']['dim']['lSup']
    dire = dirProc[nombreModulo]['Vars'][nombreArr]['Dir']
    m = dirProc[nombreModulo]['Vars'][nombreArr]['Dim']['dim']['m']
    dim2 = 1
    cuadVer(nombreArr, lSup, dire, m, dim2)

def p_arregloEmpty(p):
    '''arreglo : empty'''

def p_meteNum(p):
    '''meteNum : '''
    
    num = p[-1]
    print num
    quadExp(num,"int" )

def p_expVACIA(p):
    '''exp : empty'''

def p_exp2(p):
    '''exp2 : LESS meteOper exp'''
    #print "<"

def p_expr2Grtr(p):
    '''exp2 : GRTR meteOper exp'''
    #print ">"

def p_exp2Equal(p):
    '''exp2 : EQ meteOper exp'''
    #print "=="

def p_exp2NotEq(p):
    '''exp2 : NOTEQ meteOper exp'''
    #print "!="

def p_exp2And(p):
    '''exp2 : AND meteOper exp'''
    #print "AND"

def p_exp2OR(p):
    '''exp2 : OR meteOper exp'''
    #print "OR"


def p_exp2SUM(p):
    '''exp2 : SUM meteOper exp'''
   
    #print "+"


def p_meteOper(p):
    '''meteOper : '''
    quadOper(p[-1])

def p_exp2MINUS(p):
    '''exp2 : MINUS meteOper exp'''
    #print "-"

def p_exp2MULTP(p):
    '''exp2 : MULTP meteOper exp'''
    #print "*"

def p_exp2DIVIDE(p):
    '''exp2 : DIVIDE meteOper exp'''
    #print "/"

def p_exp2Empty(p):
    '''exp2 : empty'''
    

   
def p_output(p): 
    '''output : WRITE LEFTPAR output2  RIGHTPAR SEMICOLON'''
    #print "WRITE()"

def p_generaWriteCuad(p):
    '''generaWriteCuad : '''
    generaWriteCuad()


def p_meteID(p):
    '''meteID : '''
    meteID(p[-1])

def p_output2(p):
    '''output2 : ID meteID generaWriteCuad output2'''
    #print "WRITE(ID)"

def p_output2Quotes(p):
    '''output2 : QUOTE ID QUOTE output2'''

def p_output2Empty(p):
    '''output2 : empty'''
    
    
def p_input(p):
    '''input : READ LEFTPAR ID meteID generaReadCuad RIGHTPAR SEMICOLON'''
    #print "READ(ID)" 

def p_generaReadCuad(p):
    '''generaReadCuad : '''
    generaReadCuad()

def p_empty(p):
    '''empty :'''
    ##print "Empty"
    pass

def p_circle(p):
    '''circulo : CIRCLE LEFTPAR INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER generaCirculoCuad RIGHTPAR SEMICOLON '''

def p_generaCirculoCuad(p):
    '''generaCirculoCuad : '''
    generaCirculoCuad(p[-9], p[-7], p[-5], p[-3], p[-1])

def p_square(p):
    '''cuadro : LEFTPAR INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON'''

def p_triangle(p):
    '''triangulo : LEFTPAR INTEGER COMMA INTEGER COMMA INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON'''

def p_line(p):
    '''linea : LEFTPAR INTEGER COMMA STRING COMMA INTEGER COMMA INTEGER COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON'''

def p_rectangle(p):
    '''rectangulo : LEFTPAR INTEGER COMMA INTEGER COMMA STRING COMMA BOOL COMMA INTEGER COMMA INTEGER COMMA INTEGER RIGHTPAR SEMICOLON'''


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
#directorio = '/Users/ricardolicea/OneDrive/Tecnológico de Monterrey/8vo Semestre/EM18 Diseño de Compiladores/MIRI/Analysis/test/'
#directorio de la compu del trabajo
#directorio = 'C:/Users/rlicea/Documents/compiladores/Miri/Analysis/test/'
#directorio de miguel
directorio = '/Users/miguelbazan/Documents/ITC 2014/Semestres/8 Octavo Semestre/Compiladores/Final/Miri/Analysis/test/'
#directorio = '/Users/ricardolicea/Desktop/Analysis/test/'
archivo  = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test,"r","utf-8")
cadena  = fp.read()
fp.close()

yacc.yacc()
result = yacc.parse(cadena)

#rent result.traducir()
#traducir(result)


MaquinaVirtual(dirProc)
#print result
print dirProc
print pilaOperandos.getElements()
print pOperadores.getElements()
print cuadruplos
# print "-----------------"
#print VecIntTemp[0]
# print VecFloatTemp[0]
#print VecStringGlobal[0]
# print VecIntLocal[0]
# print dirProc['iSuma']['Vars']['iRes']['Dir']

