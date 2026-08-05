# Circuit List
~~~
┏┳┓
┣╋┫
┗┻┛
━ ┃
~~~

## 기능 회로
### LED ON/OFF
~~~
p6(GND) ━━━━━ 1kΩ ━━━━ LED(short)
p11(gpio17) ━━━━━━━━━━ LED(long)
~~~

### IR Reciver
~~~
pin11 ━━━ OUT/DATA
pin1 ━━━━ VCC
pin6 ━━━━ GND
~~~

### IR Transmitter
~~~
pin2(5V) ━┳━━━━━━━━━━━━━━━ S9012-E
          ┗ 10kΩ ━┳━━━━━━━ S9012-B
                  ┗━ 1kΩ ━ 2N2222A-C

pin12(gpio18) ━━ 2.2kΩ ━━ 2N2222A-B

pin6(GND) ━┳━ 2N22222A-E
           ┗━ IR GND

S9012-C ━━━ IR DAT

IR VCC ━━━ No Connect
~~~

## 반도체 부품류
### 트랜지스터 [(데이터시트)](https://quartzcomponents.com/products/2n2222-npn-switching-transistor)
- S9012, 2N2222A
~~~
E━┓
B━╋━D
C━┛
~~~