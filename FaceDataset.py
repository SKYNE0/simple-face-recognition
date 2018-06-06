#_*_encoding:utf-8_*_
"""
@Python -V: 3.X
@SoftWave:Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.6.5
"""

import cv2

from UserDb import user_id

def face_dataset(user_path, name):
    """
    :param user_path: 用户图片的存储路径
    :param name: 用户名
    :return:
    """
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    count = 0

    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1

            # 查询数据返回用户对应的ID
            id = user_id(name)

            # 存储摄像头根据分类器捕获到的灰度图像
            cv2.imwrite(user_path + str(id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            font = cv2.FONT_HERSHEY_SIMPLEX

            # 可以写入文本到显示画面,不能是中文
            cv2.putText(img, "Look At The Camera", (162, 40), font, 1, (255, 255, 255), 2)

            cv2.imshow('image', img)

        # 监听键盘事件,ESC退出
        k = cv2.waitKey(100) & 0xff
        if k == 27:
            break
        elif count >= 30:
             break
    # 关闭画面
    cam.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    face_dataset('dataset/sdasdas','asdas')

