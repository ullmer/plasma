import yaml
yfn = 'plasma_types.yaml'
try:
  yf  = open(yfn, 'rt')
  yd  = yaml.safe_load_all(yf)
  yd1 = next(yd)
except: 
  print("yaml parsing error")

print(yd1)
