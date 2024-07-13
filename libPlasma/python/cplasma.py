# Cython bindings around libPlasma/c
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-13

#cplasma-cython.h

class CPlasma:

  ############# constructor #############

  def __init__(self, **kwargs):
     #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
     self.__dict__.update(kwargs) #allow class fields to be passed in constructor

### end ###
