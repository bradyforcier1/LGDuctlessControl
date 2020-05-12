# LGDuctlessControl

The purpose of this project is to control the LG Ductless HVAC system in my condo. Each zone has a remote, but I like the idea of being able to control all the zones at once. Especailly if I'm away, with a VPN setup, I could control the zones remotely.

## Components
1. **Master Webapp (Flask)** - This will run on my main server. Users have the ability to specify controls for the zones via UI. Things like on/off, temp control, and sleep time
  
2. **Client Webapp (Flask)** - This webapp will run on each raspberry pi zero. This won't have a UI, but will accept REST calls to perform some IR operations are described here 

3. **IR Controller (LIRC)** - After capturing the remote control codes, calls to the webapp will trigger these to be blasted from the IR emitter attached to the raspberry pi

![alt text](https://imgur.com/a/vdFaUodg "Diagram")
