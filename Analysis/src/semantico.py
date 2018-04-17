txt = " "
iCont = 0
def incrementarContador():
    global iCont
    iCont += 1
    return "%d" %iCont

class Nodo():
    pass
    
class Null():
    def __init__(self):
        self.type = 'void'

    def imprimir(self, ident):
        print ident + "nodo nulo"

    def traducir(self): 
        global txt
        id = incrementarContador()
        txt += id + "[label = " + "nodo_nulo" + "]" + "\n\t"

        return id
    


class program(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        print ident + "Nodo: " + self.name


    def traducir(self):
        global txt
        id = incrementarContador()
        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        txt+=id+"[label = "+self.name+"]"+"\n\t"
        txt+=id+" -> "+son1+"\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
    

class program2(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt+=id+"[label= "+self.name+"]"+"\n\t"
        txt+=id+" -> "+son1 + "\n\t"
        txt+=id+" -> " + son2 + "\n\t"

        return id
    

#class program2Empty(Nodo):
#    def __init__(self,name):
#        self.name = name
#    def traducir(self):
#        global txt
#        id = incrementarContador()
#        return id
#    

class program3(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
   

#class program3Empty(Nodo):
#    def __init__(self,name):
#        self.name = name
#    def traducir(self):
#        global txt
#        id = incrementarContador()
#        return id
#   

class declare(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name
    
    def traducir(self):
        global txt
        id = incrementarContador()
        if type(self.son1) == type(tuple):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        return id
    

class declareRecursivo(Nodo):
    def __init__(self,son1, son2, son3, son4,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t" 
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id
    

#class declareResursivoEmpty(Nodo):
#    def __init__(self,name):
#        self.name = name
#    def traducir(self):
#        global txt
#        id = incrementarContador()
#        return id
#    

#class declareEmpty(Nodo):
#    def __init__(self,name):
#        self.name = name
#    def traducir(self):
#        global txt
#        id = incrementarContador()
#        return id
#    

class declare2(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
    
    

# class declar2Empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
    

class declare3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
    
    

# class declare3Empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
   

class array(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
    

# class arrayEmpty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
    
class typeClass(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
    
class type2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
   
class type2Float(Nodo):
    def __init__(self,son1, name):
        self.name = name

    
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
    

class type2String(Nodo):
    def __init__(self, son1, name):
        self.name = name

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
    

class type2Bool(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
    

class type2Void(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id

class cuerpo(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class cuerpo2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
  

# class cuerpo2Empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
   
class est(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id

class estCycle(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
   

class estRead(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
    

class estWrite(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 =  son1
    
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
   

class estAassignment(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1 
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir (" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id
   

class estFunct(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id
   
# class estEmpty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
   

class assignment(Nodo):
    def __init__(self,son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else: 
            self.son3.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id
    
class conditional(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else: 
            self.son3.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id
   

class conditional2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
    
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
    

# class conditional2Empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
    

class cycles(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
    

class cyclesFor(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
    

class cyclesDoWhile(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
    

class doWhile(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
    
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
    

class whileClass(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
    
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
    
    

class while2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
    
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
    

# class while2Empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
   

class forClass(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" " + ident)
        else:
            self.son5.imprimir(" " + ident)
        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        if type(self.son2) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        if type(self.son5) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
    
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"

        return id
    
    

class arithmeticOpPlus(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
    

class arithmeticOpMinus(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
   

    #FALTA AGREGAR LAS DE MULTP Y DIIVDE

class for2(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id
    
   

# class for2empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
  

class for3(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
    
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
    

   

# class for3empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
    

class exp(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        return id
   

class exp2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else: 
            self.son3.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id
   
   

class expr2Grtr(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
   


class exp2Equal(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
   

class exp2NotEq(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
   

class exp2And(Nodo):
    def __init__(self, self1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
    

class exp2OR(Nodo):
    def __init__(self,name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
   

class exp2Arithemti(Nodo):
    def __init__(self,son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
   

class arithmeticExp(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" " + ident)
        else:
            self.son5.imprimir(" " + ident)
        
        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" " + ident)
        else:
            self.son6.imprimir(" " + ident)


        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        if type(self.son2) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        if type(self.son5) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son6) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"

        return id
    
   

# class arithmeticExpEmpty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
    
# class exp2Empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
    

class output(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
    
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

   

class output2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
    
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

    

# class output2Empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
    

class inputClass(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
		

        return id
   

class funct(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        
        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" " + ident)
        else:
            self.son5.imprimir(" " + ident)
        
        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" " + ident)
        else:
            self.son6.imprimir(" " + ident)


        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()
        
        if type(self.son2) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        if type(self.son5) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son6) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"

        return id
    
   

class funct2(Nodo):
    def __init__(self, son1, son2, son3, son4,  name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
    def imprimir(self, ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)
        
        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)
        print ident + "Nodo: " + self.name

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()
        
        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id

class Id(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "ID: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = " + self.name + "]" + "\n\t"

        return id
class Int(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Int: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = " + self.name + "]" + "\n\t"

        return id
class Float(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Float: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = " + self.name + "]" + "\n\t"

        return id
class String(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "String: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = " + self.name + "]" + "\n\t"

        return id
    
class Bool(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Bool: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = "  + self.name + "]" + "\n\t"

        return id
class Void(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Void: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = " + self.name + "]" + "\n\t"

        return id

class Assign(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Assign: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = \""  + self.name + "]" + "\n\t"

        return id

class Sum(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Sum: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = \""  + self.name + "]" + "\n\t"

        return id
class Minus(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Minus: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = \"" + self.name + "]" + "\n\t"

        return id

class Less(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Less: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = \"" + self.name + "]" + "\n\t"

        return id

class Grtr(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Grtr: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = \"" + self.name + "]" + "\n\t"

        return id

class Eq(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Eq: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = \"" + self.name + "]" + "\n\t"

        return id

class notEq(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "notEq: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = \"" + self.name + "]" + "\n\t"

        return id
class And(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "And: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = " + self.name + "]" + "\n\t"

        return id

class Or(Nodo):
    def __init__(self, name):
        self.name = name
    def imprimir(self, ident):
        print ident + "Or: " + self.name
    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label = " + self.name + "]" + "\n\t"

        return id


# class funct2Empty(Nodo):
#     def __init__(self,name):
#         self.name = name
#     def traducir(self):
#         global txt
#         id = incrementarContador()
#         return id
    

class empty(Nodo):
    def __init__(self,name):
        self.name = name
    def traducir(self):
        global txt
        id = incrementarContador()
        return id
    