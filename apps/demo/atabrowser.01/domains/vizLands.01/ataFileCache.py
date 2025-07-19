# ata.browser file caching logic
# Brygg Ullmer, Clemson University
# Begun 2025-07-18

# Initial context: first use is in a web caching context, with rendering via pygame zero.
# The caching may retrieved on demand from the web, or from local proxy stores.
# Pygame Zero requires lower-case filenames, to preserve compatibility with case-insensitive
# filesystems.  Initially implementing this via symbolic links with local proxy caches.
# Note that according to CoPilot, symlink creation on Windows 10 (and perhaps higher) requires
# Developer Mode to be activated to avoid requiring administrative permissions.  Copilot
# describes this process as: 
#   Open Settings:
# Press Windows + I to open the Settings app.
# Navigate to Developer Settings:
# Go to Update & Security → For Developers.
# Enable Developer Mode:
# Select the Developer mode radio button.
# You may be prompted to confirm and install additional components. 
# Accept and wait for the installation to complete.
# Restart (if prompted):
# A restart may be required, though often it's not.

# All of this is non-ideal, but -- especially for potentially large caches on legacy machines
# with tightly limited storage, and toward initial demonstration, it's hopefully a pragmatic
# compromise, with some abstraction to support for extension.

import os, yaml, shutil
import ataBase

class AtaFileCache(AtaBase):
  cachePath1 = None
  cachePath2 = None

  useSymlinks = True
  useNumerics = True

  currentCacheIdx = 0
  numIdxDigits    = 4
  cacheDict       = None

  yamlMapPrimaryFn = 'cacheMap.yaml'
  yamlMapPrimaryF  = None            #holds file handle, while file is open
  yamlMapBkupFn    = 'cacheMapBk.yaml'

  autoloadCacheMap           = True
  cacheMapUpdatedThisSession = False
  backupYamlLogOnEachStart   = True
  logMapToYaml               = True
  flushYamlMapAfterEachEntry = True
  closeYamlFAfterEachEntry   = False

  ################# constructor #################

  def __init__(self): 
    try: 
      super().__init__()
      self.cacheDict = {}

      if self.autoloadCacheMap: self.loadCacheMap()
    except: self.err("constructor")

  ################# loadCacheMap #################

  def loadCacheMap(self):
    try:
      if os.path.exists(self.yamlMapPrimaryFn) is False:
        self.msg('loadCacheMap: pre-existing yaml cache map not found. This will be created")
        return False # no cache map loaded, but not necessarily a problem

      f  = open(self.yamlMapPrimaryFn, 'rt')
      yd = yaml.safe_load(f)
      f.close()

      if isInstance(yd, dict): self.cacheDict = yd; return True #successful

      self.msg("loadCacheMap: curious: yaml cache map loaded, but not a dictionary as anticipated")
      return False
    except: self.err("loadCacheMap"); return False
      
  ################# replicate Yaml Cache to Bkup #################

  def replicateYamlCacheToBkup(self):
    try:
      if not os.path.exists(self.yamlMapPrimaryFn):
        self.msg("replicateYamlCacheToBkup called, but existing yaml cache map not found")
        return False

      try:    shutil.copy(self.yamlMapPrimaryFn, self.yamlMapBkupFn)
      except: self.err("replicateYamlCacheToBkup copy error:"); return False

      return True
    except: self.err("replicateYamlCacheToBkup"); return False 

  ################# logCacheMapEntryToYaml #################

  def logCacheMapEntryToYaml(self, srcFn: str, targFn: str):
    try:
      if self.backupYamlLogOnEachStart and 
         not self.cacheMapUpdatedThisSession:

        self.replicateYamlCacheToBkup()
        self.cacheMapUpdatedThisSession = True
    except: self.err("logCacheMapEntryToYaml")

  ################# map cache paths #################

  def mapPaths(self, srcFn: str): # name could benefit from reconsideration
    try:    
      if self.cacheDict is None: 
        self.msg("mapPaths curiosity: cache dictionary is empty"); return None

      if srcFn in self.cacheDict: return self.cacheDict(srcFn)

      cp = self.cachePath(srcFn)
      self.cacheDict[srcFn] = cp
      return cp

    except: self.err("mapIdxToPaddedNumStr")

  ################# increment cache index #################
  
  def confirmCachePathWritableDir(self):
    try:
      cp2 = self.cachePath2
      if os.path.isdir(cp2) is False:
        self.msg("mapPaths: target cache path does not appear to be a directory")
        return False

      if os.assess(cp2, os.W_OK) is False:
        self.msg("mapPaths: target cache path directory appears to exist, but not be writable")
        return False

      return True
    except: self.err("confirmCachePathWritableDir")

  ################# increment cache index #################

  def incrCacheIdx(self):
    try:    self.currentCacheIdx += 1; return self.currentCacheIdx
    except: self.err("incrCacheIdx")

  ################# map index to padded numeric string #################

  def mapIdxToPaddedNumStr(self, idx: int):
    try:    return str(idx).zfill(self.numIdxDigits)
    except: self.err("mapIdxToPaddedNumStr")

  ################# getNextCachePath #################

  def getNextCachePath(self):
    try:
      if self.cachePath2 is None:
        self.msg("getNextCachePath: problem with cache path"

      idx = self.incrCacheIdx()
      pns = self.mapIdxToPaddedNumStr(idx)

      cpwd = self.confirmCachePathWritableDir()
      if cpwd is False: 
        self.msg("getNextCachePath: punting due to cache path directory issue");
        return None

      result = os.path.join(self.cachePath2, pns) 
      return result
    except: self.err("getNextCachePath")

  ################# getNextCachePath #################
  # takes a fn1 -- initially relative to a path expressed by cachePath1 
  # first tests if this exists (initially limited to pre-cached variants in local filespace)
  # then, attempt creation of an (initially numeric, symlinked) ~proxy if allowed.
  # initially, if any of this is not so, punt, hopefully with appropriate reporting

  def cachePath(self, fn: str):
    try:
      if self.useSymlinks is not True:
        self.msg("cachePaths: use symlinks is not set; this case is not yet supported"); return False

      if self.useNumerics is not True:
        self.msg("cachePaths: use numerics is not set; this case is not yet supported"); return False

      if self.cachePath1 is None:
        self.msg("cachePaths: source cache path is unset"); return

      src = os.join(self.cachePath1, fn)
      pe  = os.path.exists(src)
      if pe is False: self.msg("cachePaths: source path doesn't exist: " + str(pe)); return False
  
      dest = self.getNextCachePath()

      try:    os.symlink(src, dest)
      except: self.err("cachePaths: symlinking paths attempted, but failed")

      return dest #successful symlinked cache
      
    except: self.err("cachePaths")

### end ### 

