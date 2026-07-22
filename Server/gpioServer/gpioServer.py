import socket
import json
import RPi.GPIO as GPIO
import time

server = socket.socket()
server.bind(('127.0.0.1', 8888))
server.listen()

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

print('Python 서버 실행 중')

while True:
    client, address = server.accept()
    order = json.loads(client.recv(1024).decode())

    print('req order >> ', order)

    # 실제 GPIO 제어 위치
    # GPIO.output(17, GPIO.HIGH)
    GPIO.output(17, False)
    time.sleep(2)
    GPIO.output(17, True)
    time.sleep(2)

    client.send("OK".encode())
    client.close()


