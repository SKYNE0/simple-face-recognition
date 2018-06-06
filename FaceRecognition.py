#_*_encoding:utf-8_*_
"""
@Python -V: 3.X
@SoftWave:Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.6.5
"""

import cv2
from time import sleep
from UserDb import get_all

def face_recognition():
    """
    :return:
    """
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    font = cv2.FONT_HERSHEY_SIMPLEX

    names = dict(get_all())

    cam = cv2.VideoCapture(0)
    cam.set(3, 960)
    cam.set(4, 640)

    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        sleep(0.05)

        ret, img =cam.read()

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # print('whois',id)
            confidence = 100 - round(confidence)
            if 70 < confidence:
                name = names[id]
                confidence = "  {0}%".format(confidence)

            elif 40 < confidence < 70:
                name = "MayBe " + names[id]
                confidence = "  {0}%".format(confidence)
            else:
                name = "Alien"
                confidence = "  {0}%".format(0)

            cv2.putText(img, name, (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

        cv2.imshow('camera',img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
