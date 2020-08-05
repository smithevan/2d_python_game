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

'''class Snake(self, x, y):
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y '''
   


def main():
    running = True
    refresh_rate = 60
    clock = pygame.time.Clock()
    snake_x = randint(100, 600)
    snake_y = randint(100, 600)

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
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake_x -= 2
        if keys[pygame.K_RIGHT]:
            snake_x += 2
        if keys[pygame.K_UP]:
            snake_y -= 2
        if keys[pygame.K_DOWN]:
            snake_y += 2

       

    

    pygame.quit()


main()
