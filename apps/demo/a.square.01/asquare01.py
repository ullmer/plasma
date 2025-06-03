# Example visual application toward Animist
# Brygg Ullmer, Clemson University
# Begun 2025-06-02

######## animist canvas ######## 

class AnimCanvas:
  imgSqFn, imgArtistFn = 'sspirito01h', 'pollaiolo01'
  imgSpaceFn           = 'sspirito_extrap_cp1'
  actorSq, actorArtist, actorSpace = [None]*3

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prepCats2Vals()

########### constructor ########### 

ac = AnimCanvas()

def draw(): c.draw()

### end ###
