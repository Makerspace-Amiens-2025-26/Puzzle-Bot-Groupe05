#!/usr/bin/python3

# ============================================
# code is placed under the MIT license
#  Copyright (c) 2023 J-M-L
#  For the Arduino Forum : https://forum.arduino.cc/u/j-m-l
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#  ===============================================


import sys, threading, queue, serial, math
import cv2
import numpy as np
import serial.tools.list_ports

baudRate = 115200
arduinoQueue = queue.Queue()
localQueue = queue.Queue()

def detectAruco():
    # Initialize webcam (0 = default camera)
    cam = cv2.VideoCapture(0)

    # Capture one frame
    ret, frame = cam.read()

    cam.release()

    # Load the image
    image = cv2.imread('captured_image.png')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
    parameters = cv2.aruco.DetectorParameters()

    # Create the ArUco detector
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
    # Detect the markers
    corners, ids, rejected = detector.detectMarkers(gray)
    # Print the detected markers
    print("Detected markers:", ids)
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(image, corners, ids)
        for e in zip(corners,ids):
            x1, y1 = e[0][0][0]
            x2, y2 = e[0][0][2]
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            image = cv2.circle(image, (int(x),int(y)), radius=2, color=(0, 0, 255), thickness=-1)
            handleLocalMessage(str(math.floor(x) ))
            handleLocalMessage(str(math.floor(y)))
            

def selectArduino():
    ports = serial.tools.list_ports.comports()
    choices = []
    print('PORT\tDEVICE\t\t\tMANUFACTURER')
    for index,value in enumerate(sorted(ports)):
        if (value.hwid != 'n/a'):
            choices.append(index)
            print(index, '\t', value.name, '\t', value.manufacturer) # https://pyserial.readthedocs.io/en/latest/tools.html#serial.tools.list_ports.ListPortInfo

    choice = -1
    while choice not in choices:
        answer = input("➜ Select your port: ")
        if answer.isnumeric() and int(answer) <= int(max(choices)):
            choice = int(answer)
    print('selecting: ', ports[choice].device)
    return ports[choice].device


def listenToArduino():
    message = b''
    while True:
        incoming = arduino.read()
        if (incoming == b'\n'):
            arduinoQueue.put(message.decode('utf-8').strip().upper())
            message = b''
        else:
            if ((incoming != b'') and (incoming != b'\r')):
                 message += incoming

def listenToLocal():
    while True:
        command = sys.stdin.readline().strip().upper()
        localQueue.put(command)

def configureUserInput():
    localThread = threading.Thread(target=listenToLocal, args=())
    localThread.daemon = True
    localThread.start()


def configureArduino():
    global arduinoPort
    arduinoPort = selectArduino()
    global arduino
    arduino = serial.Serial(arduinoPort, baudrate=baudRate, timeout=.1)
    arduinoThread = threading.Thread(target=listenToArduino, args=())
    arduinoThread.daemon = True
    arduinoThread.start()

# ---- CALLBACKS UPON MESSAGES -----

def handleLocalMessage(aMessage):
    print("=> [" + aMessage + "]")
    arduino.write(aMessage.encode('utf-8'))
    arduino.write(bytes('\n', encoding='utf-8'))

def handleArduinoMessage(aMessage):
    print("<= [" + aMessage + "]")

# ---- MAIN CODE -----

configureArduino()                                      # will reboot AVR based Arduinos
configureUserInput()                                    # handle stdin 

print("Waiting for Arduino")

# --- A good practice would be to wait for a know message from the Arduino
# for example at the end of the setup() the Arduino could send "OK"
while True:
    if not arduinoQueue.empty():
        if arduinoQueue.get() == "OK":
            break
print("Arduino Ready")

# --- Now you handle the commands received either from Arduino or stdin
while True:
    if not arduinoQueue.empty():
        if arduinoQueue.get() == "TAKE_PIC":
            detectAruco()
        else:
            handleArduinoMessage(arduinoQueue.get())

    if not localQueue.empty():
        handleLocalMessage(localQueue.get())