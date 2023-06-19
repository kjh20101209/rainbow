let item = neopixel.create(DigitalPin.P1, 8, NeoPixelMode.RGB)
item.showRainbow(1, 360)
basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P2) < 512) {
        item.show()
        item.rotate(-1)
        basic.pause(100)
    } else {
        item.show()
        item.rotate(1)
        basic.pause(100)
    }
})
