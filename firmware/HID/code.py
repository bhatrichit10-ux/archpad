import board
import busio
import digitalio
import time
import neopixel
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import adafruit_ssd1306

# ---------------- OLED ----------------
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.rotation = 2

oled.fill(0)
oled.text("   /\\", 0, 0, 1)
oled.text("  /  \\", 0, 10, 1)
oled.text(" /\\   \\", 0, 20, 1)
oled.text("/______\\", 0, 30, 1)
oled.text("Arch", 70, 10, 1)
oled.text("Linux", 70, 22, 1)
oled.show()

# ---------------- HID ----------------
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# ---------------- BUTTONS ----------------
pins = {
    "MISO": board.MISO,   # unused
    "MOSI": board.MOSI,   # :skulk:
    "SCK": board.SCK,     # hello
    "RX": board.RX,       # bhatrichit10-ux
    "A0": board.A0,       # U0A3VK4GFRN
    "A1": board.A1,       # Ctrl + Shift + C
}

buttons = {}
last = {}

for name, pin in pins.items():
    b = digitalio.DigitalInOut(pin)
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP
    buttons[name] = b
    last[name] = True

# ---------------- NEOPIXELS ----------------
pixel_onboard = neopixel.NeoPixel(
    board.NEOPIXEL, 1, brightness=0.3, auto_write=False
)

pixel_external = neopixel.NeoPixel(
    board.A3, 1, brightness=0.3, auto_write=False
)

GREEN = (0, 40, 0)
RED = (40, 0, 0)

def set_pixels(color):
    pixel_onboard[0] = color
    pixel_external[0] = color
    pixel_onboard.show()
    pixel_external.show()

set_pixels(GREEN)

# ---------------- MAIN LOOP ----------------
while True:
    any_pressed = False

    for name, btn in buttons.items():
        if not btn.value and last[name]:
            if name == "SCK":
                layout.write("hello")

            elif name == "RX":
                layout.write("bhatrichit10-ux")

            elif name == "A0":
                layout.write("U0A3VK4GFRN")

            elif name == "A1":
                keyboard.press(
                    Keycode.CONTROL,
                    Keycode.SHIFT,
                    Keycode.C
                )
                time.sleep(0.05)
                keyboard.release_all()

            elif name == "MOSI":
                layout.write(":skulk:")

        if not btn.value:
            any_pressed = True

        last[name] = btn.value

    set_pixels(RED if any_pressed else GREEN)
    time.sleep(0.01)
