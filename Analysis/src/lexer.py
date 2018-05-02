# coding=utf-8
import ply.lex as lex
import re
import codecs
import os
import sys




#Tokens 
tokens = ('END','CIRCLE','LINE','TRIANGLE','SQUARE','BOOL', 'RETURN','INTEGER', 'DECLARE','INT','FLOAT','STRING','BOOL','VOID','MAIN','IF','ELSE','DO','WHILE','FOR','WRITE','READ','FUNCTION', 'PROGRAM','ID','ASSGN',  'TYPE', 'COMMA', 'DOT', 'CYCLE', 
    'COLON', 'SEMICOLON','FLOATNUMB', 'LEFTBRACK', 'RIGHTBRACK', 'LEFTPAR', 'RIGHTPAR', 'LEFTKEY', 'RIGHTKEY', 'QUOTE',
    'SUM', 'OR','AND','ACTINCR', 'ACTINCRVALOR', 'ACTDECRVALOR', 'ACTDECR', 'LEFTBRACK','MINUS', 'MULTP', 'DIVIDE', 'GRTR', 'LESS', 'EQ', 'NOTEQ', 'GRTREQ', 'LESSEQ', 'NUMBER', 'newline', 'SPACE'
)
reservadas = {
    'program' : 'PROGRAM',
    'end' : 'END',
    'declare' : 'DECLARE',
    'main' : 'MAIN',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'do' : 'DO', 
    'write' : 'WRITE',
    'read' : 'READ',
    'funct' : 'FUNCTION',
    'circulo' :  'CIRCLE',
    'and' : 'AND',
    'cuadro' : 'SQUARE',
    'or' :  'OR',
    'return' : 'RETURN',
    'paint' : 'PAINT',
    'bool' : 'BOOL',
    'float' : 'FLOAT',
    'int' : 'INT', 
    'string' : 'STRING',
    'void' : 'VOID',
    'linea' : 'LINE',
    'rectangulo' : 'RECTANGLE',
    'triangulo' : 'TRIANGLE'

}





#tokens = tokens + list(reservadas.values())

#Tokens definidos

#t_SPACE = r'\D'

t_ignore = ' \t'
t_ASSGN = r'='
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_SEMICOLON = r';'
t_LEFTBRACK = r'\['
t_RIGHTBRACK = r'\]'
t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'
t_LEFTKEY = r'{'
t_RIGHTKEY = r'}'
t_QUOTE = r'"'
t_SUM = r'\+'
t_MINUS = r'\-'
t_MULTP = r'\*'
t_DIVIDE = r'/'
t_GRTR = r'>'
t_LESS = r'<'
t_EQ = r'=='
# t_ACTINCR = r'\++'
# t_ACTDECR = r'--'
# t_ACTINCRVALOR = r'\+='
# t_ACTDECRVALOR = r'\-='
t_NOTEQ = r'!='
t_GRTREQ = r'>='
t_LESSEQ = r'<='
t_INTEGER = r'[\+,-]?\d+'
t_FLOAT = r'[+,-]?[0-9]+\.[0-9]+((E|e)[+,-]?[0-9]+)?'


#Funcion para definir la expresion regular de un BOOL
def t_BOOL(t):
    r'false|true'
    return t

#Funcion para definir la expresion regular de un ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value,'ID')
    return t

#Funcion para definir la expresion regular de un salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    





#Funcion para definir la expresion regular de un comentario
def t_COMMENT(t):
    r'\#.*'
    pass
#Funcion para definir la expresion regular de un error. Saca a pantalla
#el mensaje de un carater ilegal(no aceptado por el lenguaje)
def t_error(t):
    print " caracter ilegal '%s'" % t.value[0]
    t.lexer.skip(1)

#Funcion para buscar los archivos de prueba. Su proposito es para debugging
#def buscarFicheros(directorio):
#    ficheros = []
#    numArchivo = ''
#    respuesta = False
#    contador = 1

 #   for base, dirs, files in os.walk(directorio):
 #       ficheros.append(files)
 #   for file in files: 
 #       print str(contador) + ". " + file
 #       contador = contador + 1

 #  while respuesta == False:
  #      numArchivo = raw_input('\nNumero de test: ')
  #      for file in files:
   #         if file == files[int(numArchivo)-1]:
    #            respuesta = True
     #           break
    
    #print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]
    #return files[int(numArchivo)-1]

#directorio = '/Users/ricardolicea/OneDrive/Tecnológico de Monterrey/8vo Semestre/EM18 Diseño de Compiladores/MIRI/Analysis/test/'
#archivo  = buscarFicheros(directorio)
#test = directorio + archivo
#fp = codecs.open(test,"r","utf-8")
#cadena  = fp.read()
#fp.close()
analizador = lex.lex()
#analizador.input(cadena)


#while True:
 #   tok = analizador.token()
  #  if not tok : break
   # print(tok)