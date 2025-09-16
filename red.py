import random

FONT_COLOUR = (255, 255, 255)
WIDTH = 800
HEIGHT = 800
CENTRE_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTRE = (CENTRE_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
COLOURS = ["green", "blue"]

game_over = False
game_complete = False
current_level = 1
stars =[]
animations = []

def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0, 0))
    if geme_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "well done.")
    else:
        for star in stars:
            star.draw()
