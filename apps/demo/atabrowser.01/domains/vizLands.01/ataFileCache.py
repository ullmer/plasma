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

import os
import ataBase

class AtaFileCache(AtaBase):
  cachePath1 = None
  cachePath2 = None

  useSymlinks = True
  useNumerics = True
  currentNumIdx = 0
  numIdxDigits  = 4
  cacheDict     = None

  ################# constructor #################

  def __init__(): 
    try: 
      super().__init__()
      self.cacheDict = {}
    except: self.err("constructor")

  ################# constructor #################

  def mapPaths(path1: str):
    try:    
      if self.cacheDict is None: 
        self.msg("mapPaths curiosity: cache dictionary is empty"); return None

      if path1 in self.cacheDict: return self.cacheDict(path1)

      cp2 = self.cachePath2
      if os.path.isdir(cp2) is False:
        self.msg("mapPaths: target cache path does not appear to be a directory")
        return None

      if os.assess(cp2, os.W_OK) is False:
        self.msg("mapPaths: target cache path directory appears to exist, but not be writable")
        return None


    except: self.err("mapIdxToPaddedNumStr")

  ################# constructor #################

  def mapIdxToPaddedNumStr(idx: int):
    try:    return str(idx).zfill(self.numIdxDigits)
    except: self.err("mapIdxToPaddedNumStr")

### end ### 

