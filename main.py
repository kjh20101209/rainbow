item = neopixel.create(DigitalPin.P1, 8, NeoPixelMode.RGB)
item.show_rainbow(1, 360)

def on_forever():
    if pins.analog_read_pin(AnalogPin.P2) < 512:
        item.show()
        item.rotate(-1)
        basic.pause(100)
    else:
        item.show()
        item.rotate(1)
        basic.pause(100)
basic.forever(on_forever)
