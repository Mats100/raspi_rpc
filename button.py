import RPi.GPIO as GPIO
from autobahn import wamp


class RelaySwitch:

    @wamp.register('com.test.relay', check_types=True)
    async def switch_relay(self):
        relay_pins = 16
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(relay_pins, GPIO.OUT)
        GPIO.setwarnings(False)
        print(GPIO.gpio_function(relay_pins))
        if GPIO.input(relay_pins):
            GPIO.output(relay_pins, GPIO.LOW)
        else:
            GPIO.output(relay_pins, GPIO.HIGH)

        GPIO.cleanup()
