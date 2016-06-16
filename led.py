from gpiozero import LED
from time import sleep
import random

led1 = LED(2)
led2 = LED(3)
while True:
    number = random.randrange(10)
    if number ==2:	
       led2.off()
       led1.on()
       print(number)
       sleep(2)
    if number ==3:
      led1.off()
      led2.on()
      print(number) 
      sleep(2)
