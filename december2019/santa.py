
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
P = (255,182,193)

BLANK = (0,0,0)
_ = BLANK

santa1   = [_,_,_,W,_,_,_,_,
	    _,_,_,R,_,_,_,_,
	    _,_,R,R,_,_,_,_,
	    _,R,R,R,R,_,_,_,
	    P,_,Q,_,Q,P,_,_,
	    P,_,_,_,_,P,_,_,
	    P,_,R,R,_,P,_,_,
	    _,P,P,P,P,_,_,_]

santa2   = [_,_,_,W,_,_,_,_,
	    _,_,_,R,_,_,_,_,
	    _,_,R,R,_,_,_,_,
	    _,R,R,R,R,_,_,_,
	    P,Q,_,Q,_,P,_,_,
	    P,_,_,_,_,P,_,_,
	    P,_,_,R,R,P,_,_,
	    _,P,P,P,P,_,_,_]

santa3   = [_,W,_,_,_,_,_,_,
	    _,_,R,_,_,_,_,_,
	    _,_,R,R,_,_,_,_,
	    _,R,R,R,R,_,_,_,
	    P,Q,_,Q,_,P,_,_,
	    P,_,_,_,_,P,_,_,
	    P,_,_,R,R,P,_,_,
	    _,P,P,P,P,_,_,_]


for n in range(5):

	sense.set_pixels(santa1)
	time.sleep(1)

	sense.set_pixels(santa2)
	time.sleep(0.3)

	sense.set_pixels(santa3)
	time.sleep(0.3)

	sense.set_pixels(santa2)
	time.sleep(0.3)

	sense.set_pixels(santa3)
	time.sleep(1)

sense.set_pixels([BLANK for n in range(64)])

