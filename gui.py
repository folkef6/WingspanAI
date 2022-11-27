import pygame
import os

def get_bird_image(bird_name):
    bird_name = bird_name.replace("’","_")
    return pygame.image.load(f"media\\Birds\\{bird_name}.png").convert()

pygame.init()
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60 

pygame.display.set_caption("WingspanAI")
background_image = pygame.image.load("media\\bg.png").convert()
WIN.blit(background_image , (0,0))
WIN.blit(get_bird_image("Swainson’s Hawk"), (0,0))
pygame.display.flip()

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
pygame.quit()


