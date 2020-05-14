# LGDuctlessControl

The purpose of this project is to control the LG Ductless HVAC system in my condo. Each zone has a remote, but I like the idea of being able to control all the zones at once. Especailly if I'm away, with a VPN setup, I could control the zones remotely.

## Components
1. **Master Webapp (Flask)** - This will run on my main server. Users have the ability to specify controls for the zones via UI. Things like on/off, temp control, and sleep time
  
2. **Client Webapp (Flask)** - This webapp will run on each raspberry pi zero. This won't have a UI, but will accept REST calls to perform some IR operations are described here 

3. **IR Controller (LIRC)** - After capturing the remote control codes, calls to the webapp will trigger these to be blasted from the IR emitter attached to the raspberry pi

![Diagram](https://i.imgur.com/HNisXjo.png)

## Project Idea

This project is based off this, but with a couple modications
https://www.instructables.com/id/Raspberry-Pi-Zero-Universal-Remote/

1. 
dtoverlay=gpio-ir,gpio_pin=22 #(without: in)
dtoverlay=gpio-ir-tx,gpio_pin=23 #(without: out)

2. 
mv /etc/lirc/lirc_options.conf.dist /etc/lirc/lirc_options.conf
mv /etc/lirc/lircd.conf.dist /etc/lirc/lircd.conf
mv /etc/lirc/lircd.conf.d/devinput.lircd.conf /etc/lirc/lircd.conf.d/devinput.lircd.dist

3.
In /etc/lirc/lirc_options.conf:
driver          = default
device          = /dev/lirc1
