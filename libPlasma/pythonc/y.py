import yaml
yfn = 'plasma_types.yaml'
yf  = open(yfn, 'rt')
yd  = yaml.safe_load(yf)
print(yd)
