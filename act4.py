"""
Christian Durán García - A01654229
Adrian Garcia A01721043
Diego Bugarin - A01620485
"""
# Importar la librerias necesarias
from random import randrange
import random as rd
from turtle import *
from freegames import square, vector
import sys

# Declarar los vectores de los objetos del juego
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Una lista con los 5 colores para la serpiente y la comida
colors = ['yellow', 'cyan', 'purple', 'green', 'orange']
color = rd.sample(colors, 2)

# Lista con vectores para el movimiento de la comida
moves = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]

# Funcion para cambiar la direccion de la serpiente
def change(x, y):
    aim.x = x
    aim.y = y

# Funcion para determinar si la cabeza de la serpiente está dentro de los límites de la pantalla
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# Funcion para mover la serpiente
def move():
    head = snake[-1].copy()
    head.move(aim)

    # Si la cabeza de la serpiente sale de la pantalla o está en el cuerpo de la serpiente el juego acaba
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        sys.exit()
        return

    # Agregar un bloque a la serpiente
    snake.append(head)

    # Reubicar la comida si la cabeza tiene la misma posición que la comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Pintar de color negro el cuerpo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, color[0])

    # Darle color a la comida, y darle posición
    square(food.x, food.y, 9, color[1])
    
    if not inside(food):
        square(food.x, food.y, 9, color[1])
    else:
        food.move(rd.sample(moves, 1)[0])

    update()
    ontimer(move, 100)

# Darle tamaño a la ventana
setup(420, 420, 370, 0)

# Esconder la tortuga en la pantalla (no mostrar el cursor)
hideturtle()

# No poner la animación de la tortuga en la pantalla
tracer(False)

# Tomar el input del teclado del usuario
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Ejecutar función de movimiento
move()

# Terminar el ciclo del juego
done()