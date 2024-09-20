import sys; sys.path.append("/home/bullmer/git/plasma/libPlasma/python/")
import p4jPlasma as pj4p

p4jp.init("tcp://localhost/hello")
p4jp.pDeposit_StrStr("hello", "name:world")

### end ###

