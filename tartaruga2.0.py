import random
import turtle

turtle.colormode(255)
t = turtle.Turtle()
t.speed(30) # define a velocidade máxima
for _ in range(25):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor(r, g, b)
    t.circle(50) # desenha um círculo com raio 50
    t.right(10) # girar 10 graus

turtle.done()