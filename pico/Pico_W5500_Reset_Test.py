import time
import board
import digitalio

W5500_RSTn = board.GP15

# led = digitalio.DigitalInOut(board.LED)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

ethernetRst = digitalio.DigitalInOut(W5500_RSTn)
ethernetRst.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    ethernetRst.value = False
    time.sleep(1)
    ethernetRst.value = True
    time.sleep(5)
