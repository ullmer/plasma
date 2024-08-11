# Enodia Button-like elements -- sometimes backed by Pygame Zero, 
#  sometimes by physical buttons, sometimes by other variants.
# First approximation, albeit too specific to Pygame Zero
# Brygg Ullmer, Clemson University
# Begun    2022-02-22
# Revamped 2024-08

# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from pygame import Rect

##################### pygamezero button #####################

class enoButton:
  basePos    = (0,0)
  buttonDim  = (100, 30)
  buttonRect = None
  buttonText = ""
  actor      = None
  imageFn     = "" #image filename, relative to PGZ's "images/" directory expectations; lower-case only
  selectImgFn = "" #   selected image filename
  deactImgFn  = "" #deactivated image filename
  bgcolor1   = (0, 0, 130)
  bgcolor2   = (50, 50, 250)
  fgcolor    = "#bbbbbb"
  alpha      = .8
  fontSize   = 36
  angle      = 0

  drawText   = True
  drawImg    = False
  drawAdapt  = True   # if True, will render text and/or image only when specified

  toggleMode  = True
  toggleState = False

  ############# constructor #############

  def __init__(self, buttonText, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.buttonText = buttonText
    self.buttonRect = Rect(self.basePos, self.buttonDim)
    if self.imageFn is not None:
      self.actor     = Actor(self.imageFn)
      self.actor.pos = self.basePos

  ############# pgzero draw #############

  def draw(self, screen):
    if self.toggleMode and self.toggleState: bgcolor = self.bgcolor2
    else:                                    bgcolor = self.bgcolor1

    screen.draw.filled_rect(self.buttonRect, bgcolor)
    #screen.draw.text(self.buttonText, self.basePos, align="center",
    x0, y0 = self.basePos; dx, dy = self.buttonDim; cx=x0+dx/2; cy = y0+dy/2

    if (self.drawText or self.drawAdapt) and len(self.buttonText)>0:
      screen.draw.text(self.buttonText, centerx=cx, centery=cy, align="center",
                       fontsize=self.fontSize, color=self.fgcolor, 
                       alpha=self.alpha, angle=self.angle)

    if (self.drawImg or self.drawAdapt) and len(self.imgFn)>0:
      if self.actor is not None:
        self.actor.draw()
      else:
        if self.imageFn is not None and len(self.imageFn) > 0:
          self.actor     = Actor(self.imageFn)
          self.actor.pos = self.basePos
          self.actor.draw()

  ############# nudge #############

  def nudgeY(self, dy): 
    bpx, bpy = self.basePos
    self.basePos = (bpx, bpy+dy)
    self.buttonRect = Rect(self.basePos, self.buttonDim)

  def nudgeXY(self, dx, dy): 
    bpx, bpy = self.basePos
    self.basePos = (bpx+dx, bpy+dy)
    self.buttonRect = Rect(self.basePos, self.buttonDim)

  ######################### on_mouse_down #########################

  def toggle(self):
    if self.toggleState: self.toggleState = False
    else:                self.toggleState = True

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    if self.buttonRect.collidepoint(pos): 
      print(self.buttonText, "pressed")
      self.toggle()
      return True

    return False

##################### pygamezero button #####################

class enoButtonArray:
  basePos    = (0,0)
  buttonDim  = (100, 30)
  dx, dy     = 190, 0

  textArray    = None
  buttonArray  = []
  lastSelected = None
  angle      = 0

  ############# constructor #############

  def __init__(self, buttonTextList, **kwargs): 
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.textArray  = buttonTextList
    self.buttonArray = []

    idx = 0

    bpx, bpy = self.basePos
    for text in self.textArray:
      but = enoButton(text, basePos = (bpx+idx*self.dx, bpy+idx*self.dy),
                      buttonDim = self.buttonDim, angle=self.angle)
      self.buttonArray.append(but); idx += 1

  ############# pgzero draw #############

  def draw(self, screen): 
    for but in self.buttonArray: but.draw(screen)

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    for but in self.buttonArray:
      if but.on_mouse_down(pos):
        if self.lastSelected is not None: self.lastSelected.toggle()
        self.lastSelected = but

### end ###
