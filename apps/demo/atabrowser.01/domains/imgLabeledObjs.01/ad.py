# Animist Tangible Allomorphs Domain
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import traceback

########## animist tangible allomorphs domain ##########

class AtaDomain:
  def msg(self, mstr: str): 
    mstr2 = self.getClassName() + ' msg: ' + mstr; print(mstr2)

  def err(self, estr: str):
    estr2 = self.getClassName() + ' err: ' + estr; print(estr2)
    traceback.print_exc(); 

  def getClassName(self): return self.__class__.__name__

########## main ##########
if __name__ == "__main__":
  ad = AtaDomain()
  ad.msg("hello world")

### end ###
