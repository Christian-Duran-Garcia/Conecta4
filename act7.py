"""
Christian Durán García - A01654229
Adrian Garcia - A01721043
Diego Bugarin - A01620485
"""
# Importar librerias
from random import randrange
from turtle import *
from freegames import vector

# Crear objetos para el juego, pelota, velocidad, y balones
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# Funcion con acciones a realizar al momento de dar click en la pantalla
def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 400) / 25
        speed.y = (y + 400) / 25

# Funcion para determinar si un objeto esta dentro de la pantalla
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Funcion para dibujar los balones y la pelota
def draw():
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# Funcion que realiza los movimientos del juego
def move():
    # Generar un nuevo balon en una posicion aleatoria
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Darle una velocidad a cada balon
    for target in targets:
        target.x -= 1.5

    # Darle el movimiento parabolico a la pelota
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Generar una copia de los targets
    dupe = targets.copy()
    targets.clear()
    
    # Si los targets se encuentran en el dupe, se eliminan
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    # Actualizar la ventana del juego
    draw()

    # Si los targets salen de a pantalla se eliminan de la lista de balones
    for target in targets:
      if not inside(target):
        targets.remove(target)

    ontimer(move, 50)

# Setup de la pantalla
setup(420, 420, 370, 0)

# Eliminar la tortuga
hideturtle()

# Levantar la tortuga
up()

# Quitar la animacion de la tortuga
tracer(False)

# Ejecutar la funcion tap al momento de dar click en la pantalla
onscreenclick(tap)

# Ejecutar la funcion move
move()

# Terminar el ciclo del juego
done()