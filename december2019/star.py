
from sense_hat import SenseHat
import time
import random

sense=SenseHat()

BLANK = (0,0,0)
_ = BLANK

star = [1,0,1,0,0,1,0,1,
	0,1,0,0,0,0,1,0,
	1,0,1,0,0,1,0,1,
	0,0,0,1,1,0,0,0,
	0,0,0,1,1,0,0,0,
	1,0,1,0,0,1,0,1,
	0,1,0,0,0,0,1,0,
	1,0,1,0,0,1,0,1]

def getNewColour(oldColour):

	return (random.randint(oldColour[0]-15, oldColour[0]+15),
		random.randint(oldColour[1]-15, oldColour[1]+15),
		random.randint(oldColour[2]-15, oldColour[2]+15))

col = (128,128,128)
for t in range(1000):

	l = []
	for n in star:

		if n:
			l.append(col)
		else:
			l.append(_)


	try:
		sense.set_pixels(l)

	except:
		col = (128,128,128)
		print('Start again...')

	col = getNewColour(col)

	time.sleep(0.1)

display = [BLANK for n in range(64)]
sense.set_pixels(display)

