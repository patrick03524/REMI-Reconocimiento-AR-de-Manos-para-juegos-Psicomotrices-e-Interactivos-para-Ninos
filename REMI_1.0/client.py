import socket
import threading
import cv2
import time
import os
import HandTrackingModule as htm

import random
import simpleaudio as sa
import cvzone

import time

username = input("Enter your username: ")

host = '127.0.0.1'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

wCam, hCam = 1280, 500
dim = (wCam, hCam)

cap = 0

if(username=='user1'):
    cap = cv2.VideoCapture(2)
if(username=='user2'):
    cap = cv2.VideoCapture(3)
if(username=='user3'):
    cap = cv2.VideoCapture(1)

cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0.75,maxHands=1)

tipIds = [4, 8, 12, 16, 20]

last_value = 0
temp_last = 0

suma_obj = 5

puntos = 0
cantPuntos = 50
totalPos = puntos * cantPuntos
posBar = 550 - totalPos

verificarLocal = "no"
verificarMulti = "no"

filename = 'pop.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)

def HPVocales2():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][1] > 0 and lmList[8][1] < 500):
                aux = 1

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        HPVocales()
                    permite = False

            totalFingers = fingers.count(1)

        imagen = cv2.imread('vocales2.png', cv2.IMREAD_UNCHANGED)

        cv2.rectangle(img, (43, 30), (285, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (98, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        imgResult = cvzone.overlayPNG(img, imagen, [60, 110])

        cv2.imshow("Image", imgResult)
        cv2.waitKey(1)

def HPVocales():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][1] > 0 and lmList[8][1] < 500):
                aux = 1
            if (lmList[8][1] > 500 and lmList[8][1] < 999):
                aux = 2

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        VocalesDesorden()
                    if (aux == 2):
                        wave_obj.play()
                        HPVocales2()
                    permite = False

            totalFingers = fingers.count(1)

        imagen = cv2.imread('vocales1.png', cv2.IMREAD_UNCHANGED)

        cv2.rectangle(img, (43, 30), (285, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (98, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (673, 30), (915, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Siguiente', (680, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        imgResult = cvzone.overlayPNG(img, imagen, [60, 110])

        cv2.imshow("Image", imgResult)
        cv2.waitKey(1)

def HPDedos2():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][1] > 0 and lmList[8][1] < 500):
                aux = 1

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        HPDedos()
                    permite = False

            totalFingers = fingers.count(1)

        imagen = cv2.imread('dedos2.png', cv2.IMREAD_UNCHANGED)

        cv2.rectangle(img, (43, 30), (285, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (98, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        imgResult = cvzone.overlayPNG(img, imagen, [70, 100])

        cv2.imshow("Image", imgResult)
        cv2.waitKey(1)

def HPDedos():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][1] > 0 and lmList[8][1] < 500):
                aux = 1
            if (lmList[8][1] > 500 and lmList[8][1] < 999):
                aux = 2

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        SumaDedos()
                    if (aux == 2):
                        wave_obj.play()
                        HPDedos2()
                    permite = False

            totalFingers = fingers.count(1)

        imagen = cv2.imread('dedos1.png', cv2.IMREAD_UNCHANGED)

        cv2.rectangle(img, (43, 30), (285, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (98, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (673, 30), (915, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Siguiente', (680, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        imgResult = cvzone.overlayPNG(img, imagen, [70, 100])

        cv2.imshow("Image", imgResult)
        cv2.waitKey(1)

def SumaDedos():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        ModeSumaDedos()
                    if (aux == 2):
                        wave_obj.play()
                        HPDedos()
                    if (aux == 3):
                        wave_obj.play()
                        menu()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'SUMA DE DEDOS', (235, 150), cv2.FONT_HERSHEY_PLAIN, 4, (219, 152, 52), 6)

        cv2.rectangle(img, (350, 300), (650, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Jugar', (440, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (330, 400), (670, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Como Jugar', (350, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Menu', (445, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def VocalesDesorden():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        ModeVocalesDesorden()
                    if (aux == 2):
                        wave_obj.play()
                        HPVocales()
                    if (aux == 3):
                        wave_obj.play()
                        menu()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'SILABAS EN DESORDEN', (100, 150), cv2.FONT_HERSHEY_PLAIN, 4, (219, 152, 52), 6)

        cv2.rectangle(img, (350, 300), (650, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Jugar', (440, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (330, 400), (670, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Como Jugar', (350, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Menu', (445, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def ModeSumaDedos():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        juegoDEDOS()
                    if (aux == 2):
                        wave_obj.play()
                        juegoDEDOScoop()
                    if (aux == 3):
                        wave_obj.play()
                        SumaDedos()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'SUMA DE DEDOS', (235, 150), cv2.FONT_HERSHEY_PLAIN, 4, (219, 152, 52), 6)

        cv2.rectangle(img, (350, 300), (650, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Individual', (393, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (330, 400), (670, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Cooperativo', (355, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (440, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def ModeVocalesDesorden():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        juegoVOCALES()
                    if (aux == 2):
                        wave_obj.play()
                        juegoVOCALEScoop()
                    if (aux == 3):
                        wave_obj.play()
                        VocalesDesorden()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'SILABAS EN DESORDEN', (100, 150), cv2.FONT_HERSHEY_PLAIN, 4, (219, 152, 52), 6)

        cv2.rectangle(img, (350, 300), (650, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Individual', (393, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (330, 400), (670, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Cooperativo', (355, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (440, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def iniciar():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        SumaDedos()
                    if (aux == 2):
                        wave_obj.play()
                        VocalesDesorden()
                    if (aux == 3):
                        wave_obj.play()
                        menu()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'REMI', (285, 180), cv2.FONT_HERSHEY_PLAIN, 12, (219, 152, 52), 25)

        cv2.rectangle(img, (280, 300), (720, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Suma de Dedos', (305, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (230, 400), (770, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Silabas en Desorden', (250, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (440, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def creditos():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 1

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        menu()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'REMI', (285, 180), cv2.FONT_HERSHEY_PLAIN, 12, (219, 152, 52), 25)

        cv2.putText(img, f'Oscar Mendoza', (300, 280), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)
        cv2.putText(img, f'Patrick Marquez', (285, 330), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)
        cv2.putText(img, f'Inigo Diez Canseco', (245, 380), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (440, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def menu():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if(aux == 1):
                        wave_obj.play()
                        iniciar()
                    if(aux == 2):
                        wave_obj.play()
                        creditos()
                    if(aux == 3):
                        wave_obj.play()
                        #cv2.destroyAllWindows()
                        #exit(1)
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'REMI', (285, 180), cv2.FONT_HERSHEY_PLAIN, 12, (219, 152, 52), 25)

        cv2.rectangle(img, (350, 300), (650, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Iniciar', (435, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 400), (650, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Creditos', (400, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Salir', (440, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def juegoVOCALES():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    pTime = 0

    grosorSilaba1 = 4
    grosorSilaba2 = 4
    grosorSilaba3 = 4
    grosorSilaba4 = 4

    arrPalabras = ['CASA', 'SAPO', 'CAMA', 'PATO', 'PECERA', 'GORILA']
    arrSilabas = ['CA', 'SA', 'PO', 'MA', 'PA', 'TO', 'PE', 'CE', 'RA', 'GO', 'RI', 'LA', 'SI', 'RO', 'CO']
    arrIndex = [[1, 13, 7, 0], [2, 8, 1, 10], [14, 3, 0, 11], [5, 4, 9, 6], [7, 12, 8, 6], [11, 10, 6, 9]]

    aleatorio = random.randint(0, 5)
    palabraObjetivo = arrPalabras[aleatorio]

    palabra = ''

    aux = ''
    permite = True

    bool = 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)

            if (lmList[8][2] == 180 or lmList[8][2] == 175 or lmList[8][2] == 170 or lmList[8][2] == 185 or lmList[8][
                2] == 190):
                aux = arrSilabas[arrIndex[aleatorio][0]]
                grosorSilaba1 = 6
                grosorSilaba2 = 4
                grosorSilaba3 = 4
                grosorSilaba4 = 4

            if (lmList[8][2] == 280 or lmList[8][2] == 275 or lmList[8][2] == 270 or lmList[8][2] == 285 or lmList[8][
                2] == 290):
                aux = arrSilabas[arrIndex[aleatorio][1]]
                grosorSilaba1 = 4
                grosorSilaba2 = 6
                grosorSilaba3 = 4
                grosorSilaba4 = 4

            if (lmList[8][2] == 380 or lmList[8][2] == 375 or lmList[8][2] == 370 or lmList[8][2] == 385 or lmList[8][
                2] == 390):
                aux = arrSilabas[arrIndex[aleatorio][2]]
                grosorSilaba1 = 4
                grosorSilaba2 = 4
                grosorSilaba3 = 6
                grosorSilaba4 = 4

            if (lmList[8][2] == 480 or lmList[8][2] == 475 or lmList[8][2] == 470 or lmList[8][2] == 485 or lmList[8][
                2] == 490):
                aux = arrSilabas[arrIndex[aleatorio][3]]
                grosorSilaba1 = 4
                grosorSilaba2 = 4
                grosorSilaba3 = 4
                grosorSilaba4 = 6

            if (lmList[8][2] > 10 and lmList[8][2] < 60 and totalFingers == 2):
                wave_obj.play()
                VocalesDesorden()

            # print(lmList[8])

            # print(fingers)

            if (totalFingers != 0 and totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    palabra += aux
                    permite = False

            if (palabraObjetivo == palabra):
                cv2.putText(img, f'BIEN HECHO!', (300, 350), cv2.FONT_HERSHEY_PLAIN, 5, (45, 200, 235), 5)

            if (totalFingers == 0):
                if (permite == True):
                    palabra = palabra[:-2]
                    permite = False

            if (totalFingers == 5):
                palabra = ''
                aleatorio = random.randint(0, 5)
                palabraObjetivo = arrPalabras[aleatorio]

        # h, w, c = overlayList[totalFingers - 1].shape
        # img[0:h, 0:w] = overlayList[totalFingers - 1]

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, f'FPS: {int(fps)}', (750, 675), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, f'OBJETIVO: {str(palabraObjetivo)}', (200, 100), cv2.FONT_HERSHEY_PLAIN, 4, (84, 153, 34), 6)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][0]])}', (70, 200), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), grosorSilaba1)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][1]])}', (70, 300), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), grosorSilaba2)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][2]])}', (70, 400), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), grosorSilaba3)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][3]])}', (70, 500), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), grosorSilaba4)
        cv2.putText(img, f'{str(palabra)}', (340, 600), cv2.FONT_HERSHEY_PLAIN, 5, (15, 196, 241), 5)

        cv2.rectangle(img, (800, 10), (950, 60), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Salir', (823, 50), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def juegoDEDOS():
    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    cap.set(3, wCam)
    cap.set(4, hCam)

    pTime = 0

    last_value = 0
    temp_last = 0

    suma_obj = random.randint(1, 5)

    totalFingers = 0
    bool = 0
    permite = False

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # print(fingers)
            totalFingers = fingers.count(1)

            if totalFingers == 0:
                last_value += temp_last
            temp_last = totalFingers

            if (lmList[8][2] > 10 and lmList[8][2] < 60 and totalFingers == 2):
                wave_obj.play()
                SumaDedos()

        if suma_obj == last_value:
            cv2.putText(img, f'BIEN HECHO!', (300, 400), cv2.FONT_HERSHEY_PLAIN, 5, (45, 200, 235), 5)

        if suma_obj < last_value:
            cv2.putText(img, f'UPS! TE ESTAS PASANDO', (240, 400), cv2.FONT_HERSHEY_PLAIN, 3, (6, 111, 229), 3)

        print('Valor Acumulado: ', last_value)
        print('Valor Actual: ', totalFingers)

        h, w, c = overlayList[totalFingers - 1].shape
        img[0:h, 0:w] = overlayList[totalFingers - 1]

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, f'FPS: {int(fps)}', (750, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, f'SUMA: {int(last_value)}', (400, 675), cv2.FONT_HERSHEY_PLAIN, 3, (43, 201, 72), 3)
        cv2.putText(img, f'OBJETIVO: {int(suma_obj)}', (355, 70), cv2.FONT_HERSHEY_PLAIN, 3, (24, 24, 156), 3)

        cv2.rectangle(img, (800, 10), (950, 60), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Salir', (823, 50), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def juegoVOCALEScoop():
    global puntos
    global cantPuntos
    global totalPos
    global posBar
    global verificarLocal
    global verificarMulti

    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    verificarMulti = "si"

    cap.set(3, wCam)
    cap.set(4, hCam)

    pTime = 0

    grosorSilaba1 = 4
    grosorSilaba2 = 4
    grosorSilaba3 = 4
    grosorSilaba4 = 4

    arrPalabras = ['CASA', 'SAPO', 'CAMA', 'PATO', 'PECERA', 'GORILA']
    arrSilabas = ['CA', 'SA', 'PO', 'MA', 'PA', 'TO', 'PE', 'CE', 'RA', 'GO', 'RI', 'LA', 'SI', 'RO', 'CO']
    arrIndex = [[1, 13, 7, 0], [2, 8, 1, 10], [14, 3, 0, 11], [5, 4, 9, 6], [7, 12, 8, 6], [11, 10, 6, 9]]

    aleatorio = random.randint(0, 5)
    palabraObjetivo = arrPalabras[aleatorio]

    palabra = ''

    aux = ''
    permite = True

    bool = 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)

            if (lmList[8][2] == 180 or lmList[8][2] == 175 or lmList[8][2] == 170 or lmList[8][2] == 185 or lmList[8][
                2] == 190):
                aux = arrSilabas[arrIndex[aleatorio][0]]
                grosorSilaba1 = 6
                grosorSilaba2 = 4
                grosorSilaba3 = 4
                grosorSilaba4 = 4

            if (lmList[8][2] == 280 or lmList[8][2] == 275 or lmList[8][2] == 270 or lmList[8][2] == 285 or lmList[8][
                2] == 290):
                aux = arrSilabas[arrIndex[aleatorio][1]]
                grosorSilaba1 = 4
                grosorSilaba2 = 6
                grosorSilaba3 = 4
                grosorSilaba4 = 4

            if (lmList[8][2] == 380 or lmList[8][2] == 375 or lmList[8][2] == 370 or lmList[8][2] == 385 or lmList[8][
                2] == 390):
                aux = arrSilabas[arrIndex[aleatorio][2]]
                grosorSilaba1 = 4
                grosorSilaba2 = 4
                grosorSilaba3 = 6
                grosorSilaba4 = 4

            if (lmList[8][2] == 480 or lmList[8][2] == 475 or lmList[8][2] == 470 or lmList[8][2] == 485 or lmList[8][
                2] == 490):
                aux = arrSilabas[arrIndex[aleatorio][3]]
                grosorSilaba1 = 4
                grosorSilaba2 = 4
                grosorSilaba3 = 4
                grosorSilaba4 = 6

            if (lmList[8][2] > 10 and lmList[8][2] < 60 and totalFingers == 2):
                wave_obj.play()
                VocalesDesorden()

            # print(lmList[8])

            # print(fingers)

            if (totalFingers != 0 and totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    palabra += aux
                    permite = False

            if (palabraObjetivo != palabra):
                verificarLocal = "si"

            if (palabraObjetivo == palabra):
                cv2.putText(img, f'BIEN HECHO!', (300, 350), cv2.FONT_HERSHEY_PLAIN, 5, (45, 200, 235), 5)
                if (posBar == 150):
                    puntos = 0
                if (verificarLocal == "si"):
                    puntos = puntos + 1
                    totalPos = puntos * cantPuntos
                    posBar = 550 - totalPos
                    message = "si"
                    client.send(message.encode('utf-8'))
                    verificarLocal = "no"

            print('Puntos: ', puntos)

            if (totalFingers == 0):
                if (permite == True):
                    palabra = palabra[:-2]
                    permite = False

            if (totalFingers == 5):
                palabra = ''
                aleatorio = random.randint(0, 5)
                palabraObjetivo = arrPalabras[aleatorio]

        # h, w, c = overlayList[totalFingers - 1].shape
        # img[0:h, 0:w] = overlayList[totalFingers - 1]

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, f'FPS: {int(fps)}', (750, 675), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, f'OBJETIVO: {str(palabraObjetivo)}', (200, 100), cv2.FONT_HERSHEY_PLAIN, 4, (84, 153, 34), 6)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][0]])}', (70, 200), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), grosorSilaba1)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][1]])}', (70, 300), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), grosorSilaba2)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][2]])}', (70, 400), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), grosorSilaba3)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][3]])}', (70, 500), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), grosorSilaba4)
        cv2.putText(img, f'{str(palabra)}', (340, 600), cv2.FONT_HERSHEY_PLAIN, 5, (15, 196, 241), 5)

        cv2.rectangle(img, (800, 10), (950, 60), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Salir', (823, 50), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (844, 144), (906, 556), (60, 76, 231), cv2.FILLED)
        cv2.rectangle(img, (850, 150), (900, 550), (200, 200, 200), cv2.FILLED)
        #rectangulo subida
        cv2.rectangle(img, (850, posBar), (900, 550), (15, 196, 241), cv2.FILLED)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def juegoDEDOScoop():
    global puntos
    global cantPuntos
    global totalPos
    global posBar
    global verificarLocal
    global verificarMulti

    global username
    global cap

    if (username == 'user1'):
        cap = cv2.VideoCapture(2)
    if (username == 'user2'):
        cap = cv2.VideoCapture(3)
    if (username == 'user3'):
        cap = cv2.VideoCapture(1)

    verificarMulti = "si"

    cap.set(3, wCam)
    cap.set(4, hCam)

    pTime = 0

    last_value = 0
    temp_last = 0

    suma_obj = random.randint(1, 5)

    totalFingers = 0
    permite = False

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # print(fingers)
            totalFingers = fingers.count(1)

            if totalFingers == 0:
                last_value += temp_last
            temp_last = totalFingers

            if (lmList[8][2] > 10 and lmList[8][2] < 60 and totalFingers == 2):
                wave_obj.play()
                SumaDedos()

        if (suma_obj != last_value):
            verificarLocal = "si"

        if suma_obj == last_value:
            cv2.putText(img, f'BIEN HECHO!', (300, 400), cv2.FONT_HERSHEY_PLAIN, 5, (45, 200, 235), 5)
            if (posBar == 150):
                puntos = 0
            if (verificarLocal == "si"):
                puntos = puntos + 1
                totalPos = puntos * cantPuntos
                posBar = 550 - totalPos
                message = "si"
                client.send(message.encode('utf-8'))
                verificarLocal = "no"

        if suma_obj < last_value:
            cv2.putText(img, f'UPS! TE ESTAS PASANDO', (240, 400), cv2.FONT_HERSHEY_PLAIN, 3, (6, 111, 229), 3)

        print('Valor Acumulado: ', last_value)
        print('Valor Actual: ', totalFingers)

        print('Puntos: ', puntos)

        h, w, c = overlayList[totalFingers - 1].shape
        img[0:h, 0:w] = overlayList[totalFingers - 1]

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, f'FPS: {int(fps)}', (750, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, f'SUMA: {int(last_value)}', (400, 675), cv2.FONT_HERSHEY_PLAIN, 3, (43, 201, 72), 3)
        cv2.putText(img, f'OBJETIVO: {int(suma_obj)}', (355, 70), cv2.FONT_HERSHEY_PLAIN, 3, (24, 24, 156), 3)

        cv2.rectangle(img, (800, 10), (950, 60), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Salir', (823, 50), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (844, 144), (906, 556), (60, 76, 231), cv2.FILLED)
        cv2.rectangle(img, (850, 150), (900, 550), (200, 200, 200), cv2.FILLED)
        # rectangulo subida
        cv2.rectangle(img, (850, posBar), (900, 550), (15, 196, 241), cv2.FILLED)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


def receive_messages():
    global puntos
    global totalPos
    global posBar
    global verificarMulti
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "@username":
                client.send(username.encode("utf-8"))
            else:
                print(message)

                if (posBar == 150):
                    puntos = 0
                if (verificarMulti == "si"):
                    puntos += 1
                    totalPos = puntos * cantPuntos
                    posBar = 550 - totalPos
                    #verificarMulti = "no"
        except:
            print("An error Ocurred")
            client.close()
            break

def write_message():
    while cap.isOpened():
        message = f"{username}: {input('')}"
        client.send(message.encode('utf-8'))
        #camera()


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
write_thread = threading.Thread(target=write_message)
write_thread.start()
menu_uwu = threading.Thread(target=menu())
menu_uwu.start()