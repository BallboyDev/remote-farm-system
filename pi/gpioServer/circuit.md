# Circuit List

## 기능 회로
### LED ON/OFF
~~~
Ground 핀 --- 저항(1k) --- LED (short)
GPIO17 --- LED (long)
~~~

### IR Reciver
~~~
물리 11 --- OUT/DATA
물리 1 --- VCC
물리 6 --- GND
~~~

### IR Transmitter
~~~
물리 2번핀(5V) ───────────── S9012 E

물리 2번핀(5V) ── 10kΩ ──── S9012 B
S9012 B ───────── 1kΩ ────── 2N2222A C

물리 12번핀(GPIO18) ─ 2.2kΩ ─ 2N2222A B

물리 6번핀(GND) ──────────── 2N2222A E
S9012 C ──────────────────── IR 송신 DAT
물리 6번핀(GND) ──────────── IR 송신 GND

IR 송신 VCC ──────────────── 연결하지 않음(NC)
~~~




## 반도체 부품류
### 트랜지스터 [(데이터시트)](https://quartzcomponents.com/products/2n2222-npn-switching-transistor)
- S9012, 2N2222A
~~~
E━┓
B━╋━D
C━┛
~~~