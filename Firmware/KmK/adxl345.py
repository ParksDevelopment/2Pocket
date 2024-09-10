import busio
import board
import math

from kmk.extensions import Extension
import adafruit_adxl34x


class adxl345(Extension):
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        accelerometer = adafruit_adxl34x.ADXL345(i2c)
        self.accelerometer = accelerometer
        self.steps = 0
        self.currentstep = math.trunc(self.accelerometer.acceleration[2])

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        return

    def before_matrix_scan(self, sandbox):
        #print("X:", math.trunc(self.accelerometer.acceleration[0]), "Y:", math.trunc(self.accelerometer.acceleration[1]), "Z:", math.trunc(self.accelerometer.acceleration[2]), "steps: ", self.steps)
        if(self.currentstep < 1 and math.trunc(self.accelerometer.acceleration[2]) == 3):
            self.steps += 1
            self.currentstep = 3
        elif(self.currentstep > 2 and math.trunc(self.accelerometer.acceleration[2])  == 0):
            self.steps += 1
            self.currentstep = 0

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return
