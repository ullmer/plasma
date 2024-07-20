import sys; sys.path.append("/home/bullmer/git/plasma/libPlasma/python/")
import cplasma

cplasma.init("tcp://localhost/hello")
cplasma.pDeposit_StrStr("hello", "name:world")

