# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

from enoActorScaled import *

######## animist canvas ######## 

class enoPgzASquare:
  imgSqFn, imgTBox  = 'sspirito01h', 'transp_box01b'
  actorSq, actorBox = None, None
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

  ########### draw ########### 

  def draw(self, screen): 
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

### end ###
