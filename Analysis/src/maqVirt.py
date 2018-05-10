# coding=utf-8

from MemoriaV import *
import sys
from structs import *
from TurtleGraf import *

moduloActual = "main"
dirProc = "None"
nombrePrograma = ""
pFunciones = Stack()
pRegresar = Stack()
keys = None
valorDeReturn = None
iRadio = None
sColor = None
bFill = None
iX = None
iY = None
iTam = None
iW = None
iLent = None
iDeg = None
iA = None
iB = None
iC = None
vecMemoriaGlobal = []
vecMemoriaLocal = []
def quitaPar(valor):
    new = valor.replace("(","")
    return int(new)

def quitaPor(valor):
    try:
        new = valor.replace("%","")
        return int(new)
    except:
        new = valor.replace("%", "")
        return float(new)

def quitaBasura(valor):
    new = valor.replace("\r","")
    return int(new)
    
def getDireccion(var):
    global nombrePrograma
    try:
        direccion = dirProc[moduloActual]['Vars'][var]['Dir']
    except KeyError as key:
        try:
            direccion = dirProc[moduloActual]['Par'][var]['Dir']
        except KeyError as key:
            try:
                direccion = dirProc[nombrePrograma]['Vars'][var]['Dir']
            except KeyError as key:
                sys.exit()
    return direccion

def getDireccionMain(var):
    global nombrePrograma
    try:
        direccion = dirProc['main']['Vars'][var]['Dir']
    except KeyError as key:
        try:
            direccion = dirProc['main']['Par'][var]['Dir']
        except KeyError as key:
            try:
                direccion = dirProc[nombrePrograma]['Vars'][var]['Dir']
            except KeyError as key:
                sys.exit()
    return direccion
def getDireccionPar(var,modulo):
    global nombrePrograma
    try:
        direccion = dirProc[modulo]['Vars'][var]['Dir']
    except KeyError as key:
        try:
            direccion = dirProc[modulo]['Par'][var]['Dir']
        except KeyError as key:
            try:
                direccion = dirProc[nombrePrograma]['Vars'][var]['Dir']
            except KeyError as key:
                sys.exit()
    return direccion

def operacionAritmetica(cuadruplo):
    global moduloActual
    global valorDeReturn
    operador = cuadruplo.op
    opdoIzq = cuadruplo.opdoIzq
    opdoDer = cuadruplo.opdoDer
    res = cuadruplo.res
    resultadoOper = 0

    if operador == '+':
        res = quitaPar(res)
        if opdoIzq[0] == '%':
            valorIzq = quitaPor(opdoIzq)
            direccionDer = getDireccion(opdoDer)
            scopeDer = getScope(direccionDer)
            if scopeDer == 'global':
                respuesta = valorIzq + fixType(direccionDer, getValueGlobal(direccionDer))
            elif scopeDer =='local':
                respuesta = valorIzq + fixType(direccionDer, getValueLocal(direccionDer))
            elif scopeDer =='temp':
                respuesta = valorIzq + fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
        elif opdoDer[0] == '%':
            valorDer = quitaPor(opdoDer)
            direccionIzq = getDireccion(opdoIzq)
            scopeIzq = getScope(direccionIzq)
            if scopeIzq == 'global':
                respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) + valorDer
            elif scopeIzq =='local':
                respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) + valorDer
            elif scopeIzq == 'temp':
                respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) + valorDer
                
            setValueTemporal(res,respuesta)
        else:
            direccionIzq = getDireccion(opdoIzq)
            direccionDer = getDireccion(opdoDer)
            scopeIzq = getScope(direccionIzq)
            scopeDer = getScope(direccionDer)
            if scopeIzq == 'global':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) + fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer =='local':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) + fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer == 'temp':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) + fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'local' :
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) + fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) + fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) + fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'temp':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) + fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) + fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) + fixType(direccionDer, getValueTemp(direccionDer))
             
            setValueTemporal(res,respuesta)

    elif operador == '-':
        res = quitaPar(res)
        if opdoIzq[0] == '%':
            valorIzq = quitaPor(opdoIzq)
            direccionDer = getDireccion(opdoDer)
            scopeDer = getScope(direccionDer)
            if scopeDer == 'global':
                respuesta = valorIzq - fixType(direccionDer, getValueGlobal(direccionDer))
            elif scopeDer =='local':
                respuesta = valorIzq - fixType(direccionDer, getValueLocal(direccionDer))
            elif scopeDer == 'temp':
                respuesta = valorIzq - fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
        elif opdoDer[0] == '%':
            valorDer = quitaPor(opdoDer)
            direccionIzq = getDireccion(opdoIzq)
            scopeIzq = getScope(direccionIzq)
            if scopeIzq == 'global':
                respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - valorDer
            elif scopeIzq =='local':
                respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - valorDer
            elif scopeIzq == 'temp':
                respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - valorDer
            setValueTemporal(res,respuesta)
        elif opdoIzq[0] == '(':
            direccionIzq = quitaPar(opdoIzq)
            direccionDer = getDireccion(opdoDer)
            scopeIzq = getScope(direccionIzq)
            scopeDer = getScope(direccionDer)
            if scopeIzq == 'global':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer =='local':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'local':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeIzq == 'local' and scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'temp':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeIzq == 'local' and scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
        elif opdoDer[0] == '(':
            direccionDer = quitaPar(opdoDer)
            direccionIzq = getDireccion(opdoIzq)
            scopeIzq = getScope(direccionIzq)
            scopeDer = getScope(direccionDer)
            if scopeIzq == 'global':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer =='local':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'local':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeIzq == 'local' and scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'temp':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeIzq == 'local' and scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
        elif opdoIzq[0] == '(' and opdoDer[0] == '(':
            direccionIzq = quitaPar(opdoIzq)
            direccionDer = quitaPar(opdoDer)
            scopeIzq = getScope(direccionIzq)
            scopeDer = getScope(direccionDer)
            if scopeIzq == 'global':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer =='local':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'local':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeIzq == 'local' and scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'temp':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeIzq == 'local' and scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
        else:
            direccionIzq = getDireccion(opdoIzq)
            direccionDer = getDireccion(opdoDer)
            scopeIzq = getScope(direccionIzq)
            scopeDer = getScope(direccionDer)
            if scopeIzq == 'global':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer =='local':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'local':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeIzq == 'local' and scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'temp':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeIzq == 'local' and scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) - fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
            


    elif operador == '*':
        res = quitaPar(res)
        if opdoIzq[0] == '%':
            valorIzq = quitaPor(opdoIzq)
            direccionDer = getDireccion(opdoDer)
            scopeDer = getScope(direccionDer)
            if scopeDer == 'global':
                respuesta = valorIzq * fixType(direccionDer, getValueGlobal(direccionDer))
            elif scopeDer =='local':
                respuesta = valorIzq * fixType(direccionDer, getValueLocal(direccionDer))
            elif scopeDer == 'temp':
                respuesta = valorIzq * fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
        elif opdoDer[0] == '%':
            valorDer = quitaPor(opdoDer)
            direccionIzq = getDireccion(opdoIzq)
            scopeIzq = getScope(direccionIzq)
            if scopeIzq == 'global':
                respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) * valorDer
            elif scopeIzq =='local':
                respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) * valorDer
            elif scopeIzq == 'temp':
                respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) * valorDer
            setValueTemporal(res,respuesta)
        else:
            direccionIzq = getDireccion(opdoIzq)
            direccionDer = getDireccion(opdoDer)
            scopeIzq = getScope(direccionIzq)
            scopeDer = getScope(direccionDer)
            if scopeIzq == 'global': 
                if scopeDer == 'global':
                    vIzq = getValueGlobal(direccionIzq)
                    vDer = getValueGlobal(direccionDer)
                    respuesta = fixType(direccionIzq, vIzq) * fixType(direccionDer, vDer)
                elif scopeDer =='local':
                    vIzq = getValueGlobal(direccionIzq)
                    vDer = getValueLocal(direccionDer)
                    respuesta = fixType(direccionIzq, vIzq) * fixType(direccionDer, vDer)
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) * fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'local':
                if scopeDer == 'global':
                    vIzq = getValueLocal(direccionIzq)
                    vDer = getValueGlobal(direccionDer)
                    respuesta = fixType(direccionIzq, vIzq) * fixType(direccionDer, vDer)
                elif scopeDer == 'local':
                    vIzq = getValueLocal(direccionIzq)
                    vDer = getValueLocalal(direccionDer)
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) * fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeIzq == 'local' and scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) * fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'temp':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) * fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) * fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) * fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
    elif operador == '/':
        res = quitaPar(res)
        if opdoIzq[0] == '%':
            valorIzq = quitaPor(opdoIzq)
            direccionDer = getDireccion(opdoDer)
            scopeDer = getScope(direccionDer)
            if scopeDer == 'global':
                respuesta = valorIzq / fixType(direccionDer, getValueGlobal(direccionDer))
            elif scopeDer =='local':
                respuesta = valorIzq / fixType(direccionDer, getValueLocal(direccionDer))
            elif scopeDer == 'temp':
                respuesta = valorIzq / fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
        elif opdoDer[0] == '%':
            valorDer = quitaPor(opdoDer)
            direccionIzq = getDireccion(opdoIzq)
            scopeIzq = getScope(direccionIzq)
            if scopeIzq == 'global':
                respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) / valorDer
            elif scopeIzq =='local':
                respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) / valorDer
            elif scopeIzq == 'temp':
                respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) / valorDer
            setValueTemporal(res,respuesta)
        else:
            direccionIzq = getDireccion(opdoIzq)
            direccionDer = getDireccion(opdoDer)
            scopeIzq = getScope(direccionIzq)
            scopeDer = getScope(direccionDer)
            if scopeIzq == 'global':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) / fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer =='local':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) / fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) / fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'local':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) / fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) / fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) / fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'temp':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) / fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) / fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueTemp(direccionIzq)) / fixType(direccionDer, getValueTemp(direccionDer))
            setValueTemporal(res,respuesta)
    elif operador == '=':
        if valorDeReturn == None:
            direccion = getDireccion(res)
            scope = getScope(direccion)
            if(opdoIzq[0] == '('):
                direccionIzq = quitaPar(opdoIzq)
                valor = fixType(direccionIzq, getValueTemp(direccionIzq))
                if scope == 'local':
                    setValueLocal(direccion, valor)
                elif scope == 'global':
                    setValueGlobal(direccion, valor)
                elif scope == 'temp':
                    setValueTemporal(direccion, valor)   
            elif(opdoIzq[0] == '%'):
                opdoIzq = quitaPor(opdoIzq)
                valor = opdoIzq
                if scope == 'local':
                    setValueLocal(direccion, valor)
                elif scope == 'global':
                    setValueGlobal(direccion, valor)
                elif scope == 'temp':
                    setValueTemporal(direccion, valor) 
            elif(opdoIzq == 'true' or opdoIzq == 'false'):
                valor = opdoIzq
                if scope == 'local':
                    setValueLocal(direccion, valor)
                elif scope == 'global':
                    setValueGlobal(direccion, valor)
                elif scope == 'temp':
                    setValueTemporal(direccion, valor) 
            else:
                direccionIzq = getDireccion(opdoIzq)
                scope1 = getScope(direccionIzq)
                if scope1 == 'local':
                    v = getValueLocal(direccionIzq)
                    if scope == 'global':
                        setValueGlobal(direccion,v)
                    elif scope == 'local':
                        setValueLocal(direccion,v)
                    else:
                        setValueTemporal(direccion, v)
                elif scope1 == 'temp':
                    v = getValueTemp(direccionIzq)
                    if scope == 'global':
                        setValueGlobal(direccion,v)
                    elif scope == 'local':
                        setValueLocal(direccion,v)
                    else:
                        setValueTemporal(direccion, v)
                else:
                    v = getValueGlobal(direccionIzq)
                    if scope == 'global':
                        setValueGlobal(direccion,v)
                    elif scope == 'local':
                        setValueLocal(direccion,v)
                    else:
                        setValueTemporal(direccion, v)
        else:
            direccion = getDireccion(res)
            scope = getScope(direccion)
            
            if scope == 'local':
                setValueLocal(direccion, valorDeReturn)
            elif scope == 'global':
                setValueGlobal(direccion, valorDeReturn)
            elif scope == 'temp':
                setValueTemporal(direccion, valorDeReturn)
            valorDeReturn = None

            



        
def escribeAPantalla(cuad):
    direccion = getDireccion(cuad.res)
    scope = getScope(direccion)
    
    if scope == 'local':
        valor = getValueLocal(direccion)
    elif scope == 'global':
        valor = getValueGlobal(direccion)
    print valor

def leeDePantalla(cuad):
        direccion = getDireccion(cuad.res)
        scope = getScope(direccion)
        valor = raw_input()
        if scope == 'local':
            setValueLocal(direccion, valor)
        elif scope == 'global':
            setValueGlobal(direccion, valor)
        
def resuleveCondicion(cuadruplo):
    global moduloActual
    operador = cuadruplo.op
    opdoIzq = cuadruplo.opdoIzq
    opdoDer = cuadruplo.opdoDer
    if opdoIzq[0] == '%':
        opdoIzq = quitaPor(cuadruplo.opdoIzq)
        valorIzq = opdoIzq
        opdoDer = cuadruplo.opdoDer
        dirDer = getDireccion(opdoDer)
        valorDer = int(getValueLocal(dirDer))
    elif opdoDer[0] == '%':
        opdoIzq = cuadruplo.opdoIzq
        dirIzq = getDireccion(opdoIzq)
        valorIzq = int(getValueLocal(dirIzq))
        opdoDer = quitaPor(cuadruplo.opdoDer)
        
        valorDer = opdoDer
    else:
        opdoIzq = cuadruplo.opdoIzq
        dirIzq = getDireccion(opdoIzq)
        valorIzq = int(getValueLocal(dirIzq))
        opdoDer = cuadruplo.opdoDer
        dirDer = getDireccion(opdoDer)
        valorDer = int(getValueLocal(dirDer))
    
    res = quitaPar(cuadruplo.res)
    # valorIzq = quitaBasura(valorIzq)
    # valorDer = quitaBasura(valorDer)
    if operador == '>':
        if(valorIzq > valorDer):
            setValueTemporal(res, True)
        else:
            setValueTemporal(res, False)
    if operador == '<':
        if(valorIzq < valorDer):
            setValueTemporal(res, True)
        else:
            setValueTemporal(res, False)
    if operador == '>=':
        if(valorIzq >= valorDer):
            setValueTemporal(res,True)
        else:
            setValueTemporal(res,False)
    if operador == '<=':
        if(valorIzq <= valorDer):
            setValueTemporal(res,True)
        else:
            setValueTemporal(res, False)
    if operador == '==':
        if valorIzq == valorDer:
            setValueTemporal(res, True)
        else:
            setValueTemporal(res, False)
            


def resuelveGotoF(cuad, indice):
    direccion = quitaPar(cuad.opdoIzq)
    valorBool = getValueTemp(direccion)
    if(valorBool):
        return indice
    else:
        indice = cuad.res - 1
        return indice

def asignaParametros(cuad):
    global keys
    global moduloActual
    global iRadio
    global sColor
    global bFill
    global iX
    global iY
    global iW
    global iTam
    global iDeg
    global iLent
    global iA
    global iB 
    global iC 


    if moduloActual != 'circulo' and moduloActual != 'cuadro' and moduloActual != 'linea' and moduloActual != 'triangulo':
        if cuad.opdoIzq[0] == '(':
            valorAPasar = quitaPar(cuad.opdoIzq)
        else:
            valorAPasar = cuad.opdoIzq
            valorAPasar = getDireccion(valorAPasar)

        parAPasar = keys.pop()
        scopeAPasar = getScope(valorAPasar)
        if scopeAPasar == 'local':
            valorAPasar = getValueLocal(valorAPasar)
        elif scopeAPasar == 'global':
            valorAPasar = getValueGlobal(valorAPasar)
        elif scopeAPasar == 'temp':
            valorAPasar = getValueTemp(valorAPasar)
        dirParametro = getDireccionPar(parAPasar, pFunciones.peek())
        scopeParametro = getScope(dirParametro)
        if scopeParametro == 'local':
            setValueLocal(dirParametro, valorAPasar)
        elif scopeParametro == 'global':
            setValueGlobal(dirParametro, valorAPasar)
        elif scopeParametro == 'temp':
            setValueTemporal(dirParametro, valorAPasar)
    else:
        if moduloActual == 'circulo':
            parametro = cuad.opdoIzq
            if parametro == "iRadio":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iRadio = int(valor)
            elif parametro == "sColor":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                sColor = valor
            elif parametro == "bFill":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                if valor == 'true':
                    bFill = True
                else: 
                    bFill = False
                
            elif parametro == "iX":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iX = int(valor)
            elif parametro == "iY":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iY = int(valor)
            elif parametro == "iW":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iW = int(valor)
                circulo(iRadio, sColor, bFill, iX, iY, iW)
        elif moduloActual == 'cuadro':
            parametro = cuad.opdoIzq
            if parametro == "iTam":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iTam = int(valor)
            elif parametro == "sColor":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                sColor = valor
            elif parametro == "bFill":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                if valor == 'true':
                    bFill = True
                else: 
                    bFill = False
                
            elif parametro == "iX":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iX = int(valor)
            elif parametro == "iY":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iY = int(valor)
            elif parametro == "iW":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iW = int(valor)
                square(iTam, sColor, bFill, iX, iY, iW)
        elif moduloActual == 'linea':
            parametro = cuad.opdoIzq
            if parametro == "iLent":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iLent = int(valor)
            elif parametro == "sColor":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                sColor = valor
            elif parametro == "iX":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iX = int(valor)
            elif parametro == "iY":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iY = int(valor)
            elif parametro == "iW":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iW = int(valor)
            elif parametro == "iDeg":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iDeg = int(valor)
                linea(iLent, sColor, iX, iY, iW, iDeg)
        elif moduloActual == 'triangulo':
            parametro = cuad.opdoIzq
            if parametro == "iA":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iA = int(valor)
            elif parametro == "iB":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iB = int(valor)
            elif parametro == "iC":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iC = int(valor)
            elif parametro == "sColor":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                sColor = valor
            elif parametro == "bFill":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                if valor == "true":
                    bFill = True
                else:
                    bFill = False
            elif parametro == "iX":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iX = int(valor)
            elif parametro == "iY":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iY = int(valor)
            elif parametro == "iW":
                direccion = getDireccionMain(cuad.opdoIzq)
                scope = getScope(direccion)
                if scope == 'local':
                    valor = getValueLocal(direccion)
                elif scope == 'global':
                    valor = getValueGlobal(direccion)
                elif scope == 'temp':
                    valor = getValueTemp(direccion)
                iW = int(valor)
                triangulo(iA, iB, iC, sColor, bFill, iX, iY, iW)


        
        
        
def resuelveReturn(cuad):
    global valorDeReturn
    global vecMemoriaGlobal
    global vecMemoriaLocal

    opdoIzq = cuad.opdoIzq
    direccion = getDireccion(opdoIzq)
    scope = getScope(direccion)
    if scope == 'local':
        valorDeReturn = getValueLocal(direccion)
    elif scope == 'global':
        valorDeReturn = getValueGlobal(direccion)
    elif scope == 'temp':
        valorDeReturn = getValueTemp(direccion)
    VecIntGlobal = vecMemoriaGlobal
    VecIntLocal = vecMemoriaLocal
    
        
def correMaquina(cuadruplos, direPro, nomProg):
    global dirProc
    global nombrePrograma
    global pFunciones
    global moduloActual
    global keys
    global vecMemoriaGlobal
    global vecMemoriaLocal

    dirProc = direPro
    nombrePrograma = nomProg
    i = 0
    #for indice in range(len(cuadruplos)):
    cuadLength = len(cuadruplos)

    while i < cuadLength:
        cuad = cuadruplos[i]
        if cuad.op == 'GOTOMAIN':    
            i = int(cuad.res) - 1
        if cuad.op == 'GOTO':
            i = int(cuad.res) -1
        if cuad.op == '+' or cuad.op == '-' or cuad.op == '/' or cuad.op =='*' or cuad.op == '=':
             operacionAritmetica(cuad)
        if cuad.op == 'WRITE':
            escribeAPantalla(cuad)   
        if cuad.op == 'READ':
            leeDePantalla(cuad)
        if cuad.op == 'GOTOF':
            i = resuelveGotoF(cuad, i)
        if cuad.op == '<' or cuad.op == '>' or cuad.op == '>=' or cuad.op == '<=' or cuad.op == '==' or cuad.op == '!=':
            resuleveCondicion(cuad)
        if cuad.op == 'ERA':
            pFunciones.push(moduloActual)
            pFunciones.push(cuad.res)
            func = pFunciones.peek()
            vecMemoriaGlobal.append(VecIntGlobal)
            vecMemoriaLocal.append(VecIntLocal)
            if(func != 'circulo' and func != 'cuadro' and func != 'linea' and func != 'triangulo'):
                keys = dirProc[func]['Par'].keys()
            else:
                moduloActual = func
        if cuad.op == 'PARAM':
            asignaParametros(cuad)
        if cuad.op == 'GOSUB':
            pRegresar.push(int(i)+1)
            i = int(cuad.res) - 1
            moduloActual = pFunciones.pop()
        if cuad.op == 'RETURN':
            resuelveReturn(cuad)
            i = pRegresar.pop() - 1
            moduloActual = pFunciones.pop()
        i = i + 1 
         
        
            
        