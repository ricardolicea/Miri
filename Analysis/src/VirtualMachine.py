
# coding=utf-8
############################################################
#Nombre del archivo: VirtualMachine.py
#Autores: 
# Ricardo Licea Mata A01280892
# Miguel Bazan Aviña A01281010
#
#Función del archivo:
#
# La funcion principal de la maquina virtual es manejar los cuadruplos como 
# entreada y de aqui partir a generar las operaciones que se necesiten para ejectuar 
# todo el codigo intermedio. Se lee de memoria y se asigna a memoria.
#
# Dependiendo de los parametros que se reciben son las acciones 
# que se toman para cada uno de los cuadruplos.
#############################################################




# coding=utf-8
from cuadruplos import *
from TurtleGraf import *
from MemoriaV import *
import sys


cuadActual = 0
cGoSubActual = 0
ERANombre = 0
cuadERA = 0
vectReturn = []
d = 0
varGlobalRet = 0
nombre = 0
# parametros = param(None,None)

def MaquinaVirtual(dirProc):
    print "bl"
    operacionAritemtica()

def operacionAritemtica():
    sc = 0
    sc2 = 0
    global cuadActual
    global cGoSubActual
    global cuadERA
    global ERANombre
    global vectReturn
    global d
    global varGlobalRet
    global nombre
    cuadMain = cuadruplos[0].res
    
    for c in cuadruplos:
        if c.op == '+':
            newres = int(RemPar(c.res))
            for x in Vec:
                if sc == 0:
                    if x.var == c.opdoIzq:
                        sc = getScope(x.direccion)
                        dIzq = x.direccion
                if sc2 == 0:
                    if x.var == c.opdoDer:
                        sc2 = getScope(x.direccion)
                        dDcho = x.direccion
                        break
            if sc == 'local':
                vIzq = fixType(dIzq,getValueLocal(dIzq))
            else:
                vIzq = fixType(dIzq,getValueGlobal(dIzq))
            if sc2 == 'global':
                vDcho = fixType(dDcho,getValueGlobal(dDcho))
            else:
                vDcho = fixType(dDcho,getValueLocal(dDcho))
            resultado = vIzq + vDcho
            setValueTemporal(newres,resultado)
            sc = 0
            sc2 = 0
            newres = None
        elif c.op == '-':
            newres = int(RemPar(c.res))            
            for x in Vec:
                if sc == 0:
                    if x.var == c.opdoIzq:
                        sc = getScope(x.direccion)
                        dIzq = x.direccion
                if sc2 == 0:
                    if x.var == c.opdoDer:
                        sc2 = getScope(x.direccion)
                        dDcho = x.direccion
                        break
            if sc == 'local':
                vIzq = fixType(dIzq,getValueLocal(dIzq))
            else:
                vIzq = fixType(dIzq,getValueGlobal(dIzq))
            if sc2 == 'global':
                vDcho = fixType(dDcho,getValueGlobal(dDcho))
            else:
                vDcho = fixType(dDcho,getValueLocal(dDcho))
            resultado = vIzq - vDcho
            setValueTemporal(newres,resultado)
            sc = 0
            sc2 = 0
            newres = None
        elif c.op == '*':
            newres = int(RemPar(c.res))            
            for x in Vec:
                if sc == 0:
                    if x.var == c.opdoIzq:
                        sc = getScope(x.direccion)
                        dIzq = x.direccion
                if sc2 == 0:
                    if x.var == c.opdoDer:
                        sc2 = getScope(x.direccion)
                        dDcho = x.direccion
                        break
            if sc == 'local':
                vIzq = fixType(dIzq,getValueLocal(dIzq))                
            else:
                vIzq = fixType(dIzq,getValueGlobal(dIzq))                
            if sc2 == 'global':
                vDcho = fixType(dDcho,getValueGlobal(dDcho))                
            else:
                vDcho = fixType(dDcho,getValueLocal(dDcho))                
            resultado = vIzq * vDcho
            setValueTemporal(newres,resultado)
            sc = 0
            sc2 = 0
            newres = None
        elif c.op == '/':
            newres = int(RemPar(c.res))            
            for x in Vec:
                if sc == 0:
                    if x.var == c.opdoIzq:
                        sc = getScope(x.direccion)
                        dIzq = x.direccion
                if sc2 == 0:
                    if x.var == c.opdoDer:
                        sc2 = getScope(x.direccion)
                        dDcho = x.direccion
                        break
            if sc == 'local':
                vIzq = fixType(dIzq,getValueLocal(dIzq))
            else:
                vIzq = fixType(dIzq,getValueGlobal(dIzq))
            if sc2 == 'global':
                vDcho = fixType(dDcho,getValueGlobal(dDcho))
            else:
                vDcho = fixType(dDcho,getValueLocal(dDcho))
            resultado = vIzq / vDcho
            setValueTemporal(newres,resultado)
            sc = 0
            sc2 = 0
            newres = None
        elif c.op == '=':
            if '(' in c.opdoIzq:
                newIzq = int(RemPar(c.opdoIzq))
                v = getValueTemp(newIzq)
                for x in Vec:
                    if x.var == c.res:
                        sc = getScope(x.direccion)
                        d = x.direccion
                        break
                if sc == 'local':
                    setValueLocal(d,v)
                elif sc == 'global':
                    setValueGlobal(d,v)
            elif '(' not in c.opdoIzq:
                for x in Vec:
                    if sc == 0:
                        if  x.var == c.res:
                            sc = getScope(x.direccion)
                            d = x.direccion
                            break
                if sc == 'local':
                    setValueLocal(d,c.opdoIzq)
                elif sc == 'global':
                    setValueGlobal(d,c.opdoIzq)
            elif isinstance(c.opdoIzq,basestring) and c.opdoDer == None and c.res == None: ## es porque es un return
                val = getValueGlobal(varGlobalRet)
                if c.opdoIzq == nombre:
                    sc = dirProc[nombre]['Vars'][c.res]['Scope']
                    dire = dirProc[nombre]['Vars'][c.res]['Dir']
                    if sc == 'global':
                        setValueGlobal(dire,val)
                    elif sc == 'local':
                        setValueLocal(dire,val)
            sc = 0
        elif c.op == 'GOTO':
            if cuadruplos[0].op == 'GOTO':
                cuadActual = c.res
            else:
                cuadActual = c.res - 1
        elif c.op == 'RET':
            nombre = vectReturn.pop()
            d = dirProc[nombre]['Vars'][c.opdoIzq]['Dir']
            sc = getScope(d)
            varGlobalRet = set_dir_global(dirProc[nombre]['Vars'][c.opdoIzq]['TipoVar'],1)
            setValueGlobal(varGlobalRet,getValueLocal(d))
        elif c.op == 'GOSUB':
            cGoSubActual = cuadActual
            cuadActual = c.res
        elif c.op == 'ENDPROC':
            cuadActual = cGoSubActual + 1 
            if cuadActual > len(cuadruplos):
                break
        elif c.op == 'PARAM':
            for x in Vec:
                if sc == 0:
                    if x.var == c.opdoIzq:
                        sc = getScope(x.direccion)
                        dIzq = x.direccion
            if sc == 'local':
                vIzq = fixType(dIzq,getValueLocal(dIzq))
            else:
                vIzq = fixType(dIzq,getValueGlobal(dIzq))
            setValueTemporal(dIzq,vIzq)
        elif c.op == 'ERA':
            vectReturn.append(c.opdoIzq)
            cuadERA = cuadActual
        elif c.op == 'GOTO':
        cuadActual += 1

# class param():
#     def __init__(valor,tipo):
#         self.valor = valor
#         self.tipo = tipo            

def RemPar(valor):
    new = valor.replace("(","")
    return new

