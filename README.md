# COZIR Resources and Serial Python Parser

A work in progress set of python tools to read data from the [COZIR-A sensor](https://www.digikey.com.au/product-detail/en/gas-sensing-solutions-ltd/COZIR-AH-1/2091-COZIR-AH-1-ND/9952878).

## Raspberry Pi Setup

### Goals

- Document the process of setting up a raspberry pi from scratch
- Document the appropriate way to run python scripts on a rapberry pi
- Connect and read COZIR vales
- Create a remote python development environment

### Connect COZIR to GPIO

Connect COZIR pins 1, 3, 5 7 to [GPIO pins](https://pinout.xyz/pinout/pin8_gpio14) 1, 6, 8, 10.

### Raspberry Pi setup

- Headless Raspberry pi setup

Config.txt options: [link](https://github.com/raspberrypi/documentation/tree/master/configuration/config-txt)

### SD Card setup

Download [Raspbian](https://www.raspberrypi.org/downloads/raspbian/), flash to SD card with [Etcher](https://www.balena.io/etcher/), re-mount boot drive. 

### Wifi, ssh, gpu_mem

```
touch /Volumes/boot/ssh
cp raspi/wpa_supplicant.conf /Volumes/boot/
```

config.txt

```
enable_uart=1
dtparam=i2c_arm=on
dtparam=i2s=on
dtparam=spi=on
```

Memory link: https://www.raspberrypi.org/documentation/configuration/config-txt/memory.md

### Hostname

Update these files:

sudo nano /etc/hostname
sudo nano /etc/hosts

### Password

passwd 

### Serial connection / Bluetooth

By default the primary UART is setup with a linux console. Handy for debugging but we want to turn it off and use it for other purposes. 

Update /boot/cmdline.txt and remove console=serial0,115200 console=tty1

(https://www.raspberrypi.org/documentation/configuration/cmdline-txt.md)

This can be disabled - [see docs](https://github.com/raspberrypi/documentation/blob/master/configuration/uart.md#disabling-linuxs-use-of-console-uart)

See `pi3-miniuart-bt` in /boot/overlays/README for info. Also https://raspberrypi.stackexchange.com/questions/45570/how-do-i-make-serial-work-on-the-raspberry-pi3-pi3b-pizerow/45571#45571

```
dtoverlay=pi3-miniuart-bt
core_freq=250
```

These are GPIO 14 (pin 8) (TXD), and 15 (pin 10) (RXD). 3.3v is Pin 1.

### I2C (maybe)

http://ozzmaker.com/i2c/

## Python

```
sudo apt install -y python-pip
pip install --user pyserial
```

## Links

- [Raspberrypi Pin out](https://pinout.xyz)

/dev/tty.usbserial-MG8ZKS


