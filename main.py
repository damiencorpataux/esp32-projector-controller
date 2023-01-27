from pinout import Pinout
import machine
import time


class Projector(object):

    def __init__(self, name='Projector', **pins):
        self.name = name
        self.pinout = Pinout(**pins)

    def shutter(self, value):
        print('{}: shutter {}'.format(self.name, value))
        self.pinout.value('shutter', not value)

    def next(self):
        print('{}: next slide'.format(self.name))
        self.pinout.value('next', 0)
        time.sleep(0.5)
        self.pinout.value('next', 1)

    def blink(self, period=500, divisors=(1, 2, 4, 8, 16, 32, 64, 128)):
        print('{}: next blink all pins'.format(self.name))
        while True:
            for timeout, delay in [(1000, period/divisor) for divisor in divisors]:
                for i in range(int(timeout/delay/2)):
                    p.pinout.all('value', 0)
                    time.sleep(delay/1000)
                    p.pinout.all('value', 1)
                    time.sleep(delay/1000)
 

p = Projector(
    p1_shutter = machine.Pin(25, machine.Pin.OUT),
    p1_next = machine.Pin(26, machine.Pin.OUT),
    p2_shutter = machine.Pin(32, machine.Pin.OUT),
    p2_next = machine.Pin(33, machine.Pin.OUT),
)

p1 = Projector(
    'Projector 1',
    shutter = p.pinout.pin('p1_shutter'),
    next = p.pinout.pin('p1_next')
)

p2 = Projector(
    'Projector 2',
    shutter = p.pinout.pin('p2_shutter'),
    next = p.pinout.pin('p2_next')
)


def cycle():
    p1.shutter(0)
    p2.shutter(1)
    p2.next()
    time.sleep(0.67)
    p1.shutter(1)
    p2.shutter(0)
    p1.next()
    time.sleep(0.67)#5)

def forever():
    while True:
        cycle()


# Post-boot instructions

print("""
Welcome to Projector controller !

Usage:

p.pinout.all('value', 0)
p.pinout.all('value', 1)

p.blink()
p.pinout.all('blink', timeout=None)

cycle()
forever()

--8<-----

I will now start the show !
(press ctrl-c to stop)

""")

forever()