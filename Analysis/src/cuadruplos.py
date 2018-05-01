#from parser import *
from structs import *
from cuboSemantico import *
from MemoriaV import *
import sys

pilaOperandos = Stack()
pOperadores = Stack()
pTipos = Stack()
pSaltos = Stack()
pEjecucion = Stack()
pDimensionada = Stack()
vPolaco = Queue()
cuadruplos = []
contSaltos = 0
posPar = 0
tempSaltos = 0

class Cuadruplo:
    def __init__(self, operador, operandoIzq, operandoDer, temp):
		self.op = operador
		self.opdoIzq = operandoIzq
		self.opdoDer = operandoDer
		self.res = temp
	
def pushCuad(cuadruplo):
    global cuadruplos
    global contSaltos

    cuadruplos.append(cuadruplo)
    contSaltos += 1
   
    
    
def checkOper(p):
    if( p == '+' or p == r'(' or p == r')' or p == r'-' or p == r'*' or p == r'/' or p == r'='
        or p == r'>' or p == r'<' or p == r'>=' or p == r'<=' or p == r'==' or p == r'!='
        or p == 'and' or p == 'or'):
        return True
    else:
        return False

def goToMainQuad():
    global pSaltos
    generaCuad = Cuadruplo("GOTO", "", "", "")
    pushCuad(generaCuad)
    pSaltos.push(0)
    

def quadAssign(p1, p2, tipo):
    global pilaOperandos
    global pTipos
    global pOperadores

    if(checkOper(p1)):
        pOperadores.push(p1)
    else:
        pilaOperandos.push(p1)
        pTipos.push(tipo)
    
    if(checkOper(p2)):
       pOperadores.push(p2)
    else:
        pilaOperandos.push(p2)
        pTipos.push(tipo)
    

def quadExp(p1, tipo):
    global pilaOperandos
    global pTipos
    global pOperadores


    if(checkOper(p1)):
        pOperadores.push(p1)
    else:
        pilaOperandos.push(p1)
        pTipos.push(tipo)

    if not(pOperadores.isEmpty()):
        if not(pOperadores.peek() == r'(' or p1 == r')'):
            if(pOperadores.peek() == r'/' or pOperadores.peek() == r'*'):
                generaCuadruplo()
            elif(pOperadores.peek() == r'+' or pOperadores.peek() == r'-'):
                generaCuadruplo()
            elif(pOperadores.peek() == r'<' or pOperadores.peek() == r'>' or
                pOperadores.peek() == r'<=' or pOperadores.peek() == r'>='
                or pOperadores.peek() == r'==' or pOperadores.peek() == r'!='):
                generaCuadruplo()
            elif(pOperadores.peek() == 'and' or pOperadores.peek() == 'or'):
                generaCuadruplo()
    
    #

def metePar(p1):
    pOperadores.push(p1)

def quadOper(p1):
    global pilaOperandos
    global pTipos
    global pOperadores


    if not (pOperadores.isEmpty()):
        if not(pOperadores.peek() == r'(' or p1 == r')'):
            if(pOperadores.peek() == r'>' or pOperadores.peek() == r'<' or pOperadores.peek() == r'>=' or pOperadores.peek() == r'<=' or pOperadores.peek() == r'==' or pOperadores.peek() == r'!='):
                generaCuadruplo()
            elif(pOperadores.peek() == "and" or pOperadores.peek() == "or"):
                generaCuadruplo()
            elif (pOperadores.peek() == r'+' or pOperadores.peek() == r'-'):
                generaCuadruplo() 
            elif (pOperadores.peek() == r'/' or pOperadores.peek() == r'*'):
                generaCuadruplo()
    
    pOperadores.push(p1)
    # if(checkOper(p1)):
    #     pOperadores.push(p1)
    # else:
    #     pilaOperandos.push(p1)
    
    # if (pOperadores.peek() == r'+' or pOperadores.peek() == r'-'):
    #     generaCuadruplo()
    

def sacaPar():
    pOperadores.pop()

def gotoF():
    global contSaltos
    global pSaltos
    global pilaOperandos
    global cuadruplos
    
    dirExp = pilaOperandos.pop()
    pSaltos.push(contSaltos)
    generaCuad = Cuadruplo("GOTOF",dirExp, None, None)
    pushCuad(generaCuad)
    
    
def endproc():
    generaCuad = Cuadruplo("ENDPROC",None, None, None)
    pushCuad(generaCuad)
    
def gotoCuad():
    global contSaltos
    global pSaltos
    global pilaOperandos
    global cuadruplos
    global tempSaltos

    tempSaltos = pSaltos.pop()
    generaCuad = Cuadruplo("GOTO",None, None, None)
    pSaltos.push(contSaltos)
    pushCuad(generaCuad)

    cuad = cuadruplos[tempSaltos]
    cuad.temp = contSaltos
    cuadruplos[tempSaltos] = cuad

def cuadERA(p1):
    generaCuad = Cuadruplo('ERA', None, None, p1)
    pushCuad(generaCuad)

def llenaGoto():
    global contSaltos
    global pSaltos
    global pilaOperandos
    global cuadruplos
    global tempSaltos

    tempSaltos = pSaltos.pop()
    cuad = cuadruplos[tempSaltos]
    cuad.temp = contSaltos
    cuadruplos[tempSaltos] = cuad

def meteSalto():
    pSaltos.push(contSaltos)

def llenaCuadF():
    tempDir = pSaltos.pop()
    cuad = cuadruplos[tempDir]
    cuad.temp = contSaltos
    cuadruplos[tempDir] = cuad

def cuadFor(p1, p2):
    global pOperadores
    global pilaOperandos
    global cuadruplos
    if p1 == r'=':
        pOperadores.push(p1)
        pilaOperandos.push(p2)
    else:
        pOperadores.push(p2)
        pilaOperandos.push(p2)

def gotoVCuad():
    global contSaltos
    global pSaltos
    global pilaOperandos
    global cuadruplos
   
    tempDir = pSaltos.pop()
    generaCuad = Cuadruplo("GOTOV", pilaOperandos.pop(), None, tempDir)
    pushCuad(generaCuad)

def llenaMain():
    global contSaltos
    global pSaltos
    global pilaOperandos
    global cuadruplos
    global tempSaltos

    cuad = cuadruplos[0]
    cuad.res = contSaltos
    cuadruplos[0] = cuad

def meteID(p1):
    global pilaOperandos
    pilaOperandos.push(p1)

def quadParam():
    global pilaOperandos
    generaCuad = Cuadruplo("PARAM", pilaOperandos.pop(), None, "PAR1")
    pushCuad(generaCuad)

def generaRet(p):
    generaCuad = Cuadruplo("RETURN", p, None, None)
    pushCuad(generaCuad)
def guardaSalto():
    pSaltos.push(contSaltos)
def gosubCuad(p):
    global pOperadores
    global pilaOperandos

    generaCuad = Cuadruplo("GOSUB", None, None, pSaltos.pop())
    pushCuad(generaCuad)
    generaCuad = Cuadruplo(pOperadores.pop(),p, None, pilaOperandos.pop())
    pushCuad(generaCuad)
    print cuadruplos

def generaCuadruplo():
    global pilaOperandos
    global pTipos
    global pOperadores
    global cuadruplos

    
    if(not(pOperadores.isEmpty() or pilaOperandos.isEmpty())):
        operador = pOperadores.pop()
        operDer = pilaOperandos.pop()
        operIzq = pilaOperandos.pop()
        if not(operador == r'='):
            tipoIzq = pTipos.pop()
            tipoDer = pTipos.pop()
            tipoAnsw = cuboSemantico[tipoIzq][tipoDer][operador]
        
            if(tipoAnsw != "Error"):
                temp = set_dir_temp(tipoAnsw)
                generaCuad = Cuadruplo(operador, operIzq, operDer, temp)
                pushCuad(generaCuad)
                pilaOperandos.push(temp)
                pTipos.push(tipoAnsw)
                # if pOperadores.peek() == r'(':
                #     pOperadores.pop()
                print "------------------------------"
                print "(" + str(operador) + "," + str(operIzq) + "," + str(operDer) + "," + str(temp) +")" 
                print "------------------------------"
            else:
                sys.exit("No se puede realizar la operacion")
        else:
            generaCuad = Cuadruplo(operador, operDer, None, operIzq)
            pushCuad(generaCuad)
            print "------------------------------"
            print "(" + str(operador) + "," + str(operDer) + ", Null" +  "," + str(operIzq) +")" 
            print "------------------------------"
        
