# Plasma Protein Schemas (mapping of protocols, initially oriented
#  toward sensors and multitouch, but also with an eye toward
#  other hardware and software services)
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-20

import sys; sys.path.append("/home/bullmer/git/plasma/libPlasma/python/")
from proteinSchemas import *

ps = proteinSchemas(schemaIndexPath='/home/bullmer/git/plasma/libPlasma/yaml')
exHwSensorEls = ['C2d_generic', 'NFC_125k01', 'NFC_13m01', 'IMU_ST01']

for hwEl in exHwSensorEls: ps.registerHwSensorDepositor(hwEl)

ps.printActiveSensorFields()

### end ###

