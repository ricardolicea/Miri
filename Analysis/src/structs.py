# coding=utf-8
############################################################
#Nombre del archivo: structs.py
#Autores: 
# Ricardo Licea Mata A01280892
# Miguel Bazan Aviña A01281010
#
#Función del archivo:
#Este archivo corresponde a las estructuras de datos que utilizamos
#dentro del desarrollo del proyecto. Tiene dos clases:Queue y Stack,
#que son las estructuras usadas, por ejemplo, en las pilas de Operadores,
#Operandos y Saltos para generación de codigo intermedio
#
#
#############################################################


Vec = []

class Queue():

    """Constructor"""
    def __init__(self):
        self.items = []

    """Revisa si la queue esta vacia"""
    def isEmpty(self):
        return self.items == []

    """Agrega un elemento a la queue"""
    def enqueue(self, item):
        self.items.insert(0,item)

    """Saca un elemento de la queue"""
    def dequeue(self):
        return self.items.pop()

    """Regresa el tamano(numero de elementos) de la queue"""
    def size(self):
        return len(self.items)
        
    """Regresa todos los elementos en la queue"""
    def getElements(self):
        return self.items

    """Regresa el primer elemento de la queue sin sacarlo"""
    def peek(self):
        return self.items[len(self.items)-1]


class Stack():

    """Constructor"""
    def __init__(self):
        self.items = []

    """Revisa si el stack esta vacio"""
    def isEmpty(self):
        return self.items == []

    """Agrega un elemento al stack"""
    def push(self, item):
        return self.items.append(item)

    """Saca un elemento del stack"""
    def pop(self):
        return self.items.pop()

    """Sirve para ver el elemento superior del stack sin removerlo"""
    def peek(self):
        return self.items[len(self.items)-1]

    """Sirve para ver el segundo elemento superior del stack sin removerlo"""  
    def peekSecond(self):
        return self.items[len(self.items)-1]

    """Despliega todos los elementos del stack"""
    def getElements(self):
        return self.items

    """Regresa el tamano ( numero de elementos) del stack"""
    def size(self):
        return len(self.items)


class Direc():

    def __init__(self,var,modulo,direccion):
        self.var = var
        self.modulo = modulo
        self.direccion = direccion


def pushInfo(dire):
    global Vec
    Vec.append(dire)
