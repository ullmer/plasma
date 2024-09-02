
WIDTH, HEIGHT = 100, 100

mred   = "#773540"
mwhite = "#ffffff"
tbox   =  Rect((0, 70), (100, 100))
tpos1  = (100, -10)
tpos2  = ( 2,  102)
font1  = "oswald-medium"

def draw():
  screen.clear()
  screen.draw.filled_rect(tbox, mred)

  screen.draw.text("A",       topright  =tpos1, fontsize=70, fontname=font1, color=mwhite, alpha=0.5)
  screen.draw.text("SPATIAL", bottomleft=tpos2, fontsize=25, fontname=font1, color=mwhite, alpha=0.5)

### end ###
