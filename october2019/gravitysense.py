
# Import the relevent modules
from sense_hat import SenseHat
import time

# Set up the sense hat
sense = SenseHat()
sense.set_rotation(270)
sense.set_imu_config(False, True, False)  # gyroscope only

# Loop around forever
#while(True):
#  temp = round( sense.get_temperature_from_humidity(), 1 )
#  sense.show_message( str(temp))
#  time.sleep(0.5)
  
while(True):
  
  # Read values from Gyro
  gyro_only = sense.get_gyroscope()
  
  # Roll is left to right (on defalt mission zero emulator). Scale -> 0 - 8
  roll = int(gyro_only['roll'])
  if roll > 180:
    roll = roll - 360
    
  # Now have -90 - 90
  roll = int((roll + 90) / 22.5)
  
  print('R:', roll)

  # Roll is left to right (on defalt mission zero emulator). Scale -> 0 - 8
  pitch = int(gyro_only['pitch'])
  if pitch > 180:
    pitch = pitch - 360
    
  # Now have -90 - 90
  pitch = int((pitch + 90) / 22.5)
  
  print('P:', pitch)

  sense.set_pixel(roll, pitch, 255, 0, 255)

  #if 
  #print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
  
  # alternatives
  #print(sense.gyro)
  #print(sense.gyroscope)
  
  time.sleep(0.5)
  sense.set_pixel(roll, pitch, 0, 0, 0)

