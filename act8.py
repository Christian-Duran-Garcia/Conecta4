"""
Christian Durán García - A01654229
Adrian Garcia - A01721043
Diego Bugarin - A01620485
"""
# Importar Librerías
from random import *
from turtle import *
from freegames import path

# Declarar los objetos para el juego
car = path('car.gif') # Imagen de fondo
tiles = list(range(32)) * 2 # Cuadros que ocultan la imagen
state = {'mark': None} # Estado de los cuadros
hide = [True] * 64 # Estado de descubierto u oculto de los cuadros
counter = 0 # Contador para el número de los taps

# Agregar colores a los números para incrementar la dificultad
colors = ['red', 'yellow', 'green', 'blue', 'cyan']
rd_color = 'black' # El primer número empieza en negro

# Función para dibujar los cuadrados blancos que cubren la imagen
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Función para calcular las coordenadas del índice de los tiles
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Función para conseguir la posición de los tiles
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Función para realizar acciones cada vez que el usuario hace un tap
def tap(x, y):
    spot = index(x, y)
    mark = state['mark']
    
    # Se llaman las variables globales para poder utilizarlas y modificarlas
    global counter
    global rd_color

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Actualización de variables globales
    counter += 1
    rd_color = sample(colors, 1)[0]

# Función que dibuja el estado del tablero dependiendo de la condición de los tiles
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
        color(rand_color) # Obtener un color random
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

# Mezclar las tiles para que sean distintas cada corrida del juego
shuffle(tiles)

# Incremento del tamaño de la pantalla para mostrar el contador
setup(600, 600, 370, 0)

# Agregar la figura del coche
addshape(car)

# Ocultar la tortuga
hideturtle()

# Eliminar la animación de la tortuga
tracer(False)

# Ejecutar la función de tap al momento de que el usuario da un click en la pantalla
onscreenclick(tap)

# Ejecutar función de dibujar con un color random para el índice de los tiles
draw(rd_color)

# Terminar el ciclo de la tortuga
done()