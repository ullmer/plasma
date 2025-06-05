# Approach to allow animatable Actor scaling in Pygame Zero
# Brygg Ullmer, Clemson University
# Begun 2025-05-09

import pygame, traceback
from pgzero.actor import Actor

#WIDTH, HEIGHT = 1920, 1080

############# Actor, scaled ############# 

class enoActorScaled(Actor): #scaled actor
  scale          = 1.
  lastScaleVal   = 1.
  lastScaledSurf = None
  scaleIncrement = 1000
  alpha          = 255

  ############# constructor ############# 

  def __init__(self, image, pos=None, anchor=None, **kwargs):
    self.__dict__.update(kwargs) 
    super().__init__(image, pos, anchor)

  ############# update ############# 

  def updateScale(self): #updated scaled surface
    try:
      scaleInt     = int(self.scale * self.scaleIncrement)  #toward nuancing precision issues 
      lastScaleInt = int(self.lastScaleVal * self.scaleIncrement)

      if scaleInt == lastScaleInt: return  #nothing to do
      if self.alpha != 255:        self._orig_surf.set_alpha(self.alpha)

      w, h                = self.width * self.scale, self.height * self.scale
      self.lastScaledSurf = pygame.transform.scale(self._orig_surf, (w, h))

    except: print("ActorScaled update issue"); traceback.print_exc(); return None

  ############# draw ############# 

  def draw(self, screen): 
    if self.scale == 1.: super().draw()
    else: 
      self.updateScale()
      if self.lastScaledSurf is None:
        print("ActorScaled draw: unexpected error with last scaled surface")
      else:
        scaled_width, scaled_height = self.lastScaledSurf.get_size()
        blitX = self.pos[0] - scaled_width // 2
        blitY = self.pos[1] - scaled_height // 2
        screen.blit(self.lastScaledSurf, (blitX, blitY))
  
############# main ############# 

def grow(a1=None): animate(a1, scale=1,  duration=1.5, tween='accel_decel', 
                        on_finished=shrink)

def shrink(a1=None): animate(a1, scale=.1, duration=1.5, tween='accel_decel', 
                        on_finished=grow)

def main():
  a1 = enoActorScaled("ipan_usa_bea08c")
  a1.scale=.1
  grow(a1)

#def draw(): 
#  a1.draw()

### end ###
