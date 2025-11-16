import turtle

t = turtle.Turtle()
t.pensize(3) # define a espessura da caneta

cores = ("green","blue","yellow","red","cyan","purple","orange","black")

for cor in cores:
    t.pencolor(cor)
    t.forward(100) # andar para frente
    t.right(45) # girar 45 graus

turtle.done()