"""
Start File.
Open start screen
"""
import pygame
import sys

import game
import info
from tools import Custom_Group
from button import Button
from main import COLORS, CAPTIONS, IMAGES, SIZES, FPS

PLAY_BUTTON_TEXT = 'Play'
PLAY_BUTTON_CORDS = (SIZES["Screen"][0] // 10, SIZES["Screen"][1] // 10)

INFO_BUTTON_TEXT = "Info"
INFO_BUTTON_CORDS = (SIZES["Screen"][0] // 10, SIZES["Screen"][1] // 10 * 2)

FONT_SIZE = 70
running = True
game_screen_open = False


def main():
    """
    Main method.
    View start screen
    """
    global running, game_screen_open

    pygame.init()
    pygame.display.set_caption(CAPTIONS["Start"])
    pygame.display.set_icon(IMAGES["Icon"])
    screen = pygame.display.set_mode(SIZES["Screen"])

    buttons = Custom_Group()
    buttons.add(Button(PLAY_BUTTON_TEXT, COLORS["Stair"], game.main, FONT_SIZE, PLAY_BUTTON_CORDS))
    buttons.add(Button(INFO_BUTTON_TEXT, COLORS["Stair"], info.main, FONT_SIZE // 2, INFO_BUTTON_CORDS))

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons.handle_event(event)
        else:
            if not running or game_screen_open:
                break
        screen.fill(COLORS["Background"])
        buttons.draw(screen)
        buttons.update()
        pygame.display.flip()
        clock.tick(FPS)
    if not game_screen_open:
        pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
