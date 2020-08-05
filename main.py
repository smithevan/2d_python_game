import os
import pygame
pygame.init()

WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("My Game")

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "texture.png")), (WIDTH, HEIGHT))

SNAKE = pygame.draw.rect(screen, (22, 55, 53), (10, 10, 3, 4), 10)

def main():
    running = True
    refresh_rate = 60
    clock = pygame.time.Clock()

    def redraw():
        screen.blit(BACKGROUND, (0,0))
        pygame.display.update()

    while running:
        clock.tick(refresh_rate)
        redraw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

    

    pygame.quit()


main()
