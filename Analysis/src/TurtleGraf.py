from turtle import *

def square(tam,col,fill,x,y,w):

    ht()
    width(w)
    color(col)
    up()
    goto(x,y)
    down()
    if fill:
        begin_fill()
        forward(tam)
        left(90)  
        forward(tam)
        left(90)  
        forward(tam)
        left(90)  
        forward(tam)
        left(90)  
        end_fill()
        done()
    else:
        forward(tam)
        left(90)
        forward(tam)
        left(90)  
        forward(tam)
        left(90)  
        forward(tam)
        left(90)  
        done()
        
def circulo(radio,col,fill,x,y,w):

    ht()
    color(col)
    width(w)
    up()
    goto(x,y)
    down()
    if fill:
        begin_fill()
        circle(radio)
        end_fill()
        done()
    else:
        circle(radio)
        done()


def triangulo(a,b,c,col,fill,x,y,w):

    ht()
    width(w)
    color(col)
    up()
    goto(x,y)
    down()

    if fill:
        begin_fill()
        forward(a)
        left(120)
        forward(b)
        left(120)
        forward(c)
        end_fill()
        done()
    else:
        forward(a)
        left(120)
        forward(b)
        left(120)
        forward(c)
        done()


def linea(lent,col,x,y,w,deg):

    ht()
    width(w)
    color(col)
    up()
    goto(x,y)
    down()
    left(deg)
    forward(lent)
    done()

def rectangulo(hei,wi,col,fill,x,y,w):

    ht()
    color(col)
    up()
    goto(x,y)
    down()
    width(w)

    if fill:
        begin_fill()
        forward(wi)
        left(90)
        forward(hei)
        left(90)
        forward(wi)
        left(90)
        forward(hei)
        end_fill()
        done()
    else:
        forward(wi)
        left(90)
        forward(hei)
        left(90)
        forward(wi)
        left(90)
        forward(hei)
        done()
    
#square(100,'blue',True,10,40,5)
#circulo(100,'red',False,43,321,1)
#linea(100,'blue',100,54,2,45)
#rectangulo(50,100,'red',False,10,40,3)
#triangulo(200,200,200,'yellow',True,78,87,4)