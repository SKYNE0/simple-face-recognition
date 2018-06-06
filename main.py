#_*_encoding:utf-8_*_
"""
@Python -V: 3.X
@SoftWave:Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.6.5
"""

import os
from FaceDataset import face_dataset
from FaceTraining import face_training
from FaceRecognition import face_recognition
from UserDb import insert_name

def is_dir(path):
    """
    :param path: 需要判断是否存在的目录名
    :return: Bool
    """
    if not os.path.exists('dataset'):
        os.mkdir('dataset')

    if not os.path.exists(path):
        os.mkdir(path)
        return True
    else:
        return None

def main():
    """
    :return:
    """
    flag = input("\n请您选择信息采集模式(y) OR 识别模式(n):")

    if flag in ['y','Y', 'yes']:
        face_name = input('\n请输入你的名字:')

        insert_name(face_name)

        user_path = 'dataset/' + face_name + '/'

        is_dir(user_path)

        print("\n正在提取特征信息，请您稍等！")
        print("\n信息采集中，请您稍等！")
        face_dataset(user_path, face_name)

        print("\n正在提取特征信息，请您稍等！")
        face_training()

        print("\nOK，现在来试试效果吧！")
        print("\n友情提示，退出请按ESC键!")
        face_recognition()
        print("\n程序正常退出，感谢亲的使用!")
    else:
        print("\n正在启用识别模式，请稍等！")
        print("\n友情提示，退出请按ESC键!")
        face_recognition()
        print("\n程序正常退出，感谢亲的使用!")


if __name__ == '__main__':
    main()