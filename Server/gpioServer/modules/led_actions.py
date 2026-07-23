import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def turn_on(pin):
    print(f"GPIO {pin} ON")
    GPIO.output(17, True)


def turn_off(pin):
    print(f"GPIO {pin} OFF")
    GPIO.output(17, False)


def read_state(pin):
    print(f"GPIO {pin} 상태 읽기")
    return False

led_actions = {
    "turn_on":turn_on,
    "turn_off":turn_off,
    "read_state":read_state
}