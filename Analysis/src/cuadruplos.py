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
    print contSaltos
   
    
    
def checkOper(p):
    if( p == '+' or p == r'(' or p == r')' or p == r'-' or p == r'*' or p == r'/' or p == r'='
        or p == r'>' or p == r'<' or p == r'>=' or p == r'<=' or p == r'==' or p == r'!='
        or p == 'and' or p == 'or'):
        return True
    else:
        return False

def goToMainQuad():
    generaCuad = Cuadruplo("GOTO", "", "", "")
    pushCuad(generaCuad)
    
    

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
    
def meteAssign(p1,p2):
    global pOperadores
    global pilaOperandos

    pOperadores.push(p1)
    pilaOperandos.push(p2)
    
    print p1
    print p2

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
            
    
    #
def generaCuadFunct(p):
    global pOperadores
    global pilaOperandos
    global cuadruplos
    cuad = cuadruplos.pop()
    cuad.opdoIzq = p
    pushCuad(cuad)

def metePar(p1):
    pOperadores.push(p1)

def quadOper(p1):
    global pilaOperandos
    global pTipos
    global pOperadores


    # if not (pOperadores.isEmpty()):
    #     if not(pOperadores.peek() == r'(' or p1 == r')'):
    #         if(pOperadores.peek() == r'>' or pOperadores.peek() == r'<' or pOperadores.peek() == r'>=' or pOperadores.peek() == r'<=' or pOperadores.peek() == r'==' or pOperadores.peek() == r'!='):
    #             generaCuadruplo()
    #         elif(pOperadores.peek() == "and" or pOperadores.peek() == "or"):
    #             generaCuadruplo()
    #         elif (pOperadores.peek() == r'+' or pOperadores.peek() == r'-'):
    #             generaCuadruplo() 
    #         elif (pOperadores.peek() == r'/' or pOperadores.peek() == r'*'):
    #             generaCuadruplo()
    
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
    global cuadruplos
    
    print cuadruplos
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

    
    generaCuad = Cuadruplo("GOTO",None, None, None)
    pushCuad(generaCuad)
    cuad = pSaltos.pop()
    cuadruplos[cuad].res = contSaltos-1
    pSaltos.push(contSaltos)
    

   

def generaCuadERA(p1):
    generaCuad = Cuadruplo('ERA', None, None, p1)
    pushCuad(generaCuad)

def generaWriteCuad():
    global pilaOperandos
    global cuadruplos
    generaCuad = Cuadruplo("WRITE", None, None, pilaOperandos.pop())
    pushCuad(generaCuad)
   

def generaReadCuad():
    global pilaOperandos
    global cuadruplos
    generaCuad = Cuadruplo("READ", None, None, pilaOperandos.pop())
    pushCuad(generaCuad)
    
def generaCirculoCuad(num, caract, boleana, num2, num3):
    generaCuad = Cuadruplo("PARAM", num, None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", caract, None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", boleana, None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", num2,  None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", num3,  None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("CIRCULO", None, None, None)
    pushCuad(generaCuad)

def generaCuadradoCuad(num, caract, boleana, num2, num3):
    generaCuad = Cuadruplo("PARAM", num, None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", caract, None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", boleana, None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", num2,  None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", num3,  None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("CUADRADO", None, None, None)
    pushCuad(generaCuad)

def generaCuadLinea(num1, caract, num2, num3, num4, num5):
    generaCuad = Cuadruplo("PARAM", num1, None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", caract, None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", num2, None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", num3,  None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", num4,  None, None)
    pushCuad(generaCuad)
    generaCuad = Cuadruplo("PARAM", num5,  None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("LINEA", None,  None, None)
    pushCuad(generaCuad)



def generaTrianguloCuad(num, num2, num3, caract, boleana, num4, num5, num6):
    generaCuad = Cuadruplo("PARAM", num, None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("PARAM", num2, None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("PARAM", num3, None, None)
    pushCuad(generaCuad)
    
    generaCuad = Cuadruplo("PARAM", caract, None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("PARAM", boleana, None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("PARAM", num4,  None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("PARAM", num5,  None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("PARAM", num6,  None, None)
    pushCuad(generaCuad)

    generaCuad = Cuadruplo("TRIANGULO", None, None, None)
    pushCuad(generaCuad)


def cuadVer(p1, lSup, dire, m, dim2):
    global pilaOperandos
    global cuadruplos
    s = pilaOperandos.pop()
    generaCuad = Cuadruplo("VER", s,0, lSup)
    pushCuad(generaCuad)
    #AQUI CAMBIAR EL FORMATO DE DIRECCIONES
    if dim2 == None:
        temp = set_dir_temp('int')
        pilaOperandos.push(temp)
        generaCuad = Cuadruplo('+', s, dire, temp)
        pushCuad(generaCuad)
        
    elif dim2 == 1:
        temp = set_dir_temp('int')
        
        generaCuad = Cuadruplo("+", pilaOperandos.pop(), m, temp)
        pilaOperandos.push(temp)
        pushCuad(generaCuad)
        temp = set_dir_temp('int')
        generaCuad = Cuadruplo("+", pilaOperandos.pop(), dire, temp)
        pushCuad(generaCuad)
        pilaOperandos.push(temp)

    else:
        temp = set_dir_temp('int')
        pilaOperandos.push(temp)
        generaCuad = Cuadruplo("*", s, m, temp)
        pushCuad(generaCuad)
    print cuadruplos

def llenaGoto():
    global contSaltos
    global pSaltos
    global pilaOperandos
    global cuadruplos
    global tempSaltos

    tempSaltos = pSaltos.pop()
    cuad = cuadruplos[tempSaltos-2]
    cuad.res = contSaltos - 2
    cuadruplos[tempSaltos] = cuad

def meteSalto():
    pSaltos.push(contSaltos)

def llenaCuadF():
    tempDir = pSaltos.pop()
    cuad = cuadruplos[tempDir]
    cuad.temp = contSaltos
    cuadruplos[tempDir] = cuad

# def cuadFor(p1, p2):
#     global pOperadores
#     global pilaOperandos
#     global cuadruplos
#     if p1 == r'=':
#         pOperadores.push(p1)
#         pilaOperandos.push(p2)
#     else:
#         pOperadores.push(p2)
#         pilaOperandos.push(p2)

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
    global contSaltos
 #  contSaltos -= 1
    generaCuad = Cuadruplo("RETURN", p, None, None)
    pushCuad(generaCuad)

def guardaSalto():
    global contSaltos
    return contSaltos


def gosubCuad(p, salto):
    global pOperadores
    global pilaOperandos
    global ultimoSalto

    
    generaCuad = Cuadruplo("GOSUB", None, None, salto)
    
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
    
        
