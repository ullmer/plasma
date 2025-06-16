import yaml
yfn = 'asquare02.yaml'
yf  = open(yfn, 'rt')
yd  = yaml.safe_load(yf)
print(yd)
