import RPi.GPIO as GPIO
from autobahn import wamp


class RelaySwitch:

    @wamp.register('com.pk.codebase.relay.status.set', check_types=True)
    async def switch_relay(self):
        relay_pins = 26
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(relay_pins, GPIO.OUT)
        if GPIO.input(relay_pins):
            GPIO.output(relay_pins, GPIO.LOW)
        else:
            GPIO.output(relay_pins, GPIO.HIGH)

    @wamp.register('com.pk.codebase.relay.status.get', check_types=True)
    async def relay_status(self):
        relay_pins = 26
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(relay_pins, GPIO.OUT)

        status = GPIO.input(relay_pins)
        if status == 0:
            return True
        return False
