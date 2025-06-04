### First steps toward Animist menu ###
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

from pgzero.builtins import Actor, animate, keyboard, keys
import traceback

class enoAniMenu:

  pathPrefix = 'animist_menu'
  imgAn, imgAp, imgOp = 'animist01a_100', 'app01a_100',   'op01a_100'
  imgDa, imgPr, imgTe = 'data01a_100',    'props01a_100', 'team01a_100'
  imgHe               = 'help01a_100'

  menuImgs    = [imgAn, imgAp, imgOp, imgDa, imgPr, imgTe, imgHe]
  menuHandles = ['an', 'ap', 'op', 'da', 'pr', 'te', 'he']
  actorDict   = None

  x0,  y0     = 70, 70
  dx,  dy     = 0,  110 #base positioning
  hdx, hdy    = -110, 0 #hidden relative positioning

  shortestUnfoldDuration = .2  # in seconds 
  progressUnfoldMult     = 1.1

  isMenuHidden = True
  verbose      = False

  placeFns    = ['map45Ber01a_100', 'mapBer01a_100', 'mapBos01a_100',
                 'mapCeu01a_100',   'mapDca01a_100', 'mapLax01a_100', 
                 'mapMit01a_100',   'mapTyo01a_100']

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prepActors()

  def msg(self, msg): print("enoAniMenu msg: " + str(msg))
  def err(self, msg): print("enoAniMenu error: " + str(msg)); traceback.print_exc()

  ########### prepare actors ########### 

  def prepActors(self):
    self.actorDict = {}
    x, y = self.x0, self.y0

    for imgFn, actorHandle in zip(self.menuImgs, self.menuHandles):
      imgPath = '%s/%s' % (self.pathPrefix, imgFn)
      a = Actor(imgPath, pos=(x,y))
      self.actorDict[actorHandle] = a
      x += self.dx; y += self.dy
      if actorHandle == 'an' and self.isMenuHidden:
        x += self.hdx; y += self.hdy 

  ########### toggle menu display ########### 

  def toggleMenuDisplay(self):
    if self.verbose:      self.msg("toggleMenuDisplay")
    if self.isMenuHidden: self.animMenuOpen();   self.isMenuHidden = False
    else:                 self.animMenuHidden(); self.isMenuHidden = True
  
  ########### toggle menu display ########### 

  def animMenu(self, dx, dy):
    if self.verbose:           self.msg("animMenu %i %i" % (dx,dy)) 
    if self.actorDict is None: self.msg("amo called but uninitiated"); return
    x, y = self.x0, self.y0
    d    = self.shortestUnfoldDuration
    for el in self.menuHandles:
      a = self.actorDict[el]
      animate(a, pos=(x,y), duration=d)
      x += self.dx + dx; y += self.dy + dy; d *= self.progressUnfoldMult

  def animMenuOpen(self):   self.animMenu(0, 0)
  def animMenuHidden(self): self.animMenu(self.hdx, self.hdy)
  
  ########### draw ########### 

  def draw(self, screen):
    if self.actorDict is None: self.msg("draw called but uninitiated"); return
    for el in self.menuHandles:
      a = self.actorDict[el]
      a.draw()

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    if self.actorDict is None: 
      self.msg("on_mouse_down called but uninitiated"); return

    for el in self.menuHandles:
      a = self.actorDict[el]
      if a.collidepoint(pos): 
        self.msg(el + " pressed")
        if el == 'an': self.toggleMenuDisplay()

### end ###
