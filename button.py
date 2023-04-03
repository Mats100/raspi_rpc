import RPi.GPIO as GPIO
from autobahn import wamp

relay_pins = [16, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(relay_pins, GPIO.OUT)


class RelaySwitch:

    @wamp.register('com.test.relay', check_types=True)
    async def switch_relay(self, state):

        if state == "off":
            GPIO.output(relay_pins, GPIO.LOW)
            print("Relay turned on")
        elif state == "on":
            GPIO.output(relay_pins, GPIO.HIGH)
            print("Relay turned off")
        else:
            print("Invalid state")


GPIO.cleanup()
