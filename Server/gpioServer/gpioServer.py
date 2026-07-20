import socket
import json

server = socket.socket()
server.bind(('127.0.0.1', 8888))
server.listen()

print('Python 서버 실행 중')

while True:
    client, address = server.accept()
    order = json.loads(client.recv(1024).decode())

    print('req order >> ', order)

    # 실제 GPIO 제어 위치
    # GPIO.output(17, GPIO.HIGH)

    client.send("OK".encode())
    client.close()


