# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

WIDTH, HEIGHT = 800, 800

from enoActorScaled import *

######## animist canvas ######## 

class AnimCanvas:
  imgSqFn, imgArtistFn = 'sspirito01h', 'pollaiolo01'
  imgSpaceFn           = 'sspirito_extrap_cp1'
  actorSq, actorArtist, actorSpace = [None]*3

  ########### constructor ########### 
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prepActors()

  ########### prepare actors ########### 
  def prepActors(self):
    self.actorSq     = enoActorScaled(self.imgSqFn,     scale=.2)
    self.actorArtist = enoActorScaled(self.imgArtistFn, scale=.5)
    self.actorSpace  = enoActorScaled(self.imgSpaceFn, scale=.75, pos=(530,525))
    self.actorSpace.alpha = 80

  ########### draw ########### 
  def draw(self): 
    self.actorSpace.draw(screen)
    #self.actorSq.draw(screen)

########### main ########### 

ac = AnimCanvas()

def draw(): screen.clear(); ac.draw()

### end ###
