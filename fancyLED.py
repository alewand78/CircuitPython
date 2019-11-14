from time import sleep
from digitalio import DigitalInOut, Direction, Pull #pylint: disable=import-error
from random import randint

class FancyLED:

    counter = 0

    def __init__(self, p1, p2, p3):
        print("I exist")
        self.pin1 = DigitalInOut(p1)
        self.pin1.direction = Direction.OUTPUT
        self.pin2 = DigitalInOut(p2)
        self.pin2.direction = Direction.OUTPUT
        self.pin3 = DigitalInOut(p3)
        self.pin3.direction = Direction.OUTPUT

    def alternate(self):
           self.pin1.value = True
           self.pin2.value = False
           self.pin3.value = True
           sleep(0.5)
           self.pin1.value = False
           self.pin2.value = True
           self.pin3.value = False
           sleep(0.5)

    def blink(self):
            self.pin1.value = True
            self.pin2.value = True
            self.pin3.value = True
            sleep(1)
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = False
            sleep(1)
            self.pin1.value = True
            self.pin2.value = True
            self.pin3.value = True
            sleep(1)

    def chase(self):
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = False
            sleep(.2)
            self.pin1.value = True
            self.pin2.value = False
            self.pin3.value = False
            sleep(.2)
            self.pin1.value = True
            self.pin2.value = True
            self.pin3.value = False
            sleep(.2)
            self.pin1.value = False
            self.pin2.value = True
            self.pin3.value = True
            sleep(.2)
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = True
            sleep(.2)

    def sparkle(self):
            for counter in range(0,25):
                    pin1_rand = randint(1,2)
                    pin2_rand = randint(1,2)
                    pin3_rand = randint(1,2)
                    if pin1_rand == 1:
                            self.pin1.value = True
                    else:
                            self.pin1.value = False
                    if pin2_rand == 1:
                            self.pin2.value = True
                    else:
                            self.pin2.value = False
                    if pin3_rand == 1:
                            self.pin3.value = True
                    else:
                            self.pin3.value = False
                    counter += 1
                    sleep(.05)
                    print(counter)