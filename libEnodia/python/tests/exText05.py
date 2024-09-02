#copilot: generate code for pygame zero to draw a text string with the word "hello" into each of three windows created with pygame._sdl2

import pgzrun
import pygame

#from pygame._sdl2 import Window, Renderer

from pygame._sdl2.video import Window, Renderer, Texture

# Initialize Pygame
pygame.init()

# Set up fonts
font = pygame.font.Font(None, 74)

# Function to draw text in a window
def create_text_surface(text):
  surface = pygame.Surface((300, 300))
  surface.fill((0, 0, 0))  # Fill the window with black
  text_surface = font.render(text, True, (255, 255, 255))
  return text_surface

dest = pygame.Rect((0, 0), (300, 300))

def drawRendererS(r, s):
  #renderer.draw(surface, (0,0))
  #renderer.blit(surface, (0,0))
  #r.draw(s, dest)

  r.blit(s, dest)

def draw():
  for i in range(3):
    r = renDict[i]
    t = tDict[i]
    r.clear()
    #drawRendererS(r, t)
    r.present()

  screen.clear()

# Create three windows
winDict, renDict, tDict = {}, {}, {}

ts = create_text_surface("hello")

for i in range(3): 
  winName = "win" + str(i)
  winDict[i] = Window(winName, size=(300, 300))
  renDict[i] = Renderer(winDict[i])
  tDict[i]   = Texture.from_surface(renDict[i], ts)

# Run Pygame Zero
pgzrun.go()

### end ###
