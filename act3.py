"""
Christian Durán García - A01654229
Adrian Garcia A01721043
Diego Bugarin - A01620485

"""

from turtle import *
from freegames import vector

# Funcion para dibujar un linea desde un punto de inicio hasta un punto final
def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Funcion para dibujar un cuadrado empezando de la esquina inferior izqauierda y terminando en la superior derecha
def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Funcion para dibujar un circulo inciando del centro hasta el perimetro
def draw_circle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    circle(end.x - start.x)
    end_fill()

# Funcion para dibujar un rectangulo
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)

    end_fill()

# Funcion para dibujar un triangulo equilatero calculando la longitud de los lados
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    forward(end.x - start.x)
    left(120)
    forward(end.x - start.x)
    left(120)
    forward(end.x - start.x)
    end_fill()
    left(120)

# Funcion para poder almacenar la posicion del tap del mouse o dibujar una forma
def tap(x, y):
    start = state['start']

    # Asignacion de posiciones
    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# Modificar el contenido del diccionario que se usa para ejecutar las acciones del usuario
def store(key, value):
    state[key] = value

# Diccionario que almacena el punto de inicio y la accion a realizar
state = {'start': None, 'shape': line}

# Punto de inicio del juego
setup(420, 420, 370, 0)

# Al dar click realizar la funcion tap, almacenar nueva posicion y realizar accion en diccionario
onscreenclick(tap)

# Captar el input del teclado del usuario
listen()

# Deshacer la figura creada presionando u
onkey(undo, 'u')

# Modificar el color y forma a generar dependiendo del input del usuario
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

# Mantener loop para la herramienta grafica
done()