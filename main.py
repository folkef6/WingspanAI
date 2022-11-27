from game import Game
import pygame
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

import pygame
def main():
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.quit()
    
    
    #game = Game(players=2)
    #game.game()
    return


if __name__ == "__main__":
    main()
