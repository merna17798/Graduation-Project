import RPi.GPIO as GPIO
from socket import *

ctrCmd = [b'forward',b'backward',b'right',b'left',b'start',b'stop']

HOST = '192.168.43.121'
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST,PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

mode=GPIO.getmode()
        
mode=GPIO.getmode()


Forward1=8
Backward1=11
Forward2=25
Backward2=9
sleeptime=1

Forward3=17
Backward3=18
Forward4=27
Backward4=22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Forward1,GPIO.OUT)
GPIO.setup(Backward1,GPIO.OUT)
GPIO.output(Forward1,GPIO.LOW)
GPIO.output(Backward1,GPIO.LOW)
GPIO.setup(Forward2,GPIO.OUT)
GPIO.setup(Backward2,GPIO.OUT)
GPIO.output(Forward2,GPIO.LOW)
GPIO.output(Backward2,GPIO.LOW)
GPIO.setup(Forward3,GPIO.OUT)
GPIO.setup(Backward3,GPIO.OUT)
GPIO.output(Forward3,GPIO.LOW)
GPIO.output(Backward3,GPIO.LOW)
GPIO.setup(Forward4,GPIO.OUT)
GPIO.setup(Backward4,GPIO.OUT)
GPIO.output(Forward4,GPIO.LOW)
GPIO.output(Backward4,GPIO.LOW)

def forward():

    GPIO.output(Backward1,GPIO.HIGH)
    GPIO.output(Forward1,GPIO.LOW)
    GPIO.output(Backward2,GPIO.HIGH)
    GPIO.output(Forward2,GPIO.LOW)
    
    GPIO.output(Backward3,GPIO.LOW)
    GPIO.output(Forward3,GPIO.HIGH)
    GPIO.output(Backward4,GPIO.LOW)
    GPIO.output(Forward4,GPIO.HIGH)   
def backward():
    GPIO.output(Backward1,GPIO.LOW)
    GPIO.output(Forward1,GPIO.HIGH)
    GPIO.output(Backward2,GPIO.LOW)
    GPIO.output(Forward2,GPIO.HIGH)
    
    GPIO.output(Backward3,GPIO.HIGH)
    GPIO.output(Forward3,GPIO.LOW)
    GPIO.output(Backward4,GPIO.HIGH)
    GPIO.output(Forward4,GPIO.LOW)
    
def Leftb():
    GPIO.output(Backward4,GPIO.HIGH)
    GPIO.output(Forward4,GPIO.LOW)
    GPIO.output(Backward1,GPIO.LOW)
    GPIO.output(Forward1,GPIO.HIGH)
    
def Leftf():
    GPIO.output(Backward4,GPIO.LOW)
    GPIO.output(Forward4,GPIO.HIGH)
    GPIO.output(Backward1,GPIO.HIGH)
    GPIO.output(Forward1,GPIO.LOW)
    
    

def Rightf():
    
    GPIO.output(Backward3,GPIO.LOW)
    GPIO.output(Forward3,GPIO.HIGH)
    GPIO.output(Backward2,GPIO.HIGH)
    GPIO.output(Forward2,GPIO.LOW)
    
def Rightb():
    GPIO.output(Backward3,GPIO.HIGH)
    GPIO.output(Forward3,GPIO.LOW)
    GPIO.output(Backward2,GPIO.LOW)
    GPIO.output(Forward2,GPIO.HIGH)
def stop():
    
    GPIO.output(Backward1,GPIO.LOW)
    GPIO.output(Forward1,GPIO.LOW)
    
    GPIO.output(Backward4,GPIO.LOW)
    GPIO.output(Forward4,GPIO.LOW)
    
    GPIO.output(Backward2,GPIO.LOW)
    GPIO.output(Forward2,GPIO.LOW)
    
    GPIO.output(Backward3,GPIO.LOW)
    GPIO.output(Forward3,GPIO.LOW)   