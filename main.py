import pygame
# import os
#import time

# import random

pygame.init()

screen = pygame.display.set_mode([700, 700])
pygame.display.set_caption("Name")


def main():
    running = True
    refresh_rate = 60
    clock = pygame.time.Clock()

    while running:
        clock.tick(refresh_rate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

    pygame.quit()


main()
