import network
import urequests as requests
from machine import Pin
from time import sleep

print("Inicializando o módulo wifi")

PinLed = Pin(2, Pin.OUT, value=0)

print("Conectando na rede...")

station = network.WLAN(network.STA_IF)
station.active(False)
sleep(1)
station.active(True)
sleep(1)
station.connect('meuwifo', 'kkkkeaimen')
while(not station.isconnected()):
    pass



print("Conectou!")

def SendDir(direction):
    r = requests.get(
                        "http://192.168.39.35:8000/esp_route",
                        json={ "move": direction }
                     )
    print(r.status_code, r.text)
    r.close()



print("Inicializando pinos")

botForward  = Pin(16, Pin.IN, Pin.PULL_UP)
botBackward = Pin(17, Pin.IN, Pin.PULL_UP)
botRight    = Pin(18, Pin.IN, Pin.PULL_UP)
botLeft     = Pin(19, Pin.IN, Pin.PULL_UP)
botTiltL    = Pin(21, Pin.IN, Pin.PULL_UP)
botTiltR    = Pin(22, Pin.IN, Pin.PULL_UP)
botTiltF    = Pin(23, Pin.IN, Pin.PULL_UP)
botTiltB    = Pin(25, Pin.IN, Pin.PULL_UP)
botStop     = Pin(26, Pin.IN, Pin.PULL_UP)
botDance    = Pin(27, Pin.IN, Pin.PULL_UP)


print("Inicio do loop infinito")
PinLed.on()
gc.enable()
gc.collect()
while (True):
    if   not botForward.value():
        print('Forward')
        SendDir('Forward')
        gc.collect()
    elif not botBackward.value():
        print('Backward')
        SendDir('Backward')
        gc.collect()
    elif not botRight.value():
        print('Right')
        SendDir('Right')
        gc.collect()
    elif not botLeft.value():
        print('Left')
        SendDir('Left')
        gc.collect()
    elif not botTiltL.value():
        print('TiltL')
        SendDir('TiltL')
        gc.collect()
    elif not botTiltR.value():
        print('TiltR')
        SendDir('TiltR')
        gc.collect()
    elif not botTiltF.value():
        print('TiltF')
        SendDir('TiltF')
        gc.collect()
    elif not botTiltB.value():
        print('TiltB')
        SendDir('TiltB')
        gc.collect()
    elif not botStop.value():
        print('Stop')
        SendDir('Stop')
        gc.collect()
    elif not botDance.value():
        print('Dance')
        SendDir('Dance')
        gc.collect()









