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
  basePos     = (0,0)
  postAnimPos = None
  activAnim   = None

  buttonDim  = (100, 30)
  buttonRect  = None
  buttonText  = ""
  actor       = None
  imageFn     = None #image filename, relative to PGZ's "images/" directory expectations; lower-case only
  selectImgFn = None #   selected image filename
  deactImgFn  = None #deactivated image filename
  bgcolor1    = (0, 0, 130)
  bgcolor2    = (50, 50, 250)
  fgcolor     = "#bbbbbb"
  alpha       = .8
  fontSize    = 36
  angle        = 0
  animDuration = 1.

  drawText    = True
  drawImg     = False
  drawAdapt   = True   # if True, will render text and/or image only when specified

  toggleMode  = True
  toggleState = False
  verbose     = False
  rectCenter  = None
  requestAnim = False
  motionAnimTween = None

  ############# constructor #############

  def __init__(self, buttonText, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.buttonText = buttonText

    bpx,  bpy  = self.basePos
    bdx,  bdy  = self.buttonDim
    bdx2, bdy2 = bdx/2, bdy/2

    self.rectCenter = (bpx-bdx2, bpy-bdy2)

    self.buttonRect = Rect(self.rectCenter, self.buttonDim)
    if self.imageFn is not None:
      self.actor     = Actor(self.imageFn)
      self.actor.pos = self.basePos
      if self.verbose: print("button" + self.buttonText + ": pos" + str(self.actor.pos))

    if self.requestAnim: self.launchAnim()

  ############# postAnimCb #############

  def postAnimCb(self):

    self.basePos = self.postAnimPos

    bpx,  bpy  = self.basePos
    bdx,  bdy  = self.buttonDim
    bdx2, bdy2 = bdx/2, bdy/2

    self.rectCenter = (bpx-bdx2, bpy-bdy2)
    self.buttonRect = Rect(self.rectCenter, self.buttonDim)


  ############# launchAnim #############

  def launchAnim(self):
    if self.motionAnimTween is None: err("launchAnim called, but motion animation tween is not selected"); return

    if self.verbose: print("launchAnim:" + str (self.postAnimPos))

    if self.actor is not None: 
      self.activAnim = animate(self.actor, pos=self.postAnimPos, duration=self.animDuration, tween=self.motionAnimTween,
                               on_finished=self.postAnimCb)

  ############# draw #############

  def draw(self, screen):
    if self.toggleMode and self.toggleState: bgcolor = self.bgcolor2
    else:                                    bgcolor = self.bgcolor1

    screen.draw.filled_rect(self.buttonRect, bgcolor)
    #x0, y0 = self.basePos; dx, dy = self.buttonDim; cx=x0+dx/2; cy = y0+dy/2
    x0, y0 = self.basePos; dx, dy = self.buttonDim; cx, cy = x0, y0

    if (self.drawText or (self.drawAdapt and self.imageFn is None)) and len(self.buttonText)>0:
      screen.draw.text(self.buttonText, centerx=cx, centery=cy, align="center",
                       fontsize=self.fontSize, color=self.fgcolor, 
                       alpha=self.alpha, angle=self.angle)

    if (self.drawImg or self.drawAdapt) and self.imageFn is not None and len(self.imageFn)>0:
      if self.actor is not None:
        self.actor.draw()
      #else:
      #  if self.imageFn is not None and len(self.imageFn) > 0:
      #    self.actor     = Actor(self.imageFn)
      #    self.actor.pos = self.basePos
      #    self.actor.draw()

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
    if self.buttonRect.collidepoint(pos) or \
       (self.actor is not None and self.actor.collidepoint(pos)):
      print(self.buttonText, "pressed")
      self.toggle()
      return True

    return False

##################### pygamezero button #####################

class enoButtonArray:
  basePos    = (0,0)
  buttonDim  = (100, 30)
  dx, dy     = 190, 0

  textArray       = None
  buttonArray     = None
  imageFns        = None
  lastSelected    = None
  angle           = 0
  requestAnim     = False
  motionAnimTween = None
  animDuration    = 1.

  ############# constructor #############

  def __init__(self, buttonTextList, **kwargs): 
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.textArray  = buttonTextList
    self.buttonArray = []

    idx = 0

    bpx, bpy  = self.basePos
    ifn       = None         #image filename
    postAnimP = None

    for text in self.textArray:
      if self.imageFns is not None: ifn = self.imageFns[idx]

      p1 = (bpx+idx*self.dx, bpy+idx*self.dy)

      if self.requestAnim: # make distinction between (shared) base position and post-animation pos
        baseP     = (bpx, bpy)
        postAnimP = p1
      else: baseP = p1         # no distinction

      but = enoButton(text, basePos = baseP, postAnimPos = postAnimP, 
                      buttonDim = self.buttonDim,  angle = self.angle,     imageFn = ifn,
                      drawText = self.drawText,  drawImg = self.drawImg, drawAdapt = self.drawAdapt,
                      bgcolor1 = self.bgcolor1, bgcolor2 = self.bgcolor2,  fgcolor = self.fgcolor,
                      alpha    = self.alpha,    fontSize = self.fontSize, animDuration = self.animDuration,
                      requestAnim = self.requestAnim,              motionAnimTween = self.motionAnimTween)

      self.buttonArray.append(but); idx += 1

  activAnim   = None

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
