#!/usr/bin/env python3

import RPi.GPIO as GPIO
import subprocess
import time

pin = 14
threshold = 60
duration_sec = 1

def main():
    # Warning停止
    GPIO.setwarnings(False)
    # SoCのGPIOピン番号
    GPIO.setmode(GPIO.BCM)
    # GPIO設定
    GPIO.setup(pin, GPIO.OUT)

    # 温度読み取り
    with open('/sys/class/thermal/thermal_zone0/temp', mode='r') as file:
        # 1000倍の値が書き込まれているので除算
        temp = float(file.read()) / 1000

        # 閾値以上のときGPIOをHIGHにしてファン回す
        if temp < threshold:
            GPIO.output(pin, GPIO.LOW)
        else:
            GPIO.output(pin, GPIO.HIGH)

if __name__ == '__main__':
    while True:
        main()
        # 一定間隔でループ
        time.sleep(duration_sec)