# coding=utf-8
from cuadruplos import *
from TurtleGraf import *
from MemoriaV import *
from parser import *
import sys


def MaquinaVirtual():
    # Aqui ponemos todos los metodos que se necesiten para ejecutar todo
    # Los ponemos en orden de ejecucion
    # 1. Meter a memoria las variables gloales y locales sacandolas del dirProc
    # 2. Meter a memoria las variables temporales de los cuadruplos
    # 3. Despues de haber metido ya a memoria las direcciones de todo 
    #     podemos empezar a hacer uso de la MV.

    #Funcion para meter a memoria todo leyendo del dir proc y de los cuadruplos 


    #4. despues de meter a memoria recorremos el vector de cuadruplos para ejecutar los 
    # acciones y a su vez meter a memoria con los metodos que ya estan definidos en la clase memoriaV.

    #Hacer las funciones para cada ejecucion, de los parametros ej. suma, resta, mult, division 

    # PRIMERO HACER OPERACIONES ARITMETICAS LUEGO PENSAR EN LO DEMAAS.
    None


def operacionAritemtica():
    cuadActual = 0
    cuadMain = cuadruplos[0].res

    for c in cuadruplos:

def OpAssign():

    for c in cuadruplos:
        if c.op == '=':
           d = getValueTemp(c.opdoIzq)
        for i in Modulos
            dire = dirProc[i]['Vars'][c.res]['Dir']
        t = getScope(dire)
        if t == 'local':
            setValueLocal(dire,d)
        elif t == 'global'
            setValueGlobal(dire,d)



        

    


        

    

    

            





        
  

            







    


    











