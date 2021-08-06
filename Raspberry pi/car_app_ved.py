from socket import *      
import numpy as np
import RPi.GPIO as GPIO
import time
import serial
import subprocess
import webbrowser, os, sys
from imutils.video import VideoStream
import requests
import json
# import out_home
from image import popup
from motorapp import *
from BG_Estimation import *
# new_out=out_home.out
# patient_id=new_out[0][0]
patient_id=5
##initial dictionary
x = {'patientid':0 , 'heartrate':0, 'temprature':0 ,'spo':0, 'bloodglucose':0}
ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

y=0
while True:
    if y==1:
        break
    print ('Waiting for connection')
    tcpCliSock,addr = tcpSerSock.accept()
    print ('...connected from :', addr)
    
    while True:
        
        data = ''
        data = tcpCliSock.recv(BUFSIZE)
        print(data)
        if not data:
                break
        elif data == ctrCmd[4]:
            picam = VideoStream(usePiCamera=False).stop()
            subprocess.run(['sudo service motion start'], shell=True)

        elif data == ctrCmd[0]:
            forward()
            time.sleep(1)
            stop()
            time.sleep(2)
            print ('forward')

        elif data == ctrCmd[2]:
            Rightf()
            time.sleep(1)
            stop()
            time.sleep(2)
            data = ''
            print ('right')
        elif data == ctrCmd[3]:
            Leftf()
            time.sleep(1)
            stop()
            time.sleep(2)
            data = ''
            print ('left')
        elif data == ctrCmd[5]:
            stop()
            subprocess.run(['sudo service motion stop'], shell=True)
            url = "https://meet.jit.si/vidoeconfforgrandma#config.prejoinPageEnabled=false"
            #webcam = VideoStream(src=0).start()
            picam = VideoStream(usePiCamera=False).stop()
            chrome_path = '/usr/lib/chromium-browser/chromium-browser'
            webbrowser.get(chrome_path).open(url)
            # if():
            x=0
            for i in range (4):

                time.sleep(30)
                if(x==1):
                    subprocess.run(['pkill chromium'], shell=True)
                print("mm")
                if(i==2):
                    x=1
            y=1
                            
