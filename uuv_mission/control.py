import numpy as np

class PDController:
    def __init__(self, kp=0.1, kd=0.6):
        self.kp = kp
        self.kd = kd
        self.prev_error = 0.0

    def reset(self):
        self.prev_error = 0.0

    def __call__(self, reference, output):
        error = reference - output
        control = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return control
