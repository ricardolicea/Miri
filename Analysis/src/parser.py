
# coding=utf-8
############################################################
#Nombre del archivo: parser.py
#Autores: 
# Ricardo Licea Mata A01280892
# Miguel Bazan Aviña A01281010
#
#Función del archivo:
#Este archivo corresponde al analizador sintáctico del compilador.
#A traves de producciones, define la gramática del compilador, importando
#los tokens del analizador léxico. Aqui, estan insertados las acciones
#semanticas para la generación de código intermedio, asi como la creación
#e indexamiento de las tablas de variables.
#
#
#############################################################


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
from maqVirt import *




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

DiccCopy = []
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
    
    
def p_program2(p):
    '''program2 : declare program3'''

def p_program2Empty(p):
    '''program2 : empty'''
    
def p_declare(p):
    '''declare : DECLARE declareRecursivo '''
    

def p_declareEmpty(p):
    '''declare : empty'''
   
def p_declareRecursivo(p):
    '''declareRecursivo : type ID altaVarGlobal assignmentDecl declare2 declare3 SEMICOLON declareRecursivo'''


def p_declare2(p):
    '''declare2 : array '''

def p_dim1(p):
    '''dim1 : '''
    global dirProc
    global iContMat
    var = nombreVar
    if iContMat == 0:
        dirProc[nombreModulo]['Vars'][var]['Dim'] = {'lInf' : 0, 'lSup': 0, 'm': 0, 'dim': None}
    

def p_array(p):
    '''array : dim1 LEFTBRACK exp getTam RIGHTBRACK array'''
    
def p_getTam(p):
    '''getTam : '''
    global nombreVar
    global r
    global iContMat
    global dirProc
    global m1

    if iContMat == 1:
        # tam = int(pilaOperandos.pop())
        tam = quitaPor(pilaOperandos.pop())
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
        iContMat = 0
    else:
        # tam = int(pilaOperandos.pop())
        tam = quitaPor(pilaOperandos.pop())
        r = 1 * (tam - 0 + 1)
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['lInf'] = 0
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['lSup'] += tam
        dirProc[nombreModulo]['Vars'][nombreVar]['Dim']['m'] = r
        iContMat += 1
        
        tipoArre = dirProc[nombreModulo]['Vars'][nombreVar]['TipoVar']
        scope = dirProc[nombreModulo]['Vars'][nombreVar]['Scope']

        actMemoria(r, tipoArre, scope)
        

def p_declare3(p):
    '''declare3 : COMMA  ID altaVarGlobal declare3 '''
    

def p_program3(p):
    '''program3 : funct program3'''
    
def p_funct(p):
    '''funct : FUNCTION type ID altaModulo LEFTPAR funct2  RIGHTPAR LEFTKEY guardaSalto est functReturn endproc RIGHTKEY'''
    

def p_endProc(p):
    '''endProc : '''
    endproc()

def p_guardaSalto(p):
    '''guardaSalto : '''
    salto = guardaSalto()
    dirProc[nombreModulo]['Cuad'] = salto
    

def p_endproc(p):
    '''endproc : '''
    endproc()

def p_functReturnExp(p):
    '''functReturn : RETURN exp generaRet SEMICOLON'''

def p_functReturn(p):
    '''functReturn : RETURN NUMBER generaRet SEMICOLON'''
    

def p_functReturnID(p):
    '''functReturn : RETURN ID generaRet SEMICOLON'''
    

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
    
    
    dirProc[nombreModulo] = {'Tipo': tipo, 'Vars': {}, 'Cuad': None, 'Par': {}}
    Modulos.append(nombreModulo)
    

def p_funct2(p):
    '''funct2 : type ID altaPar funct3'''
    

def p_funct3(p):
    '''funct3 : COMMA type ID  altaPar funct3'''
   
def p_altaPar(p):
    '''altaPar : '''
    global dirProc
    global tipo
    global nombreModulo
    global nombreVar
    nombreVar = p[-1]
    direccion = set_dir_local(tipo,1)
    dirProc[nombreModulo]['Par'][nombreVar] = {'TipoVar': tipo, 'Scope': "local", 'Dir': direccion, 'Dim': None}
    setValueLocal(direccion,None)
    Info = Direc(nombreVar,nombreModulo,direccion)
    pushInfo(Info)

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
    

def p_type2Float(p):
    '''type2 : FLOAT'''
    global tipo 
    tipo = p[1]
    

def p_type2String(p):
    '''type2 : STRING'''
    global tipo 
    tipo = p[1]
    

def p_type2Bool(p):
    '''type2 : BOOL'''
    global tipo 
    tipo = p[1]
    

def p_type2Void(p):
    '''type2 : VOID'''
    global tipo 
    tipo = p[1]
    

def p_cuerpo(p):
    '''cuerpo : MAIN LEFTPAR RIGHTPAR LEFTKEY llenaMain altaModuloMain est endProc RIGHTKEY'''
    

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
    

def p_est(p):
    '''est : conditional est '''

def p_estCirculo(p):
    '''est : circulo est '''

def p_estCuadro(p):
    '''est : cuadro est '''

def p_estTriangulo(p):
    '''est : triangulo est '''

def p_estLinea(p):
    '''est : linea est'''

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
    '''llamadaAFunct : ID cuadERA LEFTPAR llamadaAFunct2 gosubCuad  generaCuadFunct RIGHTPAR'''
    

def p_cuadERA(p):
    '''cuadERA : '''
    global nombreModuloCuad
    
    nombreModuloCuad = p[-1]
    generaCuadERA(nombreModuloCuad)

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
    

def p_llamadaAFunct3(p):
    '''llamadaAFunct3 : COMMA llamadaAFunct2'''
    

def p_llamadaAFunct3Empty(p):
  '''llamadaAFunct3 : empty'''

def p_llamadaAFunct2Empty(p):
    '''llamadaAFunct2 : empty'''
    
def p_declareLocal(p):
    '''declareLocal : DECLARE declareRecursivoLocal '''
     

def p_declareRecursivoLocal(p):
    '''declareRecursivoLocal : type ID  altaVarLocal assignmentDecl declare2Local declare3Local SEMICOLON declareRecursivoLocal'''
    

def p_assignmentDeclare(p):
    '''assignmentDecl : ASSGN meteAssign exp generaCuad'''
    

def p_meteAssign(p):
    '''meteAssign : '''
    meteAssign(p[-1], p[-3])

def p_number(p):
    '''number : INTEGER meteNum'''
    

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
    


def p_assignmentFUNCT(p):
    '''assignment : ID ASSGN meteVar llamadaAFunct SEMICOLON'''

def p_assignment(p):
    '''assignment : ID ASSGN meteVar exp generaCuad SEMICOLON'''

def p_debug(p):
    '''debug : '''
    print "debug"  
  
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
    #Busca en parametros
    except:
        try:
            temp_dir = dirProc[nombreModulo]['Par'][var]['Dir']
            temp_tipoVar = dirProc[nombreModulo]['Par'][var]['Dir']
   
        #Buscar variable en globales
        except KeyError as key:
            try:
                temp_dir = dirProc[nombrePrograma]['Vars'][var]['Dir']
                temp_tipoVar = dirProc[nombrePrograma]['Vars'][var]['TipoVar']
            except KeyError as key:
                print "Variable no %s esta declarada" %key
                sys.exit()
    
    quadAssign(eq, var, temp_tipoVar)

def p_assignmentEmpty(p):
    '''assignment : empty'''

def p_conditional(p):
    '''conditional : IF LEFTPAR exp generaCuad RIGHTPAR gotoFCuad LEFTKEY debug est RIGHTKEY  conditionalElse '''
    


def p_gotoFCuad(p):
    '''gotoFCuad : '''
    gotoF()

def p_goToCuad(p):
    '''gotoCuad : '''
    gotoCuad()

def p_conditionalElse(p):
    '''conditionalElse : gotoCuad ELSE LEFTKEY est RIGHTKEY llenaGoto '''
    

def p_llenaGoto(p):
    '''llenaGoto : '''
    llenaGoto()

def p_conditionalElseEmpty(p):
    '''conditionalElse : llenaCuadF empty'''
    
def p_conditional2(p):
    '''conditional2 : exp conditional2'''
    
def p_conditional2Empty(p):
    '''conditional2 : empty'''
   
def p_cycles(p):
    '''cycles : while'''
    
def p_cyclesEmpty(p):
    '''cycles : empty'''
    
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
    '''while :  WHILE LEFTPAR while2 RIGHTPAR  gotoFCuad LEFTKEY est RIGHTKEY llenaCuadFWhile  '''
    


def p_llenaCuadF(p):
    '''llenaCuadF : '''
    llenaCuadF()

def p_llenaCuadFWhile(p):
    '''llenaCuadFWhile : '''
    llenaCuadFWhile()

def p_while2(p):
    '''while2 : exp '''
    
def p_while2Empty(p):
    '''while2 : empty'''

def p_expBool(p):
    '''exp : BOOL meteBool exp2'''

def p_meteBool(p):
    '''meteBool : '''
    meteBool(p[-1])

def p_exp(p):
    '''exp : ID meteExp exp2'''
    

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
    #Buscar variable en pars
    except: 
        try: 
            temp_dir = dirProc[nombreModulo]['Par'][var]['Dir']
            temp_tipoVar = dirProc[nombreModulo]['Par'][var]['TipoVar']
        #Buscar variable en globales
        except KeyError as key:
            try:
                temp_dir = dirProc[nombrePrograma]['Vars'][var]['Dir']
                temp_tipoVar = dirProc[nombrePrograma]['Vars'][var]['TipoVar']
            except KeyError as key:
                print "Variable no %s esta declarada" % key
                sys.exit()
    
    quadExp(var, temp_tipoVar)

def p_generaCuad(p):
    '''generaCuad : '''
    generaCuadruplo()

def p_expNUMERO(p):
    '''exp : number exp2'''
    
def p_expArreglo(p):
    '''exp : arreglo exp2'''



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
    num = "%" + str(num)
   
    quadExp(num,"int" )

def p_expVACIA(p):
    '''exp : empty'''

def p_exp2(p):
    '''exp2 : LESS meteOper exp'''
    

def p_expr2Grtr(p):
    '''exp2 : GRTR meteOper exp'''

def p_expr2GrtrEq(p):
    '''exp2 : GRTREQ meteOper exp'''
    
def p_expr2LessEq(p):
    '''exp2 : LESSEQ meteOper exp'''
def p_exp2Equal(p):
    '''exp2 : EQ meteOper exp'''
    

def p_exp2NotEq(p):
    '''exp2 : NOTEQ meteOper exp'''
    

def p_exp2And(p):
    '''exp2 : AND meteOper exp'''
   

def p_exp2OR(p):
    '''exp2 : OR meteOper exp'''
    


def p_exp2SUM(p):
    '''exp2 : SUM meteOper exp'''
   


def p_meteOper(p):
    '''meteOper : '''
    quadOper(p[-1])

def p_exp2MINUS(p):
    '''exp2 : MINUS meteOper exp'''
    

def p_exp2MULTP(p):
    '''exp2 : MULTP meteOper exp'''
    

def p_exp2DIVIDE(p):
    '''exp2 : DIVIDE meteOper exp'''
    

def p_exp2Empty(p):
    '''exp2 : empty'''
    

   
def p_output(p): 
    '''output : WRITE LEFTPAR output2  RIGHTPAR SEMICOLON'''
    

def p_generaWriteCuad(p):
    '''generaWriteCuad : '''
    generaWriteCuad()


def p_meteID(p):
    '''meteID : '''
    meteID(p[-1])

def p_output2(p):
    '''output2 : ID meteID generaWriteCuad output2'''
    

def p_output2Quotes(p):
    '''output2 : QUOTE ID QUOTE output2'''

def p_output2Empty(p):
    '''output2 : empty'''
    
    
def p_input(p):
    '''input : READ LEFTPAR ID meteID generaReadCuad RIGHTPAR SEMICOLON'''
     

def p_generaReadCuad(p):
    '''generaReadCuad : '''
    generaReadCuad()

def p_empty(p):
    '''empty :'''
    
    pass

def p_circle(p):
    '''circulo : CIRCLE cuadERA LEFTPAR ID COMMA ID COMMA ID COMMA ID COMMA ID COMMA ID generaCirculoCuad RIGHTPAR SEMICOLON '''

def p_circleEmpty(p):
    '''circulo : empty'''

def p_generaCirculoCuad(p):
    '''generaCirculoCuad : '''
    generaCirculoCuad(p[-11], p[-9], p[-7], p[-5], p[-3], p[-1])

def p_square(p):
    '''cuadro : SQUARE cuadERA LEFTPAR ID COMMA ID COMMA ID COMMA ID COMMA ID COMMA ID generaCuadradoCuad RIGHTPAR SEMICOLON'''

def p_squareEmpty(p):
    '''cuadro : empty'''

def p_generaCuadradoCuad(p):
    '''generaCuadradoCuad : '''
    generaCuadradoCuad(p[-11], p[-9], p[-7], p[-5], p[-3], p[-1])

def p_triangle(p):
    '''triangulo : TRIANGLE cuadERA LEFTPAR ID COMMA ID COMMA ID COMMA ID COMMA ID COMMA ID COMMA ID COMMA ID generaTrianguloCuad RIGHTPAR SEMICOLON'''

def p_triangleEmpty(p):
    '''triangulo : empty'''

def p_generaTrianguloCuad(p):
    '''generaTrianguloCuad : '''
    generaTrianguloCuad(p[-15], p[-13], p[-11], p[-9], p[-7], p[-5], p[-3], p[-1])

def p_line(p):
    '''linea : LINE cuadERA LEFTPAR ID COMMA ID COMMA ID COMMA ID COMMA ID COMMA ID generaCuadLinea RIGHTPAR SEMICOLON'''

def p_lineEmpty(p):
    '''linea : empty'''

def p_generaCuadLinea(p):
    '''generaCuadLinea : '''
    generaCuadLinea(p[-11], p[-9], p[-7], p[-5], p[-3], p[-1])

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
directorio = '/Users/ricardolicea/OneDrive/Tecnológico de Monterrey/8vo Semestre/EM18 Diseño de Compiladores/Miri/Analysis/test/'
#directorio de la compu del trabajo
#directorio = '/Users/rlicea/Desktop/Miri copy/Analysis/test/'
#directorio de miguel
#directorio = '/Users/miguelbazan/Documents/ITC 2014/Semestres/8 Octavo Semestre/Compiladores/Final/Miri/Analysis/test/'
#directorio = '/Users/miguelbazan/Downloads/Miri copy/Analysis/test/'
#directorio = '/Users/ricardolicea/Desktop/Analysis/test/'
archivo  = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test,"r","utf-8")
cadena  = fp.read()
fp.close()

yacc.yacc()
result = yacc.parse(cadena)


#print dirProc
#MaquinaVirtual(dirProc)
#print result
#print cuadruplos
correMaquina(cuadruplos, dirProc, nombrePrograma)
# print pilaOperandos.getElements()
# print pOperadores.getElements()
# print cuadruplos
# print "-----------------"
#print VecIntTemp[0]
# print VecFloatTemp[0]
#print VecStringGlobal[0]
# print VecIntLocal[0]
# print dirProc['iSuma']['Vars']['iRes']['Dir']

