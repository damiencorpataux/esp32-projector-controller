"""
Pinout Management.

FIXME: make functions accept argunent *pin_names for raw operations (meaning all pins if empty)
"""

import machine
import time

class Pinout(object):

    pinout = {
        'led-onboard': machine.Pin(2, machine.Pin.OUT)
    }

    def __init__(self, **pinout):
        self.pinout = pinout

    def pin(self, name):
        return self.pinout[name]
    
    def all(self, method, *args, **kwargs):
        return {
            pin_name: getattr(self, method)(pin_name, *args, **kwargs)
            for pin_name, pin in self.pinout.items()}

    def value(self, pin_name, *value):
        pin_object = self.pin(pin_name)
        pin_object.value(*value)
        return pin_object.value()

    def values(self, *pin_names, pin_value=-1):
        # FIXME: -1 to define an undefined value insted of None which is interpreted as 0 by machine.Pin.value()
        return {
            pin_name: self.value(pin_name) if pin_value != -1 else self.value(pin_name, pin_value)
            for pin_name in (pin_names or self.pinout.keys())}

    def blink(self, pin_name, timeout=1000, period=250, end_value=None):
        def infinity():
            while True:
                yield

        end_value = end_value if end_value is not None else self.value(pin_name)
        for i in range(int(timeout/delay/2)) if timeout else infinity():
            self.value(pin_name, not end_value)
            time.sleep(delay/1000)
            self.value(pin_name, end_value)
            time.sleep(delay/1000)
        # self.value(pin_name, end_value)