# Interaction panel code
# Brygg Ullmer, Clemson University
# Begun 2024-10-09

import sys, os, yaml, traceback
from ataLabelBlock import *

############# enodia interaction panel #############

class enoIpanelLBPgz(enoIpanelYaml):

  alb = None #AtaLabelBlock 
  verbose          = False

  ############# constructor #############

  def __init__(self)
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()

  ############# get panel name #############

  def getPanelAttrib(self, attrib):
    try:
      if not self.isYamlLoaded(): 
        self.msg("getPanelName: YAML not loaded"); return None

      ipan = self.panelYd['interactionPanel']
      val  = ipan[attrib]
      return val 

    except: self.err("getPanelAttrib " + str(attrib))
  
  def getPanelName(self):     return self.getPanelAttrib('name')
  def getMatrixImageFn(self): return self.getPanelAttrib('matrixImage')

  ############# check if yaml is loaded #############

  def isYamlLoaded(self):
    if self.panelYd is not None: return True
    return False

  ############# load yaml #############

  def loadYaml(self):
    self.panels  = []

    try:
      yf         = open(self.panelFn, 'rt')
      self.panelYd = yaml.safe_load(yf)

      if 'panels' in self.panelYd:
        ypanels      = self.panelYd['panels']
        for panel in ypanels: self.panels.append(panel)
      else: self.msg('loadYaml: panels not found in ' + str(self.panelFn))
    except: self.err("loadYaml")

  ############# map char to category #############

  def mapCharToCategory(self, panelChar): 
    try:
      if self.verbose: self.msg("mapCharToCategory " + str(panelChar))
      if self.panelCharToCategory is None: self.panelCharToCategory = {}
      if self.panelCharToCatList  is None: self.panelCharToCatList  = {}
      if self.panelCharToCatLIdx  is None: self.panelCharToCatLIdx  = {}

      if panelChar in self.panelCharToCategory: 
        return self.panelCharToCategory[panelChar] #caching important to performance

      try:    cm = self.panelYd['interactionPanel']['charMap']
      except: self.err('mapCharToCategory: problem accessing charMap in YAML descriptor'); return None

      if panelChar not in cm: self.err('mapCharToCategory not finding character ' + str(panelChar)); return None

      cme = cm[panelChar]
      panel = cme[0]

      self.panelCharToCategory[panelChar] = panel
      self.panelCharToCatList[panelChar]  = cme[0:]
      self.panelCharToCatLIdx[panelChar]  = 0

      if self.verbose: self.msg("mapCharToCategory result: " + str(panel))
      return panel
    except: self.err('mapCharToCategory')

  ############# map char to category next element #############

  def mapCharToCatNextEl(self, panelChar): 
    try:
      cat = self.mapCharToCategory(panelChar)
      if panelChar not in self.panelCharToCatList or \
         panelChar not in self.panelCharToCatLIdx:
        #self.err("mapCharToCatNextEl: unexpected condition 0"); return None
        return None

      idx  = self.panelCharToCatLIdx[panelChar]
      catl = self.panelCharToCatList[panelChar]
      clen = len(catl)

      if idx >= clen: return None
        #self.err("mapCharToCatNextEl: unexpected condition 1"); return None

      result = catl[idx]
      self.panelCharToCatLIdx[panelChar] += 1
      return result

    except: self.err('mapCharToCatNextEl')

  ############# getCharMatrix #############

  def getCharMatrix(self):
    try:
      result = self.panelYd['interactionPanel']['charMatrix']
      return result
    except: self.err("getCharMatrix")

  ############# getCharMatrix #############

  def expandMatrixYaml(self):
    if self.cachedMatrix is not None: return self.cachedMatrix
    else:                             self.cachedMatrix = []
    result = []
    try:
      m     = self.getCharMatrix()
      mrows = m.splitlines()
      for row in mrows:
        lenrow = len(row.rstrip())
        outrow = []
        for i in range(lenrow):
          ch  = row[i]
          panel = self.mapCharToCatNextEl(ch)
          outrow.append(panel)
        #print(outrow)
        result.append(outrow)
      self.cachedMatrix = result
      return result
    except: self.err('expandMatrixYaml')
    return None
  
  ############# get matrix locus #############

  def getMatrixLocus(self, i, j):
    try:
      if self.cachedMatrixDict is None: self.cacheMatrixYaml()
      result = self.cachedMatrixDict[(i,j)] #dict is indexed on coord tuples
      return result
    except: self.err('getMatrixLocus ' + str(i) + " " + str(j))
    return None

  ############# cache matrix yaml #############

  def cacheMatrixYaml(self):
    try:
      self.cachedMatrixDict = {}
      my = self.expandMatrixYaml()
      i, j = 0, 0
      for row in my:
        for abbrev in row:
          coord = (i, j)
          self.cachedMatrixDict[coord] = abbrev
          i += 1
        j += 1; i = 0
    except: self.err('cacheMatrixYaml')

############# main #############

if __name__ == "__main__":
  #eip = enoIpanel(panelFn = 'cspan-panels.yaml')
  eipy = enoIpanelYaml(panelFn = 'yaml/us-bea2.yaml')
  m    = eipy.getCharMatrix()
  print(m)

  #cat1 = eip.mapCharToCategory('p')
  #cat2 = eip.mapCharToCategory('f')
  #print(cat1, cat2)

  my = eipy.expandMatrixYaml()
  print(my)
  print(eipy.cachedMatrixDict)

### end ###
