# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

WIDTH, HEIGHT = 800, 800
TITLE         = 'animist square'

from enoActorScaled import *
from enoAniMenu     import *
from enoPgzASquare  import *
   
#### reassigning app icon must happen early 
#iconFn       = 'images/sspirito01h.png' # rework to 32x32, see if that makes a difference
#icon_surface = pygame.image.load(iconFn)
#pygame.display.set_icon(icon_surface)

######## animist canvas ######## 

class AnimCanvas:

  imgArtistFn, imgSpaceFn = 'pollaiolo01', 'sspirito_extrap_cp1', 
  actorArtist, actorSpace = None, None
  epas                    = None

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prepActors()
    self.epas = enoPgzASquare(windowDim=(WIDTH, HEIGHT))

  ########### prepare actors ########### 

  def prepActors(self):
    self.actorSpace  = enoActorScaled(self.imgSpaceFn,   pos=(530,525), 
                                                   scale=.75, alpha = 40)

    #self.actorArtist = enoActorScaled(self.imgArtistFn, pos=(1080, 1250), 
    #                                              scale=.22, alpha = 95)

  ########### draw ########### 

  def draw(self, screen): 
    self.actorSpace.draw(screen)
    self.epas.draw(screen)
  
  ########### on mouse down, move, up ########### 

  def on_mouse_down(self, pos):          self.epas.on_mouse_down(pos)
  def on_mouse_move(self, rel, buttons): self.epas.on_mouse_move(rel, buttons)
  def on_mouse_up(self):                 self.epas.on_mouse_up()

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
