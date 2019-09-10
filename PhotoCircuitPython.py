from digitalio import DigitalInOut, Direction, Pull
import board
import time

interupt_pin = DigitalInOut(board.D6)
interupt_pin.direction = Direction.INPUT
interupt_pin.pull = Pull.Up


interrupts = 0

interupt_state = False
last_state = False

limit = 0

max = 4
start = time.time()
while True:
    interupt_state = interupt_pin.value
    if interupt_state and not last_state:
        interrupts += 1
    last_state = interupt_state

# This will be updated every loop
    remaining = max + start - time.time()
# when Countdown ends, prints value
    if remaining <= 0:
        print("Interrupts:", str(interrupts))
        max += 4
        interrupts = 0