from piece import Piece
import pygame
from constansts import BLACK, ROWS, RED, SQUARE_SIZE
import numpy as np
import time

class Board:
    def __init__(self, win):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.win = win
        
    def draw_squares(self):
        self.win.fill(BLACK)
        time.sleep(1)

        for row in range(ROWS):
            # range(principio, fin, tamano_de_paso)
            for col in range(row % 2, ROWS, 2):
                # un error en el contenido del tercer argumento "rect"
                # las posiciones en el tuple tiene que estar multiplicados por el tamaño de los cuadros
                # (r,g,b)
                # r = np.random.randint(0,255)
                # g = np.random.randint(0,255)
                # b = np.random.randint(0,255)

                # altura = np.random.randint(10,200)
                # ancho = np.random.randint(10,200)
                # pygame.draw.rect(surface, color, rect)
                # rect = (x,y, altura, ancho)
                pygame.draw.rect(self.win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                # colores lindos:
                #pygame.draw.rect(self.win, (row*20, col*20, col*10+row*10), (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
    def create_board(self):
        pieza1 = Piece(row=0, col=1, color=RED)
        pieza1.draw(self.win)
        pieza2 = Piece(row=5, col=1, color=BLACK)
        pieza2.draw(self.win)
        pieza3 = Piece(row=0, col=3, color=RED)
        pieza3.draw(self.win)
        
