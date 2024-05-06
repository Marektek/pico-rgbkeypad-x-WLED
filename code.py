import rgbkeypad
import socketpool
import ssl
import adafruit_requests 
import wifi
import time
from random import randint

#your wifi ssid/password
ssid = 'example:mikeswifi69'
password = 'example;123456789'
wifi.radio.connect(ssid,password)

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool)

keypad = rgbkeypad.RGBKeypad()

#Wled ip
ip="exaple:192.168.2.155"                                              


while True:
    for key in keypad.keys:
        if key.is_pressed():
            print("key", key.x, key.y, "pressed")
            
            if key.x==0 and key.y==0:
                print ("pressed")
                url=f"http://{ip}/win&A=127&FX=15"
                print (url)
                key.color = (255, 0, 0)
                requests.get(url)
                key.color = (0, 255, 0)
                time.sleep(1)
                key.color = (0, 0, 0) 
            if key.x==2 and key.y==3:
                print ("pressed")
                url=f"http://{ip}/win&&T=2"
                print (url)
                key.color = (255, 0, 0)
                requests.get(url)
                key.color = (0, 255, 0)
                time.sleep(1)
                key.color = (0, 0, 0)
            if key.x==1 and key.y==3:
                print ("pressed")
                url=f"http://{ip}/win&&RB"
                print (url)
                key.color = (255, 0, 0)
                requests.get(url)
                key.color = (0, 255, 0)
                time.sleep(1)
                key.color = (0, 0, 0)
            if key.x==1 and key.y==0:
                print ("pressed")
                url=f"http://{ip}/win&&FX=10"
                print (url)
                key.color = (255, 0, 0)
                requests.get(url)
                key.color = (0, 255, 0)
                time.sleep(1)
                key.color = (0, 0, 0)
            if key.x==2 and key.y==0:
                print ("pressed")
                url=f"http://{ip}/win&&FX=159"
                print (url)
                key.color = (255, 0, 0)
                requests.get(url)
                key.color = (0, 255, 0)
                time.sleep(1)
                key.color = (0, 0, 0)
            if key.x==3 and key.y==0:
                print ("pressed")
                url=f"http://{ip}/win&&FX=0"
                print (url)
                key.color = (255, 0, 0)
                requests.get(url)
                key.color = (0, 255, 0)
                time.sleep(1)
                key.color = (0, 0, 0)
            if key.x==0 and key.y==1:
                print ("pressed")
                url=f"http://{ip}/win&&FX=9"
                print (url)
                key.color = (255, 0, 0)
                requests.get(url)
                key.color = (0, 255, 0)
                time.sleep(1)
                key.color = (0, 0, 0)


            
