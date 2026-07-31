from .rawData.aircon_raw import RAW_DATA1
from pathlib import Path
import time
import RPi.GPIO as GPIO

TX_GPIO = 18
CARRIER_HZ = 38_000
DUTY_CYCLE = 33

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

        for index, duration_us in enumerate(raw_data):
            if index % 2 == 0:
                pwm.ChangeDutyCycle(DUTY_CYCLE)
            else:
                pwm.ChangeDutyCycle(0)

            wait_microseconds(duration_us)

        pwm.ChangeDutyCycle(0)
        GPIO.output(18, GPIO.LOW)    
        print("전송 완료")

    finally:
        pwm.ChangeDutyCycle(0)
        pwm.stop()
        GPIO.output(TX_GPIO, GPIO.LOW)
        GPIO.cleanup()

def wait_microseconds(duration_us):
    """
    마이크로초 단위로 대기합니다.

    Linux 스케줄러의 영향으로 약간의 시간 오차가
    발생할 수 있습니다.
    """
    end_time = time.perf_counter_ns() + duration_us * 1_000

    while time.perf_counter_ns() < end_time:
        pass

def ir_actions(command):

    match command:
        case 'recive':
            print("recive")
        
        case 'transmit':
            ir_transmmit(RAW_DATA1)
        
        case _:
            print('지원하지 않는 명령어')


    print('ir_actions: ', command)
