import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def turn_on():
    print('led_on')
    # GPIO.output(17, True)


def turn_off():
    print('led_off')
    # GPIO.output(17, False)


def led_actions(command):

    match command:
        case 'on':
            turn_on()

        case 'off':
            turn_off()

        case _:
            print('지원하지 않는 명령어')
