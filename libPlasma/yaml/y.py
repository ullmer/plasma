import yaml

yfn = 'hwAddressSp01a.yaml'
yf  = open(yfn, 'rt')
yd  = yaml.safe_load(yf)
print(yd)

