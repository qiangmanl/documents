from const import DEVICE
import array, time
from machine import Pin,PWM
import rp2

NUM_LEDS = 1
PIN_NUM = 13
POWER =5000
# Initialize the PWM
pwm = PWM(Pin(6))
pwm.freq(POWER)
# Initialize the PIO
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()
#Initialize relay IO and configure RGB lights
class NeoPixel(object):
    def __init__(self,pin=PIN_NUM,num=NUM_LEDS,brightness=0.2):
        self.pin=pin
        self.num=num
        self.brightness = brightness
        # Create the StateMachine with the ws2812 program, outputting on pin
        self.sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))
        # Start the StateMachine, it will wait for data on its FIFO.
        self.sm.active(1)
        # Display a pattern on the LEDs via an array of LED RGB values.
        self.ar = array.array("I", [0 for _ in range(self.num)])   
        self.ch1 = Pin(21,Pin.OUT)
        self.ch2 = Pin(20,Pin.OUT)
        self.ch3 = Pin(19,Pin.OUT)
        self.ch4 = Pin(18,Pin.OUT)
        self.ch5 = Pin(17,Pin.OUT)
        self.ch6 = Pin(16,Pin.OUT)
        self.ch7 = Pin(15,Pin.OUT)
        self.ch8 = Pin(14,Pin.OUT)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 150, 0)
        self.GREEN = (0, 255, 0)
        self.CYAN = (0, 255, 255)
        self.BLUE = (0, 0, 255)
        self.PURPLE = (180, 0, 255)
        self.WHITE = (255, 255, 255)
    ##########################################################################
#The RGB output
    def pixels_show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self.num)])
        for i,c in enumerate(self.ar):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g<<16) + (r<<8) + b
        self.sm.put(dimmer_ar, 8)
#data conversion 
    def pixels_set(self, i, color):
        self.ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]
#Single color output
    def pixels_fill(self,color):
        for i in range(len(self.ar)):
            self.pixels_set(i, color)
#status lamp
    def RGB_OUT(self):
        self.pixels_fill(self.GREEN)
        self.pixels_show()
        time.sleep(0.05)
        self.pixels_fill(self.BLACK)
        self.pixels_show()
#pilot relay
    def Relay_CHx(self,n,switch): 
        if switch == 1:
            n.high()
        else:
            n.low()


strip = NeoPixel()
duty = 0
direction = 1
flag=[False,False,False,False,False,False,False,False]
channels = {
    1 : strip.ch1,
    2 : strip.ch2,
    3 : strip.ch3,
    4 : strip.ch4,
    5 : strip.ch5,
    6 : strip.ch6,
    7 : strip.ch7,
    8 : strip.ch8,
}

def do_response(channel, switch):
    assert switch in ("ON","OFF")
    if switch == "ON":
        strip.Relay_CHx(channels[channel],True)
        print(f"***Relay ch{channel} ON***")
    elif switch == "OFF":
        strip.Relay_CHx(channels[channel],False)
        print(f"***Relay ch{channel} OFF***")
    pwm.duty_u16(POWER)
    time.sleep(0.1)
    pwm.duty_u16(0)
    strip.RGB_OUT()
    print(f"***Relay ALL on***")


