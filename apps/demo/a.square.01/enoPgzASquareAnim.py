# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

import pygame, traceback
from enoPgzASquare   import *
from pgzero.builtins import Actor, animate, keyboard, keys

######## enodia pygame zero animist square ######## 

class enoPgzASquareAnim(enoPgzASquare):
  imgSqFn = 'sspirito01h'
  actorSq = None

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()

  def msg(self, msgstr): print("enoPgzASquareAnim message: " + str(msgstr))
  def err(self, msgstr): print("enoPgzASquareAnim error: "   + str(msgstr)); traceback.print_exc()
        
  ########### prepare actors ########### 

  def prepActors(self):
    super().prepActors()
    self.actorSq     = enoActorScaled(self.imgSqFn,      pos=(1000, 500), 
                                                   scale=.2, alpha = 220)

### end ###
  
