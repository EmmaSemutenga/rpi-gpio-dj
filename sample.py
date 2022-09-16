from gpiozero import LED
from time import sleep

green = LED(25)

green.on()
sleep(5)
green.off()
