# MicroPython TM1640 LED Matrix

A MicroPython library for a LED matrix modules using the TM1740 LED driver.

![demo](docs/demo.jpg)

## Installation

Using mip via mpremote:

```bash
$ mpremote mip install github:mcauser/micropython-tm1640
```

Using mip directly on a WiFi capable board:

```python
>>> import mip
>>> mip.install("github:mcauser/micropython-tm1640")
```

Manual installation:

Copy `tm1640.py` to the root directory of your device.

## Examples

**Basic usage**

```python
import tm1640
from machine import Pin
tm = tm1640.TM1640(clk=Pin(14), dio=Pin(13))

# line from bottom left to top right
tm.write([1, 2, 4, 8, 16, 32, 64, 128])

# all on
tm.write([255, 255, 255, 255, 255, 255, 255, 255])

# all off
tm.write([0, 0, 0, 0, 0, 0, 0, 0])

# all LEDs dim
tm.brightness(1)

# all LEDs bright
tm.brightness(7)

# the number 3
tm.write([0b00000000, 0b00011110, 0b00110011, 0b00110000, 0b00011100, 0b00110000, 0b00110011, 0b00011110])

# cross
tm.write(b'\x81\x42\x24\x18\x18\x24\x42\x81')

# squares
tm.write([255, 129, 189, 165, 165, 189, 129, 255])

# 50% on
tm.write_int(0x55aa55aa55aa55aa)
```

For more detailed examples, see ![tm1640_test.py](tm1640_test.py)

## Modules

* [WeMos D1 Mini](https://www.aliexpress.com/item/32529101036.html)
* [WeMos Matrix LED Shield](https://www.aliexpress.com/item/32812932291.html)
* [DIY More MatrixLED Shield for D1 Mini](https://www.aliexpress.com/item/32821752799.html)
* [Dual Base for WeMos D1 Mini](https://www.aliexpress.com/item/32642733925.html)

## Connections

`CLK` and `DIO` are bit-banged. You can use any GPIO.

TM1640 LED Matrix | WeMos D1 Mini
----------------- | -------------
CLK               | D5 (GPIO14)
DIO               | D7 (GPIO13)
VCC               | 3V3/5V
GND               | G

## Links

* [WeMos D1 Mini](https://www.wemos.cc/en/latest/d1/index.html)
* [micropython.org](http://micropython.org)
* [TM1640 datasheet](http://www.titanmic.com/pic/other/2014-11-20-15-36-028.pdf)
* [Titan Micro TM1640 product page](http://www.titanmec.com/index.php/en/project/view/id/305.html)
* [MicroPython framebuf](http://docs.micropython.org/en/latest/esp8266/library/framebuf.html)

## License

Licensed under the [MIT License](http://opensource.org/licenses/MIT).
