import yaml

#yfn = 'hwAddressSp01a.yaml'
#yfn  = 'swOps01a.yaml'
yfn = 'swAddressSp01a.yaml'
yf  = open(yfn, 'rt')
yd  = yaml.safe_load(yf)
print(yd)

