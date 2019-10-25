
# Import the relevant modules
from sense_hat import SenseHat
import time

# Set up the sense hat
sense = SenseHat()
sense.set_rotation(270)

# Define our base colours
WHT = [100, 100, 100] # White - for the graph lines
AMB = [255, 255, 0  ] # Amber for the warnings
GRN = [0  , 255, 0  ] # Green for all good
RED = [255, 0,   0  ] # Red for all bad
BLK = [0  , 0  , 0  ] # Black for an LED in the off state

# Base withg graph lines on and all other LEDS off
BASE = [BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
        WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK]

# GOOD display - green in top right
GOOD = [BLK, BLK, BLK, WHT, WHT, GRN, GRN, GRN, 
        BLK, BLK, BLK, WHT, WHT, GRN, GRN, GRN, 
        BLK, BLK, BLK, WHT, WHT, GRN, GRN, GRN, 
        WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
        WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK]

# BAD display - red in bottom left
BAD  = [BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
        WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
        WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
        RED, RED, RED, WHT, WHT, BLK, BLK, BLK, 
        RED, RED, RED, WHT, WHT, BLK, BLK, BLK, 
        RED, RED, RED, WHT, WHT, BLK, BLK, BLK]

# BAD PRESSURE display - amber in   top left 
WARN1 = [AMB, AMB, AMB, WHT, WHT, BLK, BLK, BLK, 
         AMB, AMB, AMB, WHT, WHT, BLK, BLK, BLK, 
         AMB, AMB, AMB, WHT, WHT, BLK, BLK, BLK, 
         WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
         WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
         BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
         BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
         BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK]
         
# BAD TEMPERATURE display - amber in bottom left 
WARN2 = [BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
         BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
         BLK, BLK, BLK, WHT, WHT, BLK, BLK, BLK, 
         WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
         WHT, WHT, WHT, WHT, WHT, WHT, WHT, WHT, 
         BLK, BLK, BLK, WHT, WHT, AMB, AMB, AMB, 
         BLK, BLK, BLK, WHT, WHT, AMB, AMB, AMB, 
         BLK, BLK, BLK, WHT, WHT, AMB, AMB, AMB]

# Possible states that we can measure
ALLGOOD = 0
BADPRESSURE = 1
BADTEMPERATURE = 2
BOTHBAD = 3

# Disctionary maps the possible states onto the correct display
display = {ALLGOOD: GOOD, BADPRESSURE:WARN1, BADTEMPERATURE:WARN2, BOTHBAD: BAD }

# Boolean used to track whf display is on when we are in flashing mode
flash = False

# Main code starts here/ Loop around forever
while(True):

  # Assume the status is all ok
  status = ALLGOOD

  # Get the temperature and check the range
  temp = round(sense.get_temperature_from_humidity(), 1 )
  if temp < 18 or temp > 40:
    status = BADTEMPERATURE

  # Get the pressure and check the range    
  pres = round(sense.get_pressure(), 1)
  if pres < 850 or pres > 1050:
    status += BADPRESSURE

  # If the status is good then display the steady state
  if status == ALLGOOD:
    sense.set_pixels(display[status])
  else:
    
    # Status is not good so need to flash the display as a warning.
    if flash:
        sense.set_pixels(display[status])
    else:
        sense.set_pixels(BASE)
    flash = not flash
      
  # If we are in the both bad state then flash super quick, otherwise flash at normal speed
  if status == BOTHBAD:
    time.sleep(0.1)
  else:
    time.sleep(1)
