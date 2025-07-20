### Manage an array of labeled tranlucent blocks
# Brygg Ullmer, Clemson University

import pygame
from ataBase import *

################ ata label block ################

class AtaLabelBlock(AtBase):

  rectSurfaceCache  = None
  placedSurfaceDict = None

  defaultColor = (70, 70, 100)
  defaultAlpha = 128

  ################ constructor ################

  def __init__(self):
    super().__init__()
    self.rectSurfaceCache  = {}
    self.placedSurfaceDict = {}
  
  ################ createTranslSurface ################

  def createTranslSurface(self, handle: str, w: int, h: int, rcolor=None, ralpha=None):

    try:
      if rcolor is None: rcolor = self.defaultColor
      if ralpha is None: ralpha = self.defaultAlpha

      rect_surface = pygame.Surface((w, h), pygame.SRCALPHA)
      r, g, b = rcolor
      rect_surface.fill ((r,g,b,ralpha))
      self.rectSurfaceCache[handle] = rect_surface

    except: self.err("createTranslSurface")

  ################ createTranslSurface ################

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # Clear screen with dark background
    screen.blit(rect_surface, (100, 100))  # Draw translucent rectangle
    pygame.display.flip()

pygame.quit()

### end ###

