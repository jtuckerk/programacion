
import pygame
from constansts import WIDTH, HEIGHT
from Board import Board

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def main():
    
    run = True
    clock = pygame.time.Clock()
    board = Board(WIN)
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                 pass
        
        board.draw_squares()
        board.create_board()
        pygame.display.update()
        
    pygame.quit()
main()
