#_*_encoding:utf-8_*_
"""
@Python -V: 3.X
@SoftWave:Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.6.5
"""

import cv2
import numpy as np
from PIL import Image
import os

def getImagesAndLabels(detector):
    """
    :param detector: CV里的一个检测器对象,可以根据分类器来检测是否有我们需要的图像,比如:脸,鼻子之类的
    :return:
    """
    # 图片路径列表,需要获取全部用户的图片路径
    imagePaths = []

    for dir in os.listdir('dataset'):
        for path in os.listdir('dataset' + '/' + dir):
            path = 'dataset' + '/' + dir + '/' + path
            imagePaths.append(path)

    # imagePaths = [os.path.join(path,f) for f in os.listdir('dataset')]
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:
        # 以灰度模式读取用户图片
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')

        # 获取dataset/JIAN/10.1.jpg中10,也就是用户ID
        id = int(os.path.split(imagePath)[-1].split('.')[0])
        # id = user_id(name)
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids


def face_training():
    """
    :return:
    """
    # 判断是否存在trainer目录不存在就会创建
    if not os.path.exists('trainer'):
        os.mkdir('trainer')

    # 创建识别器
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # 创建检测器
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    faces,ids = getImagesAndLabels(detector)

    # 用识别器训练获取到的信息
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer/trainer.yml')


if __name__ == '__main__':
    face_training()
