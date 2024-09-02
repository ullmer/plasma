#copilot: generate code for pygame zero to draw a text string with the word "hello" into each of three windows created with pygame._sdl2

import pgzrun
import pygame
from pygame._sdl2 import Window

# Initialize Pygame
pygame.init()

# Create three windows
window1 = Window("Window 1", size=(400, 300))
window2 = Window("Window 2", size=(400, 300))
window3 = Window("Window 3", size=(400, 300))

# Set up fonts
font = pygame.font.Font(None, 74)

# Function to draw text in a window
def draw_text(window, text):
    surface = window.get_surface()
    surface.fill((0, 0, 0))  # Fill the window with black
    text_surface = font.render(text, True, (255, 255, 255))
    surface.blit(text_surface, (50, 100))  # Draw the text
    window.refresh()

# Draw "hello" in each window
draw_text(window1, "hello")
draw_text(window2, "hello")
draw_text(window3, "hello")

# Pygame Zero draw function (not used in this example)
def draw():
    pass

# Pygame Zero update function (not used in this example)
def update():
    pass

# Run Pygame Zero
pgzrun.go()

### end ###
