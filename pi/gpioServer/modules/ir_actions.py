import time

import pigpio

from .rawData.aircon_raw import RAW_DATA1


TX_GPIO = 18
CARRIER_HZ = 38_000
DUTY_CYCLE = 0.33


def ir_recive():
    print("ir_recive")


def make_carrier_pulses(duration_us):
    """지정된 시간 동안 출력할 38kHz carrier pulse를 생성한다."""
    if duration_us <= 0:
        raise ValueError(f"pulse 시간은 0보다 커야 합니다: {duration_us}")

    gpio_mask = 1 << TX_GPIO
    period_us = 1_000_000 / CARRIER_HZ
    high_us = max(1, round(period_us * DUTY_CYCLE))
    cycle_count = max(1, round(duration_us / period_us))
    elapsed_us = 0
    pulses = []

    for cycle_index in range(cycle_count):
        # 주기 끝을 누적 반올림해 26us와 27us를 섞어 평균 38kHz를 만든다.
        cycle_end_us = round((cycle_index + 1) * period_us)
        low_us = max(1, cycle_end_us - elapsed_us - high_us)

        pulses.append(pigpio.pulse(gpio_mask, 0, high_us))
        pulses.append(pigpio.pulse(0, gpio_mask, low_us))
        elapsed_us = cycle_end_us

    return pulses


def build_wave_pulses(raw_data):
    """mode2 형식의 RAW 데이터를 pigpio wave pulse 목록으로 변환한다."""
    gpio_mask = 1 << TX_GPIO
    pulses = []

    for signal_type, duration_us in raw_data:
        if not isinstance(duration_us, int) or duration_us <= 0:
            raise ValueError(
                f"잘못된 RAW 신호 시간: {signal_type} {duration_us}"
            )

        if signal_type == "pulse":
            pulses.extend(make_carrier_pulses(duration_us))

        elif signal_type == "space":
            pulses.append(pigpio.pulse(0, gpio_mask, duration_us))

        elif signal_type == "timeout":
            # timeout은 수신 종료 표시이므로 송신 파형에 포함하지 않는다.
            break

        else:
            raise ValueError(f"지원하지 않는 RAW 신호: {signal_type}")

    if not pulses:
        raise ValueError("송신할 RAW 데이터가 없습니다.")

    return pulses


def ir_transmmit(raw_data):
    """RAW 데이터를 하나의 pigpio wave로 만들어 GPIO18에서 전송한다."""
    pi = pigpio.pi()

    if not pi.connected:
        pi.stop()
        raise RuntimeError(
            "pigpiod에 연결할 수 없습니다. "
            "'sudo systemctl start pigpiod'를 실행하세요."
        )

    wave_id = None

    try:
        pi.set_mode(TX_GPIO, pigpio.OUTPUT)
        pi.write(TX_GPIO, 0)
        pi.wave_clear()

        pulses = build_wave_pulses(raw_data)
        added_pulse_count = pi.wave_add_generic(pulses)

        if added_pulse_count < 0:
            raise RuntimeError(
                f"pigpio wave pulse 등록 실패: {added_pulse_count}"
            )

        wave_id = pi.wave_create()

        if wave_id < 0:
            raise RuntimeError(f"pigpio wave 생성 실패: {wave_id}")

        print(
            "에어컨 IR 신호 전송: "
            f"RAW {len(raw_data)}개, wave pulse {added_pulse_count}개"
        )

        send_result = pi.wave_send_once(wave_id)

        if send_result < 0:
            raise RuntimeError(f"pigpio wave 전송 실패: {send_result}")

        while pi.wave_tx_busy():
            time.sleep(0.001)

        print("에어컨 IR 신호 전송 완료")

    finally:
        pi.wave_tx_stop()

        if wave_id is not None and wave_id >= 0:
            pi.wave_delete(wave_id)

        pi.wave_clear()
        pi.write(TX_GPIO, 0)
        pi.stop()


def ir_test():
    """600us carrier와 100ms space를 10회 전송한다."""
    test_raw_data = []

    for _ in range(10):
        test_raw_data.append(("pulse", 600))
        test_raw_data.append(("space", 100_000))

    print(test_raw_data)

    ir_transmmit(test_raw_data)


def ir_actions(command):
    match command:
        case "recive":
            ir_recive()

        case "transmit":
            ir_transmmit(RAW_DATA1)

        case "test":
            ir_test()

        case _:
            raise ValueError(f"지원하지 않는 IR 명령어: {command}")

    print("ir_actions: ", command)
