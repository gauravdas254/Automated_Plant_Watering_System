import serial
import time
import threading
#COMMANDS
get_Sml = '11'
get_Wl = '12'
set_Motor_On = '21'
set_Motor_Off = '22'
set_Buzz_On = '23'
set_Buzz_Off = '24'
#REQUIRED THRESHOLDS
reqSml = 700
reqWl = 400
#DELAYS
buzzDelay = 1
motorDelay = 1
sleepDelay = 10
cdDelay = 2
checkDelay = 10
#CONDITIONAL VALUES
wlWarning = 0
watered = 0
buzzOnce = 0

arduino_serial = serial.Serial(port="/dev/ttyAMA0", baudrate=9600, timeout=.1)
arduino_serial.flush()

def getSml():
    arduino_serial.write(bytes(get_Sml, 'utf-8'))
    time.sleep(cdDelay)
    if arduino_serial.in_waiting > 0:
        smVal = int(arduino_serial.readline().decode('utf-8').rstrip())
        return smVal

def getWl():
    arduino_serial.write(bytes(get_Wl, 'utf-8'))
    time.sleep(cdDelay)
    if arduino_serial.in_waiting > 0:
        wlVal = int(arduino_serial.readline().decode('utf-8').rstrip())
        return wlVal

def setMotorOn():
    arduino_serial.write(bytes(set_Motor_On, 'utf-8'))
    time.sleep(cdDelay)
    if arduino_serial.in_waiting > 0:
        ackMon = arduino_serial.readline().decode('utf-8').rstrip()
        print(ackMon)

def setMotorOff():
    arduino_serial.write(bytes(set_Motor_Off, 'utf-8'))
    time.sleep(cdDelay)
    if arduino_serial.in_waiting > 0:
        ackMoff = arduino_serial.readline().decode('utf-8').rstrip()
        print(ackMoff)

def setBuzzOn():
    arduino_serial.write(bytes(set_Buzz_On, 'utf-8'))
    time.sleep(cdDelay)
    if arduino_serial.in_waiting > 0:
        ackBon = arduino_serial.readline().decode('utf-8').rstrip()
        print(ackBon)

def setBuzzOff():
    arduino_serial.write(bytes(set_Buzz_Off, 'utf-8'))
    time.sleep(cdDelay)
    if arduino_serial.in_waiting > 0:
        ackBoff = arduino_serial.readline().decode('utf-8').rstrip()
        print(ackBoff)

def saveSml(sml):
    f = open("/home/pi/Desktop/APWS/data/sml.txt", "w")
    f.write(sml)
    f.close()
    f = open("/home/pi/Desktop/APWS/data/sml_perm.txt", "w")
    f.write(sml)
    f.close()

def saveWl(wl):
    f = open("/home/pi/Desktop/APWS/data/wl.txt", "w")
    f.write(wl)
    f.close()
    f = open("/home/pi/Desktop/APWS/data/wl_perm.txt", "w")
    f.write(wl)
    f.close()

def readSml():
    f = open("/home/pi/Desktop/APWS/data/sml.txt")
    soilMoisture = f.read()
    f.close()
    return soilMoisture

def readWl():
    f = open("/home/pi/Desktop/APWS/data/wl.txt")
    waterLevel = f.read()
    f.close()
    return waterLevel

def apws(reqSml, longSleep):
    smVal = getSml()
    wlVal = getWl()
    saveSml(str((smVal)))
    saveWl(str(wlVal))
    if smVal>=reqSml:
        if wlVal>reqWl:
            setMotorOn()
            time.sleep(motorDelay)
            setMotorOff()
            return "plantWatered"
        else:
            for i in range(3):
                setBuzzOn()
                setBuzzOff()
            return "noWater"
