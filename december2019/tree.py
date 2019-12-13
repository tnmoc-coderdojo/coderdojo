
from sense_hat import SenseHat
import time
import random

sense=SenseHat()

G = (0,255,0)
R = (255,0,0)
Y = (255,255,0)
B = (80,42,42)
BLANK = (0,0,0)
_ = BLANK

treepic1 = [_,_,_,Y,_,_,_,_,
	    _,_,_,G,_,_,_,_,
	    _,R,_,G,_,R,_,_,
	    _,_,G,G,G,_,_,_,
	    _,_,_,G,_,_,_,_,
	    R,_,G,G,G,_,R,_,
	    _,G,G,G,G,G,_,_,
	    _,_,_,B,_,_,_,_]

treepic2 = [_,_,_,Y,_,_,_,_,
	    _,_,_,G,_,_,_,_,
	    _,_,_,G,_,_,_,_,
	    _,_,G,G,G,_,_,_,
	    _,_,_,G,_,_,_,_,
	    _,_,G,G,G,_,_,_,
	    _,G,G,G,G,G,_,_,
	    _,_,_,B,_,_,_,_]

for n in range(5):

	sense.set_pixels(treepic1)
	time.sleep(1)

	sense.set_pixels(treepic2)
	time.sleep(1)

sense.set_pixels([BLANK for n in range(64)])

