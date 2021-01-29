
import pygame
from constansts import WIDTH, HEIGHT
from Board import Board

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def main():
    
    run = True
    clock = pygame.time.Clock()
    board = Board(WIN) # A.
    while run: #C
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                 pass

        # 1. variables de nuestra logico del juego - guardado en memoria
        # 2. representacions de la ventana/pantalla de pygame - los variables dentro de pygame
        # 3. lo que vimos en la pantalla (memoria de la pantalla)
        
        board.crear_datos_de_fichas() #B # iniciar nuestra representacion del tablero
        board.draw() # poner los cambios del ventana del tablero en memoria

        pygame.display.update() # mostramos los cambios en la pantalla
        
        
    pygame.quit()
main()
