import turtle
t = turtle.Pen()
#t.forward(50)
#t.left(90)
#t.forward(50)
#t.left(90)
#t.forward(50)
#t.left(90)
#t.forward(50)
#turtle.getscreen()._root.mainloop()
##t.reset()

##for x in range(1,6):
##    t.forward(100)
##    t.left(45)

##t.rest()

#def micuadrado(size):
#    for x in range(1,5):
#        t.forward(size)
#        t.left(90)
#        
#micuadrado(180)

# dibujo solbre la estrella de n lados pares e impares
#n = int(input("ingrese un numero "))
#angulo = 180/n
#if n%2==0:
#    for i in range(0,n):
#        t.forward(100)
#        t.left(angulo*2)
#else:
#    for i in range(0,n):
#        t.forward(100)
#        t.left(angulo*4)

def nombre():
    t.left(135)
    t.forward(50)
    
    t.left(225)
    t.forward(150)
    
    t.left(270)
    t.forward(300)
    
    t.left(270)
    t.forward(200)
    
    t.left(270)
    t.forward(150)
    
    t.right(90)
    t.forward(30)
    
    t.right(90)
    t.forward(120)
    
    t.left(90)
    t.forward(140)
    
    t.left(90)
    t.forward(250)
    
    t.left(90)
    t.forward(70)
    
    t.left(135)
    t.forward(20)
    
    t.left(225)
    t.forward(30)

    
    
nombre()
turtle.getscreen()._root.mainloop()
