import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
from digitalio import DigitalInOut
import time
# Talk to the LCD at I2C address 0x27 or 0x3F.
lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)
button = DigitalInOut(board.D2)

lcd.print("Ready?")
time.sleep(0.05)
lcd.clear()

# Start at the second line, fifth column (numbering from zero).
lcd.set_cursor_pos(1, 2)
lcd.print("Button Presses :")
lcd.print(0)
while True:

    if button.value:  # button is pushed
    lcd.print(++)
    time.sleep(0.05)
# Make the cursor visible as a line.
lcd.set_cursor_mode(CursorMode.LINE)