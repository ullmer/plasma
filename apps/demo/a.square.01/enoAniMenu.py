### First steps toward Animist menu ###
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

class enoAniMenu:

  pathPrefix = 'animist_menu'
  imgAn, imgAp, imgOp = 'animist01a_100', 'app01a_100',   'op01a_100'
  imgDa, imgPr, imgTe = 'data01a_100',    'props01a_100', 'team01a_100'
  imgHe               = 'help01a_100'

  menuImgs    = [imgAn, imgAp, imgOp, imgDa, imgPr, imgTe, imgHe]
  menuHandles = ['an', 'ap', 'op', 'da', 'pr', 'te', 'he']
  actorDict   = None

  x0, y0      = 50, 50
  dx, dy      = 0,  75

  placeFns    = ['map45Ber01a_100', 'mapBer01a_100', 'mapBos01a_100',
                 'mapCeu01a_100',   'mapDca01a_100', 'mapLax01a_100', 
                 'mapMit01a_100',   'mapTyo01a_100']

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prepActors()

  ########### prepare actors ########### 

  def prepActors(self):
    self.actorDict = {}
    x, y = self.x0, self.y0

    for imgFn, actorHandle in zip(self.menuImgs, self.menuHandles):
      imgPath = '%s/%s' % (self.pathPrefix, imgFn)
      a = Actor(imgPath, pos=(x,y))
      self.actorDict[actorHandle] = a
      x += dx; y += dy

  ########### draw ########### 

  def draw(self, screen):
    if self.actorDict is None: self.msg("draw called but uninitiated"); return
    for el in self.menuHandles:
      a = self.actorDict[el]
      a.draw()

### end ###
