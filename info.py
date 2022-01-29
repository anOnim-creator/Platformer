"""
Info File.
Open info screen
"""
import pygame
import sys
from main import COLORS, CAPTIONS, IMAGES, SIZES, FPS


def main():
    """
    Main method.
    View info screen
    """
    pygame.init()
    pygame.display.set_caption(CAPTIONS["Info"])
    pygame.display.set_icon(IMAGES["Icon"])
    screen = pygame.display.set_mode(SIZES["Screen"])

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(COLORS["Background"])
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
