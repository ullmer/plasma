# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

WIDTH, HEIGHT = 800, 800

from enoActorScaled import *
from enoAniMenu     import *

######## animist canvas ######## 

class AnimCanvas:
  imgSqFn, imgArtistFn = 'sspirito01h', 'pollaiolo01'
  imgSpaceFn, imgTBox  = 'sspirito_extrap_cp1', 'transp_box01b'

  actorSq, actorArtist, actorSpace, actorBox = [None]*4
  boxSelected = False

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prepActors()

  ########### prepare actors ########### 

  def prepActors(self):
    self.actorBox    = Actor(self.imgTBox,               pos=( 500, 500))
    self.actorSq     = enoActorScaled(self.imgSqFn,      pos=(1000, 500), 
                                                   scale=.2, alpha = 220)

    self.actorSpace  = enoActorScaled(self.imgSpaceFn,   pos=(530,525), 
                                                   scale=.75, alpha = 40)

    #self.actorArtist = enoActorScaled(self.imgArtistFn, pos=(1080, 1250), 
    #                                              scale=.22, alpha = 95)

  ########### draw ########### 

  def draw(self, screen): 
    self.actorSpace.draw(screen)
    self.actorBox.draw()
  
  ########### on mouse down ########### 

  def on_mouse_down(self, pos):
    if self.actorBox.collidepoint(pos): 
      self.boxSelected = True
      print("box selected"); return

  ################## on_mouse_move ##################

  def on_mouse_move(self, rel, buttons):
    if self.boxSelected:
      x1, y1 = self.actorBox.pos
      dx, dy = rel
      x2, y2 = x1+dx, y1+dy
      self.actorBox.pos = (x2, y2)

  ################## on_mouse_up ##################

  def on_mouse_up(self): self.boxSelected = False

########### main ########### 

ac  = AnimCanvas()
eam = enoAniMenu()

def draw(): 
  screen.clear(); 
  for el in [ac, eam]: el.draw(screen)

def on_mouse_down(pos): 
    for el in [ac, eam]: el.on_mouse_down(pos)

def on_mouse_move(rel, buttons): 
    for el in [ac, eam]: el.on_mouse_move(rel, buttons)

def on_mouse_up():               
    for el in [ac, eam]: el.on_mouse_up()

### end ###
