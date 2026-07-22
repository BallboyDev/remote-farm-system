# iPhone 핫스팟 환경의 Express.js 웹서버 접속 장애 분석

## 1. 최초 증상과 환경

- 웹서버 주소: `http://172.20.10.6:3000`
- 서버: Raspberry Pi에서 실행 중인 Express.js
- 클라이언트: Mac
- 네트워크: iPhone 개인용 핫스팟
- 증상: 브라우저에서 웹서버에 연결되지 않음
- 최초에는 ping과 SSH 접근이 가능한 것으로 인식됨

## 2. Mac에서 IPv4 연결 검사

Mac에서 다음 항목을 검사했다.

- `172.20.10.6`까지의 라우팅 경로
- TCP 3000번 포트 연결
- HTTP 요청

라우팅 검사 결과는 다음과 같았다.

```text
route to: 172.20.10.6
gateway: 192.0.0.1
interface: en0
```

Mac은 `172.20.10.6`을 같은 로컬 네트워크의 장치로 취급하지 않고 `192.0.0.1` 게이트웨이로 전달하고 있었다. `curl`과 `nc`를 이용한 3000번 포트 연결도 실패했다.

## 3. Mac의 실제 네트워크 설정 확인

Mac의 `en0` 네트워크 설정은 다음과 같았다.

```text
IPv4: 192.0.0.2/32
IPv6: 2001:2d8:20a1:5d62:...
CLAT46 활성화
기본 게이트웨이: 192.0.0.1
```

Mac은 일반적인 iPhone 핫스팟 IPv4 주소인 `172.20.10.x`를 받지 않았다. 대신 IPv6 연결과 IPv4 호환을 위한 CLAT46, `/32` 주소인 `192.0.0.2`를 사용하고 있었다.

따라서 Mac에는 Raspberry Pi의 `172.20.10.6`으로 직접 접근할 수 있는 IPv4 로컬 경로가 없었다.

## 4. 기존 ping 및 SSH 접근 여부 재검증

현재 Mac에서 `172.20.10.6`을 다시 검사한 결과는 다음과 같았다.

```text
ping: 응답 없음
TCP 22번: 연결 실패
TCP 3000번: 연결 실패
```

따라서 최초에 알려진 ping과 SSH 접근 가능 상태는 현재 Mac의 네트워크 상태에서는 재현되지 않았다.

## 5. Raspberry Pi의 네트워크 확인

Raspberry Pi의 `ifconfig` 결과에서 다음 주소를 확인했다.

```text
wlan0 IPv4: 172.20.10.6/28
wlan0 IPv6: 2001:2d8:20a1:5d62:4c99:32ab:1646:c782
```

iPhone 핫스팟은 Mac과 Raspberry Pi를 서로 다른 IPv4 방식으로 구성하고 있었다.

| 장치 | IPv4 | IPv6 |
| --- | --- | --- |
| Mac | `192.0.0.2/32`, CLAT46 | 글로벌 IPv6 주소 있음 |
| Raspberry Pi | `172.20.10.6/28` | 글로벌 IPv6 주소 있음 |

두 장치의 IPv4 주소 체계는 달랐지만 동일한 IPv6 프리픽스를 사용하고 있었다.

## 6. IPv6 연결 검사

Mac에서 Raspberry Pi의 글로벌 IPv6 주소로 ping을 실행했다.

```bash
ping6 -c 3 '2001:2d8:20a1:5d62:4c99:32ab:1646:c782'
```

검사 결과는 다음과 같았다.

```text
3 packets transmitted
3 packets received
0.0% packet loss
```

이 결과로 다음 사실을 확인했다.

- iPhone의 장치 간 통신 차단 문제가 아님
- Mac과 Raspberry Pi 사이의 IPv6 네트워크가 정상임
- Raspberry Pi의 IPv6 주소까지 정상적으로 도달 가능함

## 7. IPv6 TCP 3000번 포트 검사

IPv6 주소의 3000번 포트에 연결을 시도했다.

```bash
nc -6 -vz -w 3 \
  '2001:2d8:20a1:5d62:4c99:32ab:1646:c782' \
  3000
```

결과는 다음과 같았다.

```text
Connection refused
```

`Connection refused`는 패킷이 Raspberry Pi까지 도달했지만 해당 IPv6 주소의 3000번 포트에서 수신 중인 프로세스가 없다는 의미이다. 네트워크 단절이나 응답 없는 방화벽과는 다른 결과다.

## 8. Express 수신 주소 확인

Raspberry Pi에서 Node.js 프로세스의 수신 상태를 확인했다.

```bash
sudo ss -lntp | grep ':3000'
```

결과는 다음과 같았다.

```text
LISTEN 0 511 0.0.0.0:3000 0.0.0.0:* users:(("node",pid=7422,fd=24))
```

`0.0.0.0:3000`은 Express가 모든 IPv4 인터페이스에서 수신하지만 IPv6에서는 수신하지 않는다는 뜻이다.

## 9. 최종 원인

다음 두 조건이 동시에 발생하여 브라우저 연결이 실패했다.

1. Mac은 iPhone 핫스팟에서 CLAT46 기반 `192.0.0.2/32` 주소를 받아 Raspberry Pi의 `172.20.10.6`으로 직접 접근할 IPv4 경로가 없다.
2. Express는 `0.0.0.0:3000`에서 IPv4 연결만 수신하고 있어, 정상적으로 통신 가능한 IPv6 경로로도 접속할 수 없다.

따라서 웹서버 자체는 IPv4에서 정상적으로 실행되고 있었지만, Mac에서 사용할 수 있는 네트워크 경로와 Express의 수신 프로토콜이 서로 일치하지 않았다.

## 10. 해결 방법

Express의 수신 주소를 IPv6 와일드카드 주소인 `::`로 변경한다.

```javascript
app.listen(3000, '::', () => {
  console.log('Server listening on port 3000');
});
```

Linux에서 다음 설정이 `0`이면 `::` 바인딩 하나로 IPv4와 IPv6 연결을 모두 수신할 수 있다.

```bash
sysctl net.ipv6.bindv6only
```

애플리케이션을 변경하고 재시작한 후 수신 상태를 확인한다.

```bash
sudo ss -lntp | grep ':3000'
```

예상 결과는 다음과 같다.

```text
LISTEN ... [::]:3000
```

Mac에서 IPv6 포트 연결을 다시 검사한다.

```bash
nc -6 -vz -w 3 \
  '2001:2d8:20a1:5d62:4c99:32ab:1646:c782' \
  3000
```

브라우저에서는 다음 주소로 접속한다.

```text
http://[2001:2d8:20a1:5d62:4c99:32ab:1646:c782]:3000/
```

IPv6 주소에는 콜론이 포함되므로 URL에서 반드시 대괄호로 감싸야 한다. 또한 글로벌 IPv6 주소는 iPhone 핫스팟을 재연결할 때 변경될 수 있다.
