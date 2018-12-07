# Inkyphat_Assistant

Building a speech controled multi-functional deskside gadget.

This is a personal project working with Raspberry pi zero w, Pimoroni Inkyphat and MakerSpot 4-port USB HubHAT.

Two SanDisk Cruzer 32 GB flash drive and one Kinobo usb mini microphone are used for hardware extensions.

![Greeting](../master/test_images/ShibaInu_startup.jpg)

## Get Started

If you would prefer a pre-soldered Raspberry pi zero w as i did, buy one along the Inkyphat from adafruit:

* [Raspberry Pi Zero WH](https://www.adafruit.com/product/3708) - Pre-soldered pi zero board

* [Inky pHAT(adafruit)](https://www.adafruit.com/product/3933) - Pimoroni eink 212*104 tri-color eink hat ship from adafruit

* [Inky pHAT(Pimoroni)](https://shop.pimoroni.com/products/inky-phat) - Official product page from Pimoroni

I bought the yellow/Black/White for color of my design. 

Red/Black/White or Black/White pHat are availiable from their website.

## Setup

First prepare a SD card with Raspbian Stretch Lite,

* [Download Raspbian Strech Lite](https://www.raspberrypi.org/downloads/raspbian/) - Headless SSH and WiFi will be setup

Use etcher to flash Lite to sd card,

* [balenaEtcher](https://www.balena.io/etcher/) - Care x64 or x86


After sd card is prepared, unplug and plug back in. Etcher will auto reject USB after finished.

Then, enter the 'boot' root directory through file explorer and start by creating a file name 'ssh'.

Note this file should not contain extension such as .txt, this is created to enable SSH connection to pi zero.

And create a file named 'wpa_supplicant.conf', enter code below:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US
 
network={
    ssid="YOURSSID"
    psk="YOURPASSWORD"
    scan_ssid=1
}
```

Replace the YOURSSID and YOURPASSWORD with your WiFi information. The final code should be like:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US
 
network={
    ssid="abc"
    psk="123456"
    scan_ssid=1
}
```

Plug in power and the LED indicator should light up. Go to your WiFi router setting page and find out IP address for raspberry.

Personally I highly recommend using PuTTY for SSH client.

* [PuTTY](https://www.putty.org/) - SSH toward pi zero with IP address

Raspbian default username is "pi" and password is "raspberry". Now SSH should be functional.


## Installing

Start with updating and upgrading Raspbian


```
sudo apt-get update
sudo apt-get upgrade
```

To support microphone audio input, [Pyaudio](https://people.csail.mit.edu/hubert/pyaudio/) is needed.

```
sudo pip3 install pyaudio
```

Note that 'sudo' is necessary only if there is permission error during installing.


In this project, I used python [SpeechRecognition library](https://github.com/realpython/python-speech-recognition) for speech recognition.

```
sudo pip3 install SpeechRecognition
```

And most important library, the [inkyphat library from Pimoroni](https://github.com/pimoroni/inky-phat). I recommend install with,

```
sudo apt-get install python3-inkyphat
```

All listed libraries should run in python3 environment.

## Function

The speech recognition is set to catch keywords that triggers different functions. Current audio keyword contains:

```
logo (showing the original logo from inkyphat)
calendar (showing calendar)
clean (eink color cleaning, clear up color after multiple uses)
```

(I am using os.system for calling in main.py, not a good practice but there is conflict between 2.7 and 3.4 in my raspbian)

## Artwork

All .png artwork is done through Pixilart and organized in [my gallery](https://www.pixilart.com/pingrenworkhard/gallery).

Check out [Artwork Information](https://github.com/PingRen32/Inkyphat_Assistant/blob/master/resources/ShibaInu_resources/ARTWORK.md) for more information.

## Notes

This repo will be constantly updated as developed.

Multiple functions and features are still in construction progress.

Contact me if you have any question.
