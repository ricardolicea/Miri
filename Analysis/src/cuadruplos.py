#from parser import *
from structs import *
import sys

pilaO = Stack()
pOper = Stack()
pTipos = Stack()
pSaltos = Stack()
pEjecucion = Stack()
pDimensionada = Stack()

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
    
    

def goToMainQuad():
    global pSaltos
    generaCuad = Cuadruplo("GOTO", "", "", "")
    print generaCuad.op
    print generaCuad.opdoIzq
    print generaCuad.opdoDer
    print generaCuad.res
    pushCuad(generaCuad)
    pSaltos.push(0)
    