#from parser import *
from structs import *
from cuboSemantico import *
from tablas import *
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
   
    #
    
def checkOper(p):
    if( p == '+' or p == r'(' or p == r')' or p == r'-' or p == r'*' or p == r'/' or p == r'='):
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

    if not(pOperadores.peek() == r'\(' or p1 == r'\)'):
        if(pOperadores.peek() == r'+' or pOperadores.peek() == r'-'):
            generaCuadruplo()
        if(pOperadores.peek() == r'/' or pOperadores.peek() == r'*'):
            generaCuadruplo()
    
    #

def metePar(p1):
    global posPar
    posPar = pOperadores.size()
    pOperadores.push(p1)

def quadOper(p1):
    global pilaOperandos
    global pTipos
    global pOperadores

    if (pOperadores.peek() == r'/' or pOperadores.peek() == r'*'):
        generaCuadruplo() 
        if (pOperadores.peek() == r'+' or pOperadores.peek() == r'-'):
            generaCuadruplo()
    
    if(checkOper(p1)):
        pOperadores.push(p1)
    else:
        pilaOperandos.push(p1)
    
    
    

def sacaPar():
    cuadruplos.pop()

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
                if pOperadores.peek() == r'(':
                    pOperadores.pop()
                print tipoAnsw
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
        
