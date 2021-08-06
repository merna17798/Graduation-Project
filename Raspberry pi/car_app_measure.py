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
MAX30100_StartFlag = '1'
SPO2_Flag = '2'
HR_Flag = '3'
TempTip_StartFlag = '4'
TempTip_BodyFlag = '5'
TempTip_AmbFlag = '6'
TempRest_StartFlag = '7'
TempRest_BodyFlag = '8'
TempRest_AmbFlag = '9'

MAX30100_StartFlag_CHECK = 49
SPO2_Flag_CHECK = 50
HR_Flag_CHECK = 51
TempTip_StartFlag_CHECK = 52
TempTip_BodyFlag_CHECK = 53
TempTip_AmbFlag_CHECK = 54
TempRest_StartFlag_CHECK = 55
TempRest_BodyFlag_CHECK = 56
TempRest_AmbFlag_CHECK = 57

HR_Data = 0
SPO2_Data = 0
BodyTemp_Data = 0
AmbTemp_Data = 0
BodyRestTemp_Data = 0
AmbRestTemp_Data = 0
BG=0
d2=0
# mode=GPIO.getmode()
# 
# 
# Forward1=8
# Backward1=11
# Forward2=25
# Backward2=9
# sleeptime=1
# 
# Forward3=17
# Backward3=18
# Forward4=27
# Backward4=22
# 
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(Forward1,GPIO.OUT)
# GPIO.setup(Backward1,GPIO.OUT)
# GPIO.setup(Forward2,GPIO.OUT)
# GPIO.setup(Backward2,GPIO.OUT)
# GPIO.setup(Forward3,GPIO.OUT)
# GPIO.setup(Backward3,GPIO.OUT)
# GPIO.setup(Forward4,GPIO.OUT)
# GPIO.setup(Backward4,GPIO.OUT)
# GPIO.output(Forward1,GPIO.LOW)
# GPIO.output(Backward1,GPIO.LOW)
# GPIO.output(Forward2,GPIO.LOW)
# GPIO.output(Backward2,GPIO.LOW)
# GPIO.output(Forward3,GPIO.LOW)
# GPIO.output(Backward3,GPIO.LOW)
# GPIO.output(Forward4,GPIO.LOW)
# GPIO.output(Backward4,GPIO.LOW)
# 
# def backward():
# 
#     GPIO.output(Backward1,GPIO.HIGH)
#     GPIO.output(Forward1,GPIO.LOW)
#     GPIO.output(Backward2,GPIO.LOW)
#     GPIO.output(Forward2,GPIO.HIGH)
#     
#     GPIO.output(Backward3,GPIO.HIGH)
#     GPIO.output(Forward3,GPIO.LOW)
#     GPIO.output(Backward4,GPIO.LOW)
#     GPIO.output(Forward4,GPIO.HIGH)   
# def forward():
#     GPIO.output(Backward1,GPIO.LOW)
#     GPIO.output(Forward1,GPIO.HIGH)
#     GPIO.output(Backward2,GPIO.HIGH)
#     GPIO.output(Forward2,GPIO.LOW)
#     
#     GPIO.output(Backward3,GPIO.LOW)
#     GPIO.output(Forward3,GPIO.HIGH)
#     GPIO.output(Backward4,GPIO.HIGH)
#     GPIO.output(Forward4,GPIO.LOW)
#     
# def Rightf():
#     GPIO.output(Backward4,GPIO.HIGH)
#     GPIO.output(Forward4,GPIO.LOW)
#     GPIO.output(Backward1,GPIO.LOW)
#     GPIO.output(Forward1,GPIO.HIGH)
#     
# def Rightb():
#     GPIO.output(Backward4,GPIO.LOW)
#     GPIO.output(Forward4,GPIO.HIGH)
#     GPIO.output(Backward1,GPIO.HIGH)
#     GPIO.output(Forward1,GPIO.LOW)
#     
#     
# 
# def Leftf():
#     
#     GPIO.output(Backward3,GPIO.LOW)
#     GPIO.output(Forward3,GPIO.HIGH)
#     GPIO.output(Backward2,GPIO.HIGH)
#     GPIO.output(Forward2,GPIO.LOW)
#     
# def Leftb():
#     GPIO.output(Backward3,GPIO.HIGH)
#     GPIO.output(Forward3,GPIO.LOW)
#     GPIO.output(Backward2,GPIO.LOW)
#     GPIO.output(Forward2,GPIO.HIGH)
# def stop():
#     
#     GPIO.output(Backward1,GPIO.LOW)
#     GPIO.output(Forward1,GPIO.LOW)
#     
#     GPIO.output(Backward4,GPIO.LOW)
#     GPIO.output(Forward4,GPIO.LOW)
#     
#     GPIO.output(Backward2,GPIO.LOW)
#     GPIO.output(Forward2,GPIO.LOW)
#     
#     GPIO.output(Backward3,GPIO.LOW)
#     GPIO.output(Forward3,GPIO.LOW)
def MAX30100_CheckFlag(StartFlagMAX30,HR_DataFlagMAX30,SPO2_DataFlagMAX30,
                                   StartFlagCheckMAX30,HR_DataFlagCheckMAX30,SPO2_DataFlagCheckMAX30):
#     window_1=popup().alert_popup("Follow instructions","hr-spo2.jpeg")
    global HR_Data
    global SPO2_Data
    ser.write(StartFlagMAX30.encode())
#     f=f+1
    time.sleep(1)
    Recive_StartFlagMAX30=ser.read()
    Recive_StartFlagMAX30=int.from_bytes(Recive_StartFlagMAX30,byteorder='big')

    print('startflag=',Recive_StartFlagMAX30)
    if(Recive_StartFlagMAX30 == StartFlagCheckMAX30):
        print("ok")
        ser.write(HR_DataFlagMAX30.encode())
        time.sleep(1)
        Recive_HR_DataFlagMAX30 = ser.read()
        Recive_HR_DataFlagMAX30 = int.from_bytes(Recive_HR_DataFlagMAX30,byteorder='big')
        print('HRflag=',Recive_HR_DataFlagMAX30)
        time.sleep(1)
        HR_Data = ser.read()
        HR_Data = int.from_bytes(HR_Data,byteorder='big')
        print('HRdata=',HR_Data)
        if(Recive_HR_DataFlagMAX30 == HR_DataFlagCheckMAX30):
            print("yes")
            s=ser.write(SPO2_DataFlagMAX30.encode())
            time.sleep(1)
            Recive_SPO2_DataFlagMAX30 = ser.read()
            Recive_SPO2_DataFlagMAX30 = int.from_bytes(Recive_SPO2_DataFlagMAX30,byteorder='big')
            print('spo2flag=',Recive_SPO2_DataFlagMAX30)
            time.sleep(1)
            Recive_SPO2_DataFlagMAX30 = ser.read()
            Recive_SPO2_DataFlagMAX30 = int.from_bytes(Recive_SPO2_DataFlagMAX30,byteorder='big')
            print('spo2flaggg=',Recive_SPO2_DataFlagMAX30)
            time.sleep(1)
            SPO2_Data = ser.read()
            SPO2_Data = int.from_bytes(SPO2_Data,byteorder='big')
            print('spo2data=',SPO2_Data)
            if(Recive_SPO2_DataFlagMAX30 == SPO2_DataFlagCheckMAX30):
                print("done")
                
def TempTip_CheckFlag(StartFlagMAX90,BodyTemp_DataFlagMAX90,AmbTemp_DataFlagMAX90,
                                   StartFlagCheckMAX90,BodyTemp_DataFlagCheckMAX90,AmbTemp_DataFlagCheckMAX90):
#     window_3=popup().alert_popup("Follow instructions","temp.jpeg")
    global BodyTemp_Data
    global AmbTemp_Data
    ser.write(StartFlagMAX90.encode())
#     f=f+1
    time.sleep(1)
    Recive_StartFlagMAX90=ser.read()
    Recive_StartFlagMAX90=int.from_bytes(Recive_StartFlagMAX90,byteorder='big')
#
#     f1=ord (recive)
#     print(recive)
    print('startflagtemp=',Recive_StartFlagMAX90)
    if(Recive_StartFlagMAX90 == StartFlagCheckMAX90):
        print("ok")
        ser.write(BodyTemp_DataFlagMAX90.encode())
        time.sleep(1)
        Recive_BodyTemp_DataFlagMAX90 = ser.read()
        Recive_BodyTemp_DataFlagMAX90 = int.from_bytes(Recive_BodyTemp_DataFlagMAX90,byteorder='big')
        print('bodytempflag=',Recive_BodyTemp_DataFlagMAX90)
        time.sleep(1)
        BodyTemp_Data = ser.read()
        BodyTemp_Data = int.from_bytes(BodyTemp_Data,byteorder='big')
        print('BODYTEMPdata=',BodyTemp_Data)
        if(Recive_BodyTemp_DataFlagMAX90 == BodyTemp_DataFlagCheckMAX90):
            print("yes")
            s=ser.write(AmbTemp_DataFlagMAX90.encode())
            time.sleep(1)
            Recive_AmbTemp_DataFlagMAX90 = ser.read()
            Recive_AmbTemp_DataFlagMAX90 = int.from_bytes(Recive_AmbTemp_DataFlagMAX90,byteorder='big')
            print('AMBTEMPflag=',Recive_AmbTemp_DataFlagMAX90)
            time.sleep(1)
            Recive_AmbTemp_DataFlagMAX90 = ser.read()
            Recive_AmbTemp_DataFlagMAX90 = int.from_bytes(Recive_AmbTemp_DataFlagMAX90,byteorder='big')
            print('AMBTEMPflag=',Recive_AmbTemp_DataFlagMAX90)
            time.sleep(1)
            AmbTemp_Data = ser.read()
            AmbTemp_Data = int.from_bytes(AmbTemp_Data,byteorder='big')
            print('AMBTEMPdata=',AmbTemp_Data)
            if(Recive_AmbTemp_DataFlagMAX90 == AmbTemp_DataFlagCheckMAX90):
                print("done")

def TempRest_CheckFlag(StartFlagMAX90,BodyTemp_DataFlagMAX90,AmbTemp_DataFlagMAX90,
                                   StartFlagCheckMAX90,BodyTemp_DataFlagCheckMAX90,AmbTemp_DataFlagCheckMAX90):
    global BodyRestTemp_Data
    global AmbRestTemp_Data
    ser.write(StartFlagMAX90.encode())
#     f=f+1
    time.sleep(1)
    Recive_StartFlagMAX90=ser.read()
    Recive_StartFlagMAX90=int.from_bytes(Recive_StartFlagMAX90,byteorder='big')
#
#     f1=ord (recive)
#     print(recive)
    print('startflagtemprest=',Recive_StartFlagMAX90)
    if(Recive_StartFlagMAX90 == StartFlagCheckMAX90):
        print("ok")
        ser.write(BodyTemp_DataFlagMAX90.encode())
        time.sleep(1)
        Recive_BodyTemp_DataFlagMAX90 = ser.read()
        Recive_BodyTemp_DataFlagMAX90 = int.from_bytes(Recive_BodyTemp_DataFlagMAX90,byteorder='big')
        print('bodytempflagrest=',Recive_BodyTemp_DataFlagMAX90)
        time.sleep(1)
        BodyRestTemp_Data = ser.read()
        BodyRestTemp_Data = int.from_bytes(BodyRestTemp_Data,byteorder='big')
        print('BODYTEMPdatarest=',BodyRestTemp_Data)
        if(Recive_BodyTemp_DataFlagMAX90 == BodyTemp_DataFlagCheckMAX90):
            print("yes")
            s=ser.write(AmbTemp_DataFlagMAX90.encode())
            time.sleep(1)
            Recive_AmbTemp_DataFlagMAX90 = ser.read()
            Recive_AmbTemp_DataFlagMAX90 = int.from_bytes(Recive_AmbTemp_DataFlagMAX90,byteorder='big')
            print('AMBTEMPflagrest=',Recive_AmbTemp_DataFlagMAX90)
            time.sleep(1)
            Recive_AmbTemp_DataFlagMAX90 = ser.read()
            Recive_AmbTemp_DataFlagMAX90 = int.from_bytes(Recive_AmbTemp_DataFlagMAX90,byteorder='big')
            print('AMBTEMPflagrest=',Recive_AmbTemp_DataFlagMAX90)
            time.sleep(1)
            AmbRestTemp_Data = ser.read()
            AmbRestTemp_Data = int.from_bytes(AmbRestTemp_Data,byteorder='big')
            print('AMBTEMPdatarest=',AmbRestTemp_Data)
            if(Recive_AmbTemp_DataFlagMAX90 == AmbTemp_DataFlagCheckMAX90):
                print("done")
def blood_glucose(BodyTemp_Data,BodyRestTemp_Data,AmbRestTemp_Data):
    global BG
    BG=Estimate_BloodGlucose(patient_id,BodyTemp_Data,AmbTemp_Data,BodyTemp_Data,BodyRestTemp_Data)

def update(n,temp_tip,hr,spo2,bg):
    x.update({"patientid": n}) #patient id based on what visit you are in 
    #read sensor data then for example
    
    temperature=temp_tip
    heartrate=hr
    spo=spo2
    x.update({"bloodglucose": bg})
    if(temperature>=27 & temperature<= 55):
        x.update({"temprature": temperature-13})
    if(heartrate>=40 & heartrate<=200):    
        x.update({"heartrate": heartrate})
    if(spo>=80 & spo<=100):
        x.update({"spo": spo})
    ## covert dictionary to json object 
    sorted_string = json.dumps(x, indent=4, sort_keys=True)
    #requesting API
    url="http://192.168.43.198/LoginRegister/update_VS.php"
    r = requests.post(url, json=x)
    #only print the response
    print(r.text)
# ctrCmd = [b'forward',b'backward',b'right',b'left',b'start',b'stop']
# 
# HOST = '10.10.10.40'
# PORT = 8000
# BUFSIZE = 1024
# ADDR = (HOST,PORT)
# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)
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
            window_0=popup().alert_popup("welcome","welcome.jpeg")
            window_1=popup().alert_popup("Follow instructions","hr-spo2.jpeg")

            for i in range(5):
                MAX30100_CheckFlag(MAX30100_StartFlag,SPO2_Flag,HR_Flag,
                                   MAX30100_StartFlag_CHECK,SPO2_Flag_CHECK,HR_Flag_CHECK)
                print(BodyTemp_Data-13,HR_Data,SPO2_Data,BG)
                update(patient_id,BodyTemp_Data,HR_Data,SPO2_Data,BG)
                
            window_3=popup().alert_popup("Follow instructions","temp.jpeg")
            for i in range(5):
                TempTip_CheckFlag(TempTip_StartFlag,TempTip_BodyFlag,TempTip_AmbFlag,
                                   TempTip_StartFlag_CHECK,TempTip_BodyFlag_CHECK,TempTip_AmbFlag_CHECK)
                
                
                print(BodyTemp_Data,HR_Data,SPO2_Data,BG)
                update(patient_id,BodyTemp_Data,HR_Data,SPO2_Data,BG)
                 
            window_3=popup().alert_popup("Follow instructions","temp.jpeg")
            for i in range(5):
                TempRest_CheckFlag(TempRest_StartFlag,TempRest_BodyFlag,TempRest_AmbFlag,TempRest_StartFlag_CHECK,TempRest_BodyFlag_CHECK,TempRest_AmbFlag_CHECK)
                blood_glucose(BodyTemp_Data-15,BodyRestTemp_Data,AmbRestTemp_Data)
                print(BodyTemp_Data,HR_Data,SPO2_Data,BG)
                update(patient_id,BodyTemp_Data,HR_Data,SPO2_Data,BG)
                 
            y=1
                            


