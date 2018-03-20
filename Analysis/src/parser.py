import ply.yacc as yacc
import os
import codecs
import re
from lexer.py import tokens
from sys import stdin

precedence = (
    ('right', 'ASSGN'),
    ('left', 'AND'),
    ('left', 'OR'),
    ('left', 'NOTEQ'),
    ('left', 'EQ'),
    ('left', 'GRTR', 'GRTREQ', 'LESS', 'LESSEQ'),
    ('left', 'SUM', 'MINUS'),
    ('left', 'MULTP', 'DIVIDE'),
    ('left', 'LEFTPAR', 'RIGHTPAR')

)

def p_program(p):
    '''program = PROGRAM ID ; declare funct main END ; ''' 
    print("program")
    p[0] = 

def p_declare(p):
    ''' declare = DECLARE type ID  '''