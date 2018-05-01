# coding=utf-8
from cuadruplos import *
from TurtleGraf import *
from MemoriaV import *
import sys

cuadActual = 0

def MaquinaVirtual(dirProc):
    print "bl"
    operacionAritemtica()

def operacionAritemtica():
    sc = 0
    sc2 = 0
    global cuadActual
    cuadMain = cuadruplos[0].res
    
    for c in cuadruplos:
        if c.op == '+':
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
            setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
        elif c.op == '-':
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
            setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
        elif c.op == '*':
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
            setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
        elif c.op == '/':
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
                vDcho = fixType(dDcho,getValueGlobal(dDch))
            else:
                vDcho = fixType(dDcho,getValueLocal(dDcho))
            
            resultado = vIzq / vDcho
            setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
        elif c.op == '=':
            r = checaMemoria()
            if r == 'memoria':
                v = getValueTemp(c.res)
                for x in Vec:
                    if x.var == c.res:
                        sc = getScope(x.direccion)
                        d = x.direccion
                        break
                if sc == 'local':
                    setValueLocal(d,v)
                elif sc == 'global':
                    setValueGlobal(d,v)
            elif r == 'valor':
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
            sc = 0
        cuadActual += 1

def checaMemoria():
    global cuadActual
    if cuadruplos[cuadActual-1].op == '+' or cuadruplos[cuadActual-1].op == '-' or cuadruplos[cuadActual-1].op == '*' or cuadruplos[cuadActual-1].op == 'GOTO' or cuadruplos[cuadActual-1].op == '/':
        return 'memoria'
    else:
        return 'valor'
