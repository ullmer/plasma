# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

WIDTH, HEIGHT = 800, 800

from enoActorScaled import *
from enoAniMenu     import *

######## animist canvas ######## 

class AnimCanvas:
  imgSqFn, imgArtistFn = 'sspirito01h', 'pollaiolo01'
  imgSpaceFn, imgTBox  = 'sspirito_extrap_cp1', 'transp_box01'
  actorSq, actorArtist, actorSpace, actorBox = [None]*4

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prepActors()

  ########### prepare actors ########### 

  def prepActors(self):
    self.actorBox    = Actor(self.imgTBox,               pos=( 500, 500)
    self.actorSq     = enoActorScaled(self.imgSqFn,      pos=(1000, 500),  
                                                   scale=.2, alpha = 220)

    self.actorSpace  = enoActorScaled(self.imgSpaceFn,   pos=(530,525),    
                                                   scale=.75, alpha = 40)

    #self.actorArtist = enoActorScaled(self.imgArtistFn, pos=(1080, 1250), 
    #                                               scale=.22, alpha = 95)

  ########### draw ########### 

  def draw(self, screen): 
    for a in [self.actorSpace, self.actorSq]:
      a.draw(screen)
  
  ########### on mouse down ########### 

  def on_mouse_down(self, pos):  pass

########### main ########### 

ac  = AnimCanvas()
eam = enoAniMenu()

def draw(): 
  screen.clear(); 
  for el in [ac, eam]: el.draw(screen)

def on_mouse_down(pos): 
  for el in [ac, eam]: el.on_mouse_down(pos)

### end ###
