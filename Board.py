from piece import Piece
import pygame
from constansts import BLACK, ROWS, RED, SQUARE_SIZE, WHITE, COLS
import numpy as np
import time

class Board:
    def __init__(self, win):
        self.datos_de_fichas = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.win = win
        self.create_board()
        
    def draw_squares(self):
        self.win.fill(BLACK)

        for row in range(ROWS):
            # range(principio, fin, tamano_de_paso)
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(self.win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
    def crear_datos_de_fichas(self): # tenemos que cambiar este nombre
       
        for row in range(ROWS):
            self.datos_de_fichas.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.datos_de_fichas[row].append(Piece(row,col,WHITE))
                    elif row > 4:
                        self.datos_de_fichas[row].append(Piece(row,col,RED))
                    else:
                        self.datos_de_fichas[row].append(None)
                else:
                    self.datos_de_fichas[row].append(None)
        print("cols y rows", COLS, ROWS)
        print("Tamano del tablero", len(self.datos_de_fichas), len(self.datos_de_fichas[0]))
    
    def draw(self):
        self.draw_squares()
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.datos_de_fichas[row][col]
                if piece is not None:
                    piece.draw(self.win)
        
