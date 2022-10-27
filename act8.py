from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
counter = 0
colors = ['red', 'yellow', 'green', 'blue', 'cyan']
rd_color = 'black'

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    global counter
    global rd_color

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    counter += 1
    rd_color = sample(colors, 1)[0]

def draw(rand_color):
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    global counter
    global rd_color

    # Dibujar los cuadrados blancos en caso de que los tiles esten ocultos
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    # Asignar la marca del cuadro tiene una marca
    mark = state['mark']

    # Dibujar los numeros de las tiles que estan ocultas
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        color(rand_color)
        if tiles[mark] < 10:
            goto(x + 17, y) # Posicion centrada para numeros de un solo digito
            write(tiles[mark], font=('Arial', 30, 'normal'))
        else:
            goto(x + 3, y) # Posicion centrada para numeros de dos digitos
            write(tiles[mark], font=('Arial', 30, 'normal'))
    
    # Verificar si los tiles estan todos descubiertos
    if not any(hide):
       return

    # Mostrar el contador de taps
    up()
    goto(0, 200)
    color('black')
    write(counter, font=('Arial', 30, 'normal'))

    # Actualizar la ventana
    update()
    ontimer(draw(rd_color), 100)

shuffle(tiles)
setup(600, 600, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw(rd_color)
done()