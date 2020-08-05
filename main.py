import os
import pygame
pygame.init()

screen = pygame.display.set_mode([700, 700])
pygame.display.set_caption("My Game")

BACKGROUND = pygame.image.load(os.path.join("assets", "solid_black.png"))


def main():
    running = True
    refresh_rate = 60
    clock = pygame.time.Clock()

    def redraw():
        screen.blit(BACKGROUND, (0,0))
        pygame.display.update()

    while running:
        clock.tick(refresh_rate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

    

    pygame.quit()


main()
