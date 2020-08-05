import os
import pygame
from random import randint
pygame.init()

WIDTH = 700
HEIGHT = 700
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("My Game")

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "texture.png")), (WIDTH, HEIGHT))

SNAKE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "solid_black.png")), (10, 10))

def main():
    running = True
    refresh_rate = 60
    clock = pygame.time.Clock()
    snake_x = randint(10, 600)
    snake_y = randint(10, 600)

    def redraw():
        SCREEN.blit(BACKGROUND, (0,0))
        SCREEN.blit(SNAKE, (snake_x,snake_y))
        pygame.display.update()
       

    while running:
        clock.tick(refresh_rate)
        redraw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       

    

    pygame.quit()


main()
