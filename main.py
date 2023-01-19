from gpiozero import RGBLED
from time import sleep
from bluedot.btcomm import BluetoothServer
from signal import pause

led = RGBLED(red=27, green=17, blue=22)

def leer(data):
    print(data)
    dato=data.strip()
    if 'R' in dato:
        led.color = (1, 0, 0) # full red
        sleep(1)
    if 'G' in dato:
        led.color = (0, 1, 0) # full green
        sleep(1)
    if 'B' in dato:
        led.color = (0, 0, 1) # full blue
        sleep(1)
    if 'C' in dato:
        led.color = (0, 1, 1) # cyan
        sleep(1)
    if 'M' in dato:
        led.color = (1, 0, 1) # magenta
        sleep(1)
    if 'Y' in dato:
        led.color = (1, 1, 0) # yellow
        sleep(1)
    if 'W' in dato:
        led.color = (1, 1, 1) # white
        sleep(1)
    if 'S' in dato:
        led.color = (0, 0, 0) # off
        sleep(1)
    if 'RA' in dato:
        led.color = (0, 1, 0) # full green
        sleep(1)
        led.color = (0, 0, 1) # full blue
        sleep(1)
        led.color = (1, 0, 1) # magenta
        sleep(1)
        led.color = (1, 1, 0) # yellow
        sleep(1)
        led.color = (0, 1, 1) # cyan
        sleep(1)
        led.color = (1, 1, 1) # white
        sleep(1)
        led.color = (0, 0, 0) # off
        sleep(1)       
print("Inicializando Servidor")
S = BluetoothServer(leer)

pause()