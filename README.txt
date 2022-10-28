Conecta5
Juego de Conecta 5 usando Python con Pygame basándose en el tradicional Conecta 4

Realizado por:
Christian Durán García - A01654229
Adrian Garcia - A01721043
Diego Bugarin - A01620485

LIBRERÍAS
Las librerías que se utilizan para el funcionamiento del juego son las siguientes:
- numpy # Generar matriz para llevar el control del tablero
- pygame # Generar interfaz visual para el usuario
- sys # Cerrar ventana con interfaz visual una vez concluido el juego
- math # Usado para operación de floor para determinar posición de las fichas del juego

VARIABLES GLOBALES
Se declaran 5 variables globales para el juego:
- int ROW_COUNT # Representa el número de filas para el tablero del juego
- int COL_COUNT # Representa el número de columnas para el tablero del juego
- tuple BLUE # Tupla con el valor RGB del color azul
- tuple WHITE # Tupla con el valor RGB del color blanco
- tuple RED # Tupla con el valor RGB del color rojo
- tuple YELLOW # Tupla con el valor RGB del color amarillo
- int SQUARESIZE # Representa el tamaño de cada cuadro en la ventana gráfica
- inr RADIUS # Representa la magnitud del radio de las fichas y los espacios de las fichas en el tablero

FUNCIONES
Se declaran 7 funciones para el juego:

- create_board() #Función para crear una matriz de ceros que representa el tablero vacío
INPUTS None
Se emplea la función zeros de numpy con ROW_COUNT y COL_COUNT como argumentos
Se crea la variable board que es la matriz de ceros que representa el tablero
RETURN board

- drop_piece(board, row, col, piece) # Función para agregar una ficha
INPUTS board, row, col, piece
Se requiere del tablero, de la fila y la columna que se quiere agregar la ficha, y el tipo de ficha
Se realiza una asignación en la fila y en la columna del tablero de la ficha a agregar
RETURN None

- is_valid_location(board, col) # Función para verificar si es posible agregar una ficha en una columna draw_board
INPUTS board, col
Se requiere del tablero y de la columna en donde se quiere poner la ficha
Se verifica si en el tablero se puede colocar una ficha más en la columna indicada
RETURN bool

- get_next_open_row(board, col) # Función para determinar en qué línea hay que colocar la ficha
INPUTS board, col
Se requiere del tablero y del número de columna en donde se quiere insertar la ficha
Se realiza una evaluación a través de la columna hasta encontrar el punto en donde se puede insertar la ficha
RETURN int r # número de fila a insertar la ficha

- print_board(board) # Función para imprimir el tablero a la terminal
INPUTS board
Únicamente se requiere del tablero
Se realiza un print del tablero volteado través del eje x con la función flip de numpy
RETURN None

- winning_move(board, piece) # Función que checa si existe una condición ganadora en el tablero
Se requiere del tablero y de la ficha a insertar
Se verifican las condiciones de Conecta 5: horizontal, vertical, diagonal positiva, y diagonal negativas

- draw_board(board) # Funcion para dibujar el tablero en la ventana con la interfaz gráfica
INPUTS board
Únicamente se requiere de el tablero
Primero se realiza un ciclo para hacer un setup del juego
Se dibuja el fondo del tablero de color azul y los espacios de las fichas en color blanco como el fondo
Después se realiza otro ciclo para verificar si las casillas de las fichas ya están ocupadas por fichas
Se dibuja la ficha del jugador correspondiente en el espacio correspondiente
Finalmente se actualiza la ventana de la interfaz gráfica
RETURN None

MAIN
Se crean las siguientes variables
- board # Se emplea la función create_board() para crear la matriz del tablero
- game_over # Es un valor booleano que sirve para determinar si el juego sigue o termina, se inicia en False
- turn # Contador para determinar quien es el jugador con el turno en curso, se inicia en 0 para que después del set up vaya el jugador 1

Se inicializa pygame con el método init() # Se inicializa antes de la declaración de las siguientes variables porque se utiliza en éstas

- width # Es el ancho de la ventana, es COL_COUNT * SQUARESIZE
- height # Es la altura de la ventana, ES (ROW_COUNT + 1) * SQUARESIZE, se agrega una fila para poder tener espacio para visualizar la ficha a poner
- size # Tupla con los valores de anchura y altura de la ventana con la interfaz gráfica del juego
- screen # Objeto display de pygame con el tamaño usando el valor de size

Se dibuja el tablero con la función draw_board()
Se actualiza la ventana gráfica con display.update() de pygame

Se crea un ciclo que contiene lo siguiente:

Se toma un evento de pygame que es una acción del usuario
Si es la tecla esc se termina el juego
El movimiento del ratón sirve para mover la ficha a poner y se obtiene la posición de la columna
Si es un clic se ejecutan las funciones correspondientes para ingresar la ficha en el lugar correspondiente
Se evalua si existe una condición de ganador en el tablero con winning_move(board) y se toma el estado actual del tablero
Se despliega un mensaje se ganador del color del jugador que ganó
Se hace un cálculo para el cambio de turno
Si se termina el juego existe una espera para salir de la pantalla