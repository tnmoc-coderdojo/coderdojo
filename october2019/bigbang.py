
from sense_hat import SenseHat
import time
import random

sense=SenseHat()
col = (255, 255, 255)
factor = 0.9
display = [col for n in range(64)]
#sense.set_pixels(display)

#sense.set_pixel(3, 5, col)
time.sleep(1)

#for n in range(500):
while(True):

	sense.set_pixels(display)
	for pixel,n  in zip(display,range(64)):
		display[n] = (int(pixel[0]*factor), int(pixel[1]*factor), int(pixel[2]*factor))

	if random.randint(1, 10) ==  5:

		# Use this for  stars of same colour
		 display[random.randint(0,63)] = col

		# USe this for random colour stars
		#display[random.randint(0,63)] = (random.randint(100,255), random.randint(100,255), random.randint(100,255))

	time.sleep(0.05)
