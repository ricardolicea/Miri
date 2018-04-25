#from parser import *
from structs import *
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
    if(p == '+' or p == r'\-' or p == r'\*' or p == r'/' or p == r'\='):
        return True
    else:
        return False

def goToMainQuad():
    global pSaltos
    generaCuad = Cuadruplo("GOTO", "", "", "")
    pushCuad(generaCuad)
    pSaltos.push(0)
    

def quadAssign(p1, p2):
    global pilaOperandos
    global pTipos
    global pOperadores

    if(checkOper(p1)):
        pOperadores.push(p1)
    else:
        pilaOperandos.push(p1)
    
    if(checkOper(p2)):
       pilaOperandos.push(p2)
    else:
        pOperadores.push(p2)
    

def quadExp(p1):
    global pilaOperandos
    global pTipos
    global pOperadores

    if(checkOper(p1)):
        pOperadores.push(p1)
    else:
        pilaOperandos.push(p1)

    


def quadOper(p1):
    global pilaOperandos
    global pTipos
    global pOperadores

    if(checkOper(p1)):
        pOperadores.push(p1)
    else:
        pilaOperandos.push(p1)


def generaCuadruplo():
    global pilaOperandos
    global pTipos
    global pOperadores
    global cuadruplos

    if(not(pOperadores.size()==0 or pilaOperandos.size() == 0)):
        operador = pOperadores.pop()
        operDer = pilaOperandos.pop()
        operIzq = pilaOperandos.pop()
        # print "Operador"
        # print operador
        # print "izq"
        # print operIzq
        # print "der"
        # print operDer

        generaCuad = Cuadruplo(operador, operDer, operIzq, "")
        pushCuad(generaCuad)
