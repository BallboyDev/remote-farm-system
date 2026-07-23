import socket
import json
import RPi.GPIO as GPIO
import time
from modules.led_actions import led_actions


server = socket.socket()
server.bind(('127.0.0.1', 8888))
server.listen()



print('Python 서버 실행 중')

while True:
    client, address = server.accept()
    req = json.loads(client.recv(1024).decode())

    print('req >> ', req)


    # 실제 GPIO 제어 위치
    # GPIO.output(17, True)
    # time.sleep(2)
    # GPIO.output(17, False)

    # led_actions['turn_on'](100)
    # f`req['type']`_actions[req['action']](1)
    match req['type']:
        case 'led':
            led_actions[f"turn_{req['action']}"](1)
        case _:
            print('지원하지 않는 명령어')

    client.send("OK".encode())
    client.close()


