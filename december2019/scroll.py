
from sense_hat import SenseHat
import time
import random

sense=SenseHat()

G = (0,255,0)
R = (255,0,0)
Y = (255,255,0)
B = (80,42,42)
W = (255,255,255)
Q = (0,0,200)
Z = (0,0,255)

BLANK = (0,0,0)
_ = BLANK

star1    = [_,_,_,_,_,_,_,_,
	    _,_,_,_,_,_,_,_,
	    _,_,_,G,G,G,G,G,
	    _,_,_,G,_,R,_,G,
	    _,_,Y,G,R,R,R,G,
	    _,Y,_,G,_,R,_,G,
	    _,_,_,G,G,G,G,G,
	    _,_,_,_,_,_,_,_,
	    _,_,_,_,_,_,_,_,
	    _,_,_,_,_,Y,Y,Y,
	    _,_,_,_,_,Y,Y,Y,
	    _,_,_,_,_,Y,Y,Y,
	    _,_,_,_,_,Y,Y,Y,
	    _,_,_,_,_,_,_,_,
	    _,_,_,_,_,_,_,_,
	    _,_,_,Y,R,R,R,R,
	    _,_,_,Y,R,R,R,R,
	    _,_,_,_,_,_,_,_,
	    _,_,_,_,_,_,Z,Z,
	    _,_,_,_,_,_,Z,Z,
	    _,_,_,R,R,R,Z,Z,
	    _,Y,Y,R,R,R,Z,Z,
	    _,Y,Y,R,R,R,Z,Z,
	    _,_,_,R,R,R,_,_,
	    _,_,_,_,_,_,_,_,

]

for n in range(80):

	star1 = star1[8:] + star1[:8]

	sense.set_pixels(star1[:64])
	time.sleep(0.1)

sense.set_pixels([BLANK for n in range(64)])
