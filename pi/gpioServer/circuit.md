# Circuit List

## 라즈베리파이 3 핀 배열
||BCM|BOARD|BOARD|BCM|
|:-:|:-:|:-:|:-:|:-:|
|1|+3.3v|1|2|+5v|
|2|GPIO2|3|4|+5v|
|3|GPIO3|5|6|GND|
|4|GPIO4|7|8|GPIO14|
|5|GND|9|10|GPIO15|
|6|GPIO17|11|12|GPIO18|
|7|GPIO27|13|14|GND|
|8|GPIO22|15|16|GPIO23|
|9|+3.3v|17|18|GPIO24|
|10|GPIO10|19|20|GND|
|11|GPIO9|21|22|GPIO25|
|12|GPIO11|23|24|GPIO8|
|13|GND|25|26|GPIO7|
|14|ID_SD|27|28|ID_SC|
|15|GPIO5|29|30|GND|
|16|GPIO6|31|32|GPIO12|
|17|GPIO13|33|34|GND|
|18|GPIO19|35|36|GPIO16|
|19|GPIO26|37|38|GPIO20|
|20|GND|39|40|GPIO21|
|LAN| USB| 포트 |방향|

## 기능 회로
### LED ON/OFF
~~~
Ground 핀 --- 저항(1k) --- LED (short)
GPIO17 --- LED (long)
~~~

### IR Reciver
~~~
GPIO17 --- OUT/DATA
3.3V 핀 --- VCC
Ground 핀 --- GND
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