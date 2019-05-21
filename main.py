from machine import Pin

green_led = Pin(2, mode=Pin.OUT)

light_in = Pin(13, mode=Pin.IN)

while(True):
    light_in.value()