# Raspberry Pi 4 Power HAT Fan Controller Script

This is fan control script for [Raspberry Pi 4 OKdo Official Power HAT Case](https://www.okdo.com/jp/p/okdohat/) by Python3.

- Default settings
  - Threshold: temperature: 60℃
  - Polling duration: 1.0sec

## System Requirements

- Board: Raspberry Pi 4 Model B 4GB (OKdo)
- Case: OKdo Power HAT Case
- OS: Ubuntu MATE 20.04 LTS (arm64)
- Python: 3.8.5

## Usage

Install packages and a library.

```sh
sudo apt update
sudo install python3 python3-pip
sudo pip3 install RPi.GPIO
```

Copy scripts.

```sh
sudo cp power-hat-fan-control.py /opt
sudo cp power-hat-fan-control.service /etc/systemd/system
```

Enable and start a daemon.

```sh
sudo systemctl enable power-hat-fan-control
sudo systemctl start power-hat-fan-control
```
