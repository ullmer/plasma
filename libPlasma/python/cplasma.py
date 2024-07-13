# Cython bindings around libPlasma/c
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-13

#cplasma-cython.h

class CPlasma:
  poolSpecifier = None

  ############# error reporting #############

  def err(self, msg): print("CPlasma error:", msg)

  ############# constructor #############

  def __init__(self, **kwargs):
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    if poolSpecifier is None: err("constructor: poolSpecifier not provided"); return -1
     
    self.initPlasma(self.poolSpecifier)
  
  ############# initiate C Plasma #############

  def initPlasma(self, poolSpecifier=None): pass

  ############# initiate C Plasma #############

  def deposit(self, descrips=None, ingests=None): pass

################################
############# main #############

if __name__ == "__main__":
  p = CPlasma("tcp://localhost/hello")
  p.deposit("hello", "name:world")

### end ###
