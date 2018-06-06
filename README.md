### 使用

#### 请参照requirements.txt中依赖的库,自行安装。建议使用虚环境。

#### 最难安装的是OpenCV，需要下载源码编译安装，请参考这篇文章[Raspbian Stretch: Install OpenCV 3 + Python on your Raspberry Pi](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/)

#### 需要注意的是树莓派系统有Stretch，Jessie，Wheezy之分，另外，强烈建议更换国内的软件源。

### 其他
#### 人脸识别的精度不是很高,存在很多问题,有很多优化的地方.

#### 自己主要依照文章[用树莓派实现实时的人脸检测](http://shumeipai.nxez.com/2018/03/09/real-time-face-recognition-an-end-to-end-project-with-raspberry-pi.html)来做的

#### 该文章是翻译的一篇英文文章,原作者的仓库地址为[Mjrovai](https://github.com/Mjrovai/OpenCV-Face-Recognition)

#### 自己也是按照上面是文章做出的,自己在原作者的基础上增加了小改进.

```
1. 增加自动创建所需目录的部分
2. 各部分封装进函数由main.py来调用
3. 增加数据库来存储用户信息,原作者使用列表来储存
4. 连接成一个整体,从采集,训练,到识别
```
#### 自己也看了其他的人脸识别的文章,下面推荐一些文章或者仓库地址

#### [基于Python的开源人脸识别库：离线识别率高达99.38%](基于Python的开源人脸识别库：离线识别率高达99.38%)

#### [计算机视觉库/人脸识别 - 开源软件库 - 开源中国社区](https://www.oschina.net/project/tag/316/opencv)

#### [DFace人工智能开源免费的人脸识别科技](https://github.com/kuaikuaikim/DFace)

### TODO

#### 自己还在看相关的技术文章，觉得face_recognition很不错。

#### 自己再慢慢研究下，争取提高识别精度，配合其他模块做个简单的人脸识别应用。