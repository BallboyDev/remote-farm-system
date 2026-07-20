# Raspberry Pi GPIO base

Python과 `gpiozero`를 사용한 LED 및 DC 모터 제어의 최소 예제입니다. 핀 번호는 물리 핀 번호가 아닌 **BCM GPIO 번호**입니다.

## 기본 배선

| 기능 | BCM GPIO | 물리 핀 |
|---|---:|---:|
| LED 제어 | 17 | 11 |
| 모터 정방향 입력 | 23 | 16 |
| 모터 역방향 입력 | 24 | 18 |
| 모터 PWM/Enable | 18 | 12 |

LED에는 직렬 저항(일반적으로 220~330Ω)을 사용하세요. DC 모터는 GPIO에 직접 연결하지 말고 TB6612FNG, L298N 같은 모터 드라이버를 사용해야 합니다. 모터는 별도 전원으로 공급하고 드라이버와 Raspberry Pi의 GND를 공통으로 연결하세요.

드라이버마다 핀 이름이 다를 수 있습니다. 일반적으로 `motor_forward`/`motor_backward`는 IN1/IN2에, `motor_enable`은 PWM 또는 EN 핀에 연결합니다. TB6612FNG의 STBY 핀도 활성화해야 합니다.

## 설치 및 실행

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python gpio_control.py led-blink
python gpio_control.py forward --speed 0.5 --seconds 2
python gpio_control.py backward --speed 0.3 --seconds 2
python gpio_control.py demo --speed 0.5
```

각 명령은 지정 시간이 지나면 출력 장치를 안전 상태로 되돌리고 GPIO 자원을 해제합니다. 핀을 바꾸려면 `gpio_control.py`의 `PinConfig` 값을 수정하세요.

## Node.js와 TCP 소켓 통신

Python GPIO 서버를 먼저 실행합니다.

```bash
python socket_server.py --host 0.0.0.0 --port 9000
```

같은 장비에서 Node.js 연결을 시험하려면 프로젝트의 `back` 디렉터리에서 실행합니다.

```bash
node pythonSocketClient.js
```

Node.js와 Raspberry Pi가 서로 다른 장비라면 Node.js 실행 환경에 Pi 주소를 지정합니다.

```bash
GPIO_SOCKET_HOST=192.168.0.10 GPIO_SOCKET_PORT=9000 node pythonSocketClient.js
```

애플리케이션 코드에서는 클라이언트를 한 번 만든 뒤 재사용할 수 있습니다.

```js
const PythonSocketClient = require('./pythonSocketClient');
const gpio = new PythonSocketClient();

await gpio.send({ command: 'led', on: true });
await gpio.send({ command: 'motor', direction: 'forward', speed: 0.5 });
await gpio.send({ command: 'motor', direction: 'stop' });
gpio.close();
```

메시지는 줄바꿈으로 구분된 JSON(NDJSON)입니다. 기본 포트 `9000`을 외부 네트워크에 공개하지 말고, 신뢰할 수 있는 내부망과 방화벽 안에서 사용하세요.
