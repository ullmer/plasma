#copilot: generate code for pygame zero to draw a text string with the word "hello" into each of three windows created with pygame._sdl2

import pgzrun
import pygame
import pgzero.ptext

#from pygame._sdl2 import Window, Renderer

from pygame._sdl2.video import Window, Renderer, Texture

# Initialize Pygame
pygame.init()

# Set up fonts
font = pygame.font.Font(None, 74)

winDim=(100,100)

# Function to draw text in a window
def create_text_surface(text):
  tsurf = pygame.Surface(winDim)
  tsurf.fill((0, 0, 0))  # Fill the window with black
  pgzero.ptext.draw("hallo", surf=tsurf, topleft=(0,0), fontsize=40, alpha=.5, color=(255,255,255))
  return tsurf

dest = None

def drawRendererS(r, t):
  global dest
  if dest is None: w,h = t.width, t.height; dest = pygame.Rect((0,0), (w,h))
  r.blit(t, dest) #r.draw(t, dest) # not in common pip-distributed distro as of 2024-09

firstFrame = True

def draw():
  global firstFrame
  if firstFrame: firstFrameActions(); firstFrame = False

  for i in range(3):
    r,t = renDict[i], tDict[i]
    r.clear()
    drawRendererS(r, t)
    r.present()

# Create three windows
winDict, renDict, tDict = {}, {}, {}

ts = create_text_surface("hello")

def firstFrameActions():

  for i in range(3): 
    winName = "win" + str(i)
    winDict[i] = Window(winName, size=winDim)
    renDict[i] = Renderer(winDict[i])
    tDict[i]   = Texture.from_surface(renDict[i], ts)

# Run Pygame Zero
pgzrun.go()

### end ###
