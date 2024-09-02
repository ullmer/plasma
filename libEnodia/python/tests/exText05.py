#copilot: generate code for pygame zero to draw a text string with the word "hello" into each of three windows created with pygame._sdl2

import pgzrun
import pygame
from pygame._sdl2 import Window, Renderer

# Initialize Pygame
pygame.init()

# Create three windows
winDict, renDict = {}, {}

for i in range(3): 
  winDict[i] = Window("Window " + str(i), size=(300, 300))
  renDict[i] = Renderer(winDict[i])

# Set up fonts
font = pygame.font.Font(None, 74)

# Function to draw text in a window
def create_text_surface(text):
  surface = pygame.Surface(size=(400, 300))
  surface.fill((0, 0, 0))  # Fill the window with black
  text_surface = font.render(text, True, (255, 255, 255))
  return text_surface

def draw_renderer_surface(renderer, surface):
  renderer.draw(surface, (0,0))

# Draw "hello" in each window
#draw_text(window1, "hello")
#draw_text(window2, "hello")
#draw_text(window3, "hello")

ts = create_text_surface("hello")

def draw():
  for i in range(3):
    r = renDict[i]
    draw_renderer_surface(r, ts)

# Run Pygame Zero
pgzrun.go()

### end ###
