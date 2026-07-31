from .rawData.aircon_raw import RAW_DATA1
from pathlib import Path
import time
import RPi.GPIO as GPIO

TX_GPIO = 18
CARRIER_HZ = 38_000
DUTY_CYCLE = 33

RAW_POWER_ON = []

def ir_recive():
    print('ir_recive')

def ir_transmmit(raw_data):
    print('ir_transmmit :', raw_data)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TX_GPIO, GPIO.OUT, initial=GPIO.LOW)

    pwm = GPIO.PWM(TX_GPIO, CARRIER_HZ)
    pwm.start(0)

    try:
        print("에어컨 IR 신호 전송")

        for index, duratio_us in enumerate(raw_data):
            if index % 2 == 0:
                pwm.ChangeDutyCycle(DUTY_CYCLE)
            else:
                pwm.ChangeDutyCycle(0)

            wait_microseconds(duratio_us)

        pwm.ChangeDutyCycle(0)
        GPIO.output(18, GPIO.LOW)    
        print("전송 완료")

    finally:
        pwm.ChangeDutyCycle(0)
        pwm.stop()
        GPIO.output(TX_GPIO, GPIO.LOW)
        GPIO.cleanup()

    

def ir_actions(command):

    match command:
        case 'recive':
            print("recive")
        
        case 'transmit':
            ir_transmmit(RAW_DATA1)
        
        case _:
            print('지원하지 않는 명령어')


    print('ir_actions: ', command)
