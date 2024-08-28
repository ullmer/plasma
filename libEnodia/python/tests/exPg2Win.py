#copilot output from query "code for creating new windows in pygame-ce using sdl2"

import pygame
from pygame._sdl2 import Window, Renderer

# Initialize pygame
pygame.init()

# Create the first window
window1 = Window("First Window", size=(640, 480))
renderer1 = Renderer(window1)

# Create the second window
window2 = Window("Second Window", size=(640, 480))
renderer2 = Renderer(window2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    renderer1.clear()
    renderer2.clear()

    # Present the screen
    renderer1.present()
    renderer2.present()

# Quit pygame
pygame.quit()
