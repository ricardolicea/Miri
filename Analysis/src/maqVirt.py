# coding=utf-8

from MemoriaV import *
import sys
from structs import *

moduloActual = "main"
dirProc = "None"
nombrePrograma = ""
pFunciones = Stack()
pRegresar = Stack()
keys = None
valorDeReturn = None

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
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) * fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer =='local':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) * fixType(direccionDer, getValueLocal(direccionDer))
                elif scopeDer =='temp':
                    respuesta = fixType(direccionIzq, getValueGlobal(direccionIzq)) * fixType(direccionDer, getValueTemp(direccionDer))
            elif scopeIzq == 'local':
                if scopeDer == 'global':
                    respuesta = fixType(direccionIzq, getValueLocal(direccionIzq)) * fixType(direccionDer, getValueGlobal(direccionDer))
                elif scopeDer == 'local':
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
            else:
                direccionIzq = getDireccion(opdoIzq)
                scope1 = getScope(direccionIzq)
                if scope1 == 'local':
                    v = getValueLocal(direccionIzq)
                    setValueLocal(direccion,v)
                elif scope1 == 'temp':
                    v = getValueTemp(direccionIzq)
                    setValueTemporal(direccion,v)
                else:
                    v = getValueGlobal(direccionIzq)
                    setValueGlobal(direccion,v)
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
        valorAPasar = cuad.opdoIzq
        parAPasar = keys.pop()
        valorAPasar = getDireccion(valorAPasar)
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
        
        
        
def resuelveReturn(cuad):
    global valorDeReturn
    opdoIzq = cuad.opdoIzq
    direccion = getDireccion(opdoIzq)
    scope = getScope(direccion)
    if scope == 'local':
        valorDeReturn = getValueLocal(direccion)
    elif scope == 'global':
        valorDeReturn = getValueGlobal(direccion)
    elif scope == 'temp':
        valorDeReturn = getValueTemp(direccion)
    
        
def correMaquina(cuadruplos, direPro, nomProg):
    global dirProc
    global nombrePrograma
    global pFunciones
    global moduloActual
    global keys

    dirProc = direPro
    nombrePrograma = nomProg
    i = 0
    #for indice in range(len(cuadruplos)):
    cuadLength = len(cuadruplos)

    while i < cuadLength:
        cuad = cuadruplos[i]
        if cuad.op == 'GOTOMAIN':    
            i = cuad.res - 1
        if cuad.op == 'GOTO':
            i = cuad.res -1
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
            keys = dirProc[func]['Par'].keys()
        if cuad.op == 'PARAM':
            asignaParametros(cuad)
        if cuad.op == 'GOSUB':
            pRegresar.push(i)
            i = cuad.res - 1
            moduloActual = pFunciones.pop()
        if cuad.op == 'RETURN':
            resuelveReturn(cuad)
            i = pRegresar.pop()
            moduloActual = pFunciones.pop()
        i = i + 1    
        
            
        