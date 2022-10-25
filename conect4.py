# Importar librerias
import numpy as np
import pygame
import sys
import math

# Declarar variables globales
ROW_COUNT = 6
COL_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Funcion para crear una matriz que representa el tablero
def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

# Funcion para agregar una ficha
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Funcion para verificar si es posible poner una ficha en la columna
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

# Funcion para saber en qué línea hay que colocar la ficha
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
    pass

# Funcion para imprimir el tablero de manera correcta
def print_board(board):
    print(np.flip(board, 0))

# Checar por victorias
def winning_move(board, piece):
    # Checar horizontalmente
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Checar verticalmente       
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+3][c] == piece and board[r+3][c] == piece:
                return True

    # Checar diagonales positivas
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Checar diagonales negativas
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    # Iterar por todo el tablero para hacer un set up del juego
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    # Iterar sobre todo el tablero para dibujar la ficha indicada
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    pygame.display.update()


# Creando tablero de conecta 4
board = create_board()
# print_board(board) # Imprimir el tablero en la consola
game_over = False
turn = 0 # Variable para identificar el jugador

# Inicializando PYGAME
pygame.init()

# Determinando tamaño del display y medidas para las figuras a dibujar
SQUARESIZE = 90
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
screen = pygame.display.set_mode(size)

# Dibujar el tablero y refrescar la pantalla
draw_board(board)
pygame.display.update()

# Declarar la fuente para dibujar el mensaje de ganador
myfont = pygame.font.SysFont("monospace", 75)

while not game_over:
    # Manejar el evento de PYGAME
    for event in pygame.event.get():
        # En caso de salir, que se termine el juego
        if event.type == pygame.QUIT:
            sys.exit()

        # Dibujar la ficha en el lugar en donde se puede colocar, arriba del tablero
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0] # Obtener la poscion horizontal del mouse en la ventana
            if turn == 0: # Ficha para Jugador 1
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else: # Ficha para Jugador 2
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:
            # Dibujar un rectángulo negro para dejar de mostrar la ficha potencial
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))

            # Preguntar por el input del jugador 1
            if turn == 0:
                # Conseguir la posición en la ventana en la cual colocar la ficha
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                # Colocar la ficha en el lugar adecuado en caso de estar disponible
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    # Despleagar mensaje de ganador en caso de hacer un movimiento ganador
                    if winning_move(board, 1):
                        label = myfont.render("GANADOR!!!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

            # Preguntar por el input del jugador 2
            else:
                # Conseguir la posición en la ventana en la cual colocar la ficha
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                # Colocar la ficha en el lugar adecuado en caso de estar disponible
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    # Despleagar mensaje de ganador en caso de hacer un movimiento ganador
                    if winning_move(board, 2):
                        label = myfont.render("GANADOR!!!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True

            # Desplegar el tablero tanto en consola como en la ventana
            print_board(board)
            draw_board(board)
            
            # Alternan entre turnos 1 y 2
            turn += 1
            turn = turn % 2
            
            # Esperar 3 segundos antes de cerrar la ventana
            if game_over:
                pygame.time.wait(3000)