from pathlib import Path
import time
import RPi.GPIO as GPIO


TX_GPIO = 18
CARRIER_HZ = 38_000
DUTY_CYCLE = 33

RAW_FILE = (
    Path(__file__).resolve().parent
    / "rawData"
    / "aircon_raw.txt"
)


def load_raw_data(file_path):
    """
    mode2 형식의 파일을 읽습니다.

    반환 예:
    [
        ("pulse", 8988),
        ("space", 4418),
        ("pulse", 615),
        ...
    ]
    """
    raw_data = []

    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) != 2:
                raise ValueError(
                    f"{line_number}번째 줄 형식 오류: {line}"
                )

            signal_type, duration_text = parts

            try:
                duration_us = int(duration_text)
            except ValueError as error:
                raise ValueError(
                    f"{line_number}번째 줄의 시간이 숫자가 아닙니다: "
                    f"{duration_text}"
                ) from error

            if signal_type == "timeout":
                # 신호의 끝이므로 저장하거나 송신하지 않습니다.
                break

            if signal_type not in ("pulse", "space"):
                raise ValueError(
                    f"{line_number}번째 줄의 알 수 없는 신호: "
                    f"{signal_type}"
                )

            raw_data.append(
                (signal_type, duration_us)
            )

    if not raw_data:
        raise ValueError(
            f"RAW 신호가 비어 있습니다: {file_path}"
        )

    if raw_data[0][0] != "pulse":
        raise ValueError(
            "RAW 신호의 첫 번째 항목은 pulse여야 합니다."
        )

    return raw_data


def wait_microseconds(duration_us):
    """
    마이크로초 단위로 대기합니다.

    Linux 스케줄러의 영향으로 약간의 시간 오차가
    발생할 수 있습니다.
    """
    end_time = time.perf_counter_ns() + duration_us * 1_000

    while time.perf_counter_ns() < end_time:
        pass


def send_raw(pwm, raw_data):
    for signal_type, duration_us in raw_data:
        if signal_type == "pulse":
            # 38kHz 반송파 출력
            pwm.ChangeDutyCycle(DUTY_CYCLE)

        elif signal_type == "space":
            # IR LED 끄기
            pwm.ChangeDutyCycle(0)

        wait_microseconds(duration_us)

    # 전송이 끝난 후 반드시 IR LED를 끕니다.
    pwm.ChangeDutyCycle(0)
    GPIO.output(TX_GPIO, GPIO.LOW)


def transmit_aircon():
    raw_data = load_raw_data(RAW_FILE)

    print(f"RAW 파일: {RAW_FILE}")
    print(f"펄스 항목 수: {len(raw_data)}")

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(
        TX_GPIO,
        GPIO.OUT,
        initial=GPIO.LOW
    )

    pwm = GPIO.PWM(TX_GPIO, CARRIER_HZ)
    pwm.start(0)

    try:
        send_raw(pwm, raw_data)
        print("에어컨 신호 전송 완료")

    finally:
        pwm.ChangeDutyCycle(0)
        pwm.stop()
        GPIO.output(TX_GPIO, GPIO.LOW)
        GPIO.cleanup()


if __name__ == "__main__":
    transmit_aircon()