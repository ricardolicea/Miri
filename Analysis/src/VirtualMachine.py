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
dIzq = 0
dDcho = 0



def MaquinaVirtual(dirProc):
    print "bl"
    operacionAritemtica()

def operacionAritemtica():
    sc = 0
    sc2 = 0
    global dIzq
    global cuadActual
    global cGoSubActual
    global cuadERA
    global ERANombre
    global vectReturn
    global d
    global varGlobalRet
    global nombre
    global dDcho
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
            dDcho = 0
            dIzq = 0
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
            setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
            dDcho = 0
            dIzq = 0
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
            dDcho = 0
            dIzq = 0
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
                vDcho = fixType(dDcho,getValueGlobal(dDcho))
            else:
                vDcho = fixType(dDcho,getValueLocal(dDcho))
            resultado = vIzq / vDcho
            setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
            dDcho = 0
            dIzq = 0
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
            dIzq = 0
        elif c.op == 'ERA':
            vectReturn.append(c.opdoIzq)
            cuadERA = cuadActual
        elif c.op == '>':
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
            if vIzq > vDcho:
                resultado = True
                setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
            dDcho = 0
            dIzq = 0
        elif c.op == '<':
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
            if vIzq < vDcho:
                resultado = True
                setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
            dDcho = 0
            dIzq = 0
        elif c.op == '==':
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
            if vIzq == vDcho:
                resultado = True
                setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
            dDcho = 0
            dIzq = 0
        elif c.op == '!=':
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
            if vIzq != vDcho:
                resultado = True
                setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
            dDcho = 0
            dIzq = 0
        elif c.op == '>=':
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
            if vIzq >= vDcho:
                resultado = True
                setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
            dDcho = 0
            dIzq = 0
        elif c.op == '<=':
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
            if vIzq <= vDcho:
                resultado = True
                setValueTemporal(c.res,resultado)
            sc = 0
            sc2 = 0
            dDcho = 0
            dIzq = 0
        elif c.op == 'GOTOF':
            tipo = 0
            for x in Vec:
                if sc == 0:
                    if x.var == c.opdoIzq:
                        sc = getScope(x.direccion)
                        dIzq = x.direccion
                        break
            if sc == 'local':
                vIzq = fixType(dIzq,getValueLocal(dIzq))
                tipo = getTypeLocal(dIzq)
            else:
                vIzq = fixType(dIzq,getValueGlobal(dIzq))
                tipo = getTypeGlobal(dIzq)
            if not vIzq:
                cuadActual = c.res - 1
        elif c.op == 'WRITE':
            tipo = 0
            for x in Vec:
                if sc == 0:
                    if x.var == c.opdoIzq:
                        sc = getScope(x.direccion)
                        dIzq = x.direccion
                        break
            if sc == 'local':
                vIzq = fixType(dIzq,getValueLocal(dIzq))
                tipo = getTypeLocal(dIzq)
            else:
                vIzq = fixType(dIzq,getValueGlobal(dIzq))
                tipo = getTypeGlobal(dIzq)
            print(vIzq)


        cuadActual += 1    
            

def RemPar(valor):
    new = valor.replace("(","")
    return new

