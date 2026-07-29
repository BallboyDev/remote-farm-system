import socket
import json
import RPi.GPIO as GPIO
import time
# from modules.led_actions import led_actions
from modules import actions


server = socket.socket()
server.bind(('127.0.0.1', 8888))
server.listen()

print(f'Python 서버 실행 중 : 127.0.0.1:8888')

while True:
    client, address = server.accept()
    req = json.loads(client.recv(1024).decode())

    print('req >> ', req)
    device, command = (req['device'], req['command'])
    
    try:
        actions[device](command)
        client.send("success".encode())
    except KeyError:
        print(f'지원하지 않는 장치 : {device}')
        client.send("failure".encode())


    client.close()


