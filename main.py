import os
import pygame
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

    def redraw():
        SCREEN.blit(BACKGROUND, (0,0))
        SCREEN.blit(SNAKE, (100,100))
        pygame.display.update()
       

    while running:
        clock.tick(refresh_rate)
        redraw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       

    

    pygame.quit()


main()
