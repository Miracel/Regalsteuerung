# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
#import colimpiiorsys
import math
from neopixel import *
from colorsys import hsv_to_rgb
from Tkinter import *
from threading import Thread

# LED strip configuration:
LED_COUNT      = 10     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor


class LED_Thread(Adafruit_NeoPixel, Thread):
    def __init__(self, animation):
        Thread.__init__(self)
        self.stop = False
        self.animation = animation
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        
    def run(self):
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        strip.begin()
        while not self.stop:
            print("Hallo")
            self.animation.animate(strip)
            time.sleep(1)        #definieren       


class GUI_surface:

    def __init__(self, master, strip):
        self.master = master
        master.title("LED Steuerung Steineregal")
        self.LED_Thread = None
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

        #Buttons, Labels und andere Objekte programmieren

        #Button RegenbogenAnimation
        self.rainbow_button = Button(master = window,
                    text = "Regenbogen Modus",
                    command = lambda: self.toggle(RainbowAnimation(strip)),
                    font = ("Arial", 20),
                    bg = "white",
                    fg = "black",   
                    height = 5,
                    width = 20)

        self.off_button = Button(master = window,
                    text = "Off",
                    command = lambda: self.toggle(OffAnimation(strip)),
                    font = ("Arial", 20),
                    bg = "white",
                    fg = "black",   
                    height = 5,
                    width = 20)
                    
        self.rainbow_button.pack()
        self.off_button.pack()

    def toggle(self, animation):
        #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        
        if self.LED_Thread is None:
            self.LED_Thread = LED_Thread(animation)
            self.LED_Thread.start()

        elif self.LED_Thread.animation.id != animation.id:
            self.LED_Thread.stop = True
            self.LED_Thread = None
            self.LED_Thread = LED_Thread(animation)
            self.LED_Thread.start()

        else:
            self.LED_Thread.stop = True
            self.LED_Thread = None

#Animationsueberklasse
class Animation():
    def __init__(self):
        self.id = -1
        #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        
    def animate(self):
        sleep(0.001)

#Animationen in eigenen Klasse mit der Erbung Animation

class RainbowAnimation(Animation, Adafruit_NeoPixel):

    def __init__(self, strip):
        self.id = 1
        self.hue = 0
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

    def animate(self, strip):
        print("Ih bims")

        
        
        #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        for i in range(LED_COUNT):
            strip.setPixelColorRGB(i, 200, 0, 0)
        strip.show()
        #rgb = [0,0,0]
        #for i in range(0, LED_COUNT - 1):
         #   color = strip.getPixelColor(i+1) 
          #  rgb[0] = (color & 0xFF0000) >> 16
           # rgb[1] = (color & 0x00FF00) >> 8
            #rgb[2] = (color & 0x0000FF)
            #strip.setPixelColorRGB(i, rgb[0], rgb[1], rgb[2])   
        #rgb = hsv_to_rgb(hue,1.0,0.2)
        #hue += 0.01
        #strip.setPixelColorRGB(LED_COUNT - 1, int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        #if hue > 1:
         #   hue = 0
        #strip.show()
        #time.sleep(0.05)
        #return hue

class OffAnimation(Animation, Adafruit_NeoPixel):

    def __init__(self, strip):
        self.id = 2
        self.hue = 0
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

    def animate(self, strip):
        print("Ih bims")

        
        
        #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        for i in range(LED_COUNT):
            strip.setPixelColorRGB(i, 0, 0, 0)
        strip.show()


def set_color (wait_ms=50):
    for i in range(LED_COUNT):
        strip.setPixelColorRGB(i, 200, 0, 0)
        strip.show()
        time.sleep(wait_ms/500)
        

def sector_control():
    rgb = [0,0,0]
    color =[(0,1),
            (0.333,1),
            (0.666,1),
            (0,0),  
            (5.236,1,1),
            (1.047,1,1),
            (0,1,1)]
    print("Choose Sector between 1 - 16: ")
    sector = input("Sector: ")
    if sector != 0 and sector < 17:
        print("Choose Color: [0] rot \n [1] gruen \n [2] blau \n [3] weiss  ")
        selection = input("Farbe waehlen: ")
        hue = color[selection][0]
        sat = color[selection][1]
        #val = color[selection][2]
        rgb = hsv_to_rgb(hue, sat, val)
        for i in range ((sector*22 - 22), (sector * 22)): 
            strip.setPixelColorRGB(i, int(rgb[1]*255), int(rgb[0]*255), int(rgb[2]*255))
        strip.show()
        time.sleep(0.5)
    else:
        print("Wrong Sector")  

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)


window = Tk()
regalsteuerung = GUI_surface(window, strip)
window.mainloop()
     
