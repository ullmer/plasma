# Early Animist Plasma YAML handler
# Brygg Ullmer, Clemson University
# Begun 2025-06-16 

# Exploring compact messaging:
#  message descriptor|descr|descrips: v2int8  (pair of bytes)
#  message arguments |args |ingests:  v2int32 (pair of 32-bit signed integers)
#                                     string  (character string)

import yaml

class enoPlasYaml:
  yamlFn = None
  yamlD  = None
  modsD, appD, opsD = [None] * 3

  ########### constructor ########### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    if self.yamlFn is not None: self.loadYaml()

  def msg(self, mstr): print("enoPlasYaml msg: " + str(mstr))
  def err(self, mstr): print("enoPlasYaml err: " + str(mstr))

  ########### constructor ########### 

  def storeYamlEl(self, fieldStr, fieldRef):
    if self.yamlD is None: self.msg("storeYamlEl: yamlD is unassigned"); return
    if fieldStr in self.yamlD:
      val = self.yamlD[fieldStr]
      fieldRef = val

  ########### constructor ########### 

  def loadYaml(self):
    if self.yamlFn is None: self.msg("loadYaml: yamlFn is unassigned"); return
    yamlF      = open(self.yamlFn, 'rt')
    self.yamlD = yaml.safe_load(yamlF)

    self.storeYamlEl('mods', self.modsD)
    self.storeYamlEl('app',  self.appD)
    self.storeYamlEl('ops',  self.opsD)


### operations ###

mods:
  get:            {descrMod: 0x0001} #add to descr[iption] ~address
  getR:           {descrMod: 0x0002}
  set:            {descrMod: 0x0003}
  setR:           {descrMod: 0x0004}

app:
  name:           {descr: 0x0110, args:, response: string}
  descr:          {descr: 0x0110, args:, response: string}
  authors:
    orgs:         {descr: 0x0120, args:, response: list of strings}
    names:        {descr: 0x0130, args:}
  listeners:      {descr: 0x0140, args:}
    devices:      {descr: 0x0140, args:}
    windows:      {descr: 0x0140, args:}

  listOps:              {descr: 0x0160, args:} #~glossary?

ops:
  create:
    square:            {descr: 0x0200, args:}
    window:            {descr: 0x0210, args:}

  move:
    square:            {descr: 0x0220, args:}
      get:             {descr: 0x0221, args:}
      getR:            {descr: 0x0222, args: v2int32} #get response
      set:             {descr: 0x0223, args: v2int32}
    window:            {descr: 0x0230, args:}
      get:             {descr: 0x0231, args:}
      getR:            {descr: 0x0231, args: v2int32}
      set:             {descr: 0x0232, args: v2int32}

  toggle:
    square:            {descr: 0x0240, args:}

plasma:
  address:        {bs: ABBB CCCC DDDD EEEE} #bs: bitstring

  sw:        ############# SOFTWARE ############ classes of services
      address:    {bs: 0BBB CCCC, bv: 0,  nm: software, prefix: SW}
      std:
        addr:     {bs: 0000 CCCC DDDD EEEE} 

        file:     
          addr:   {bs: 0000 0001 0000, bv: 0x0100}
          open:   {bs: 0000 0001 0001, bv: 0x0110}
          close:  {bs: 0000 0001 0010, bv: 0x0120}
          new:    {bs: 0000 0001 0011, bv: 0x0130}
          save:   {bs: 0000 0001 0100, bv: 0x0140}

### end ###
