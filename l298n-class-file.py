import RPi.GPIO as gpio
import time

class l298n:

    def __init__(self, pin1, pin2, pin3, pin4):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.init_pins()

    def init_pins(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin1, gpio.OUT)
        gpio.setup(self.pin2, gpio.OUT)
        gpio.setup(self.pin3, gpio.OUT)
        gpio.setup(self.pin4, gpio.OUT)

    def move_forward(self):
        self.init_pins()
        print("Moving forward")
        time.sleep(1)
        gpio.output(self.pin1, True)
        gpio.output(self.pin2, False)
        gpio.output(self.pin3, True)
        gpio.output(self.pin4, False)
        gpio.cleanup()

    def move_backward(self):
        self.init_pins()
        print("Moving backward")
        time.sleep(1)
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, True)
        gpio.output(self.pin3, False)
        gpio.output(self.pin4, True)
        gpio.cleanup()

    def stop(self):
        self.init_pins()
        print("Stopping motors")
        time.sleep(1)
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, False)
        gpio.output(self.pin3, False)
        gpio.output(self.pin4, False)
        gpio.cleanup()

    def start(self):
        self.init_pins()
        self.move_forward()
        gpio.cleanup()

    def move_right(self):
        self.init_pins()
        print("Moving right")
        time.sleep(1)
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, True)
        gpio.output(self.pin3, True)
        gpio.output(self.pin4, False)
        gpio.cleanup()

    def move_left(self):
        self.init_pins()
        print("Moving left")
        time.sleep(1)
        gpio.output(self.pin1, True)
        gpio.output(self.pin2, False)
        gpio.output(self.pin3, False)
        gpio.output(self.pin4, True)
        gpio.cleanup()
