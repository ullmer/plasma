# Plasma Protein Schemas (mapping of protocols, initially oriented
#  toward sensors and multitouch, but also with an eye toward
#  other hardware and software services)
# Lead by Brygg Ullmer, Clemson University
# Begun 2024-07-20

import sys; sys.path.append("/home/ullmer/git/plasma/libPlasma/python/")
import plasmaProteinSchemas

pps = plasmaProteinSchemas(schemaIndexPath='/home/bullmer/git/plasma/libPlasma/yaml')
#print(pps.hardwareYamlD)

#examples:
# C2d_generic: {bv: 0x9601, nm: multitouch, fmt: unt16x3, layout: AB CC DD, fields: [device, touch, x, y]}
# NFC_125k01: {bv: 0x9A01, nm: HiTag2,  fmt: unt16x3, layout: AA AA AA,    fields: [serial]}
# NFC_13m01:  {bv: 0x9A11, nm: NTAG213, fmt: unt16x4, layout: AA AA AA A0, fields: [serial]}
# IMU_ST01:  {bv: 0x9F01, nm: ST LSM6DS3TR_C IMU Ac Gy, fmt: unt16x2, layout: AA BB, fields: [Ac, Gy]}

exampleHWdevs = ['C2d_generic', 'NFC_125k01', 'NFC_13m01', 'IMU_ST01']
for hwEl in exampleHWdevs:
  print(hwEl)

### end ###

