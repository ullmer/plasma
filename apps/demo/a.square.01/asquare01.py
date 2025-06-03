# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

WIDTH, HEIGHT = 800, 800

from enoActorScaled import *
from enoAniMenu     import *

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
    self.actorSq     = enoActorScaled(self.imgSqFn,     scale=.2,
                                      pos=(1000, 500),   alpha = 220)

    #self.actorArtist = enoActorScaled(self.imgArtistFn, scale=.22, 
    #                                  pos=(1080, 1250), alpha = 95)

    self.actorSpace  = enoActorScaled(self.imgSpaceFn,  scale=.75, 
                                      pos=(530,525),    alpha = 40)

  ########### draw ########### 

  def draw(self, screen): 
    for a in [self.actorSpace, self.actorSq]:
      a.draw(screen)

########### main ########### 

ac  = AnimCanvas()
eam = enoAniMenu()

def draw(): 
  screen.clear(); 
  for el in [ac, eam]: el.draw(screen)

### end ###
