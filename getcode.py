import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
from PIL import Image  #安装pillow
import colorsys
from aip import AipOcr  #安装baidu-aip


def login():
    mydriver = webdriver.Chrome()
    mydriver.get("http://sunshine.olading.com:18390/#/login")
    time.sleep(2)
    #切换到企业登录
    mydriver.find_element_by_xpath('//*[@id="tab-1"]').click()
    time.sleep(4)
    #
    # initimgpath=getImg(mydriver)
    # grayimgpath=getGray(initimgpath)
    # catcha=getResult(grayimgpath)

    catcha=getresult(mydriver)
    mydriver.find_element_by_xpath(
        "/html/body/div/section/section/main/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input").send_keys(
        'user_1705')
    mydriver.find_element_by_xpath(
        '/html/body/div/section/section/main/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/input').send_keys(
        'lanmao123')
    mydriver.find_element_by_xpath(
        '/html/body/div/section/section/main/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/div[1]/input').send_keys(
        catcha)
    mydriver.find_element_by_xpath(
        '/html/body/div/section/section/main/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/button').click()
    time.sleep(2)

    mydriver.close()


# def getImg(driver):
#
#     data = driver.page_source
#
#     soup = BeautifulSoup(data, 'html.parser')
#     gg = soup.select('img')
#     for i in gg:
#         if str(i['src']).count('.jpg') >= 1:
#             continue
#         else:
#             imgurl = i['src']
#             newulr = 'http://sunshine.olading.com:18390' + imgurl
#             print(newulr)
#             print("开始下载图片：" + newulr + "\r\n")
#             try:
#                 pic = requests.get(newulr, timeout=10)
#             except requests.exceptions.ConnectionError:
#                 print('图片无法下载')
#                 continue
#             # 保存图片路径
#             # mm=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#             dir = os.getcwd()+'/getImage/initimg.jpg'
#             fp = open(dir, 'wb')
#             fp.write(pic.content)
#
#             fp.close()
#             return dir
#
#
# def getGray(path):
#     # # 输入文件
#     # filename = path
#
#     # 目标色值
#     # Hue 为 0 代表红色，120 代表绿色，240 代表蓝色。我们可以自定义 0-355 这 360 个数值，实现不同的色调转换
#
#
#     # 读入图片，转化为 RGB 色值
#     image = Image.open(path).convert('RGB')
#
#     # 将 RGB 色值分离
#     image.load()
#     r, g, b = image.split()
#
#     result_r, result_g, result_b = [], [], []
#
#     # 依次对每个像素点进行处理
#     for pixel_r, pixel_g, pixel_b in zip(r.getdata(), g.getdata(), b.getdata()):
#         # 转为 HSV 色值
#
#         h, s, v = colorsys.rgb_to_hsv(pixel_r / 255., pixel_b / 255., pixel_b / 255.)
#
#         # 转回 RGB 色系
#         rgb = colorsys.hsv_to_rgb(h, s, s)
#         # rgb = colorsys.hsv_to_rgb(s, 0, s)
#
#         pixel_r, pixel_g, pixel_b = [int(x * 255.) for x in rgb]
#
#         # 每个像素点结果保存
#         result_r.append(pixel_r)
#         result_g.append(pixel_g)
#         result_b.append(pixel_b)
#     s
#     r.putdata(result_r)
#     g.putdata(result_g)
#     b.putdata(result_b)
#
#     # 合并图片
#     image = Image.merge('RGB', (r, g, b))
#
#     # 转为灰度
#     image = image.convert('L')  # 转化为灰度图
#     # 输出图片
#     dir=os.getcwd()+'/getresultimg/resultimg.jpg'
#     image.save(dir)
#     return dir
#
# def getResult(picturepath):
#
#
#     App_ID = '18281215'
#     API_Key = 'LaPVmmTzWM7ykVeGqzWWh2s4'
#     Secret_Key = 'fnvu8AGOBzT2aFdDcFVlmDCSpCaUNDsV'
#
#     client = AipOcr(App_ID, API_Key, Secret_Key)
#
#     # img=Image.open('yzoutput1.jpg')
#
#     # 读取图片
#     def get_file_content(filePath):
#         with open(filePath, 'rb') as fp:
#             return fp.read()
#
#     img = get_file_content(picturepath)
#
#
#     # 定义参数变量
#     myoptions = {
#         # 定义图像方向
#         'detect_direction': 'true',
#         # 识别语言类型，默认为'CHN_ENG'中英文混合
#         'language_type': 'CHN_ENG',
#     }
#
#     result = client.general(img, options=myoptions)
#
#     for word in result['words_result']:
#         print(f"验证码是{word['words']}")
#     return word['words']
#
# login()

def getresult(driver):

    #获取页面上图片路径，并下载到本地
    data = driver.page_source

    soup = BeautifulSoup(data, 'html.parser')
    gg = soup.select('img')
    for i in gg:
        if str(i['src']).count('.jpg') >= 1:
            continue
        else:
            imgurl = i['src']
            newulr = 'http://sunshine.olading.com:18390' + imgurl
            print(newulr)
            print("开始下载图片：" + newulr + "\r\n")
            try:
                pic = requests.get(newulr, timeout=10)
            except requests.exceptions.ConnectionError:
                print('图片无法下载')
                continue
            # 保存图片路径
            # mm=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            # dir = os.getcwd() + '/getImage/initimg.jpg'
            dir1='initimg.jpg'
            fp = open(dir1, 'wb')
            fp.write(pic.content)

            fp.close()

    #处理图片，便于识别
    # Hue 为 0 代表红色，120 代表绿色，240 代表蓝色。我们可以自定义 0-355 这 360 个数值，实现不同的色调转换

    # 读入图片，转化为 RGB 色值
    image = Image.open(dir1).convert('RGB')

    # 将 RGB 色值分离
    image.load()
    r, g, b = image.split()

    result_r, result_g, result_b = [], [], []

    # 依次对每个像素点进行处理
    for pixel_r, pixel_g, pixel_b in zip(r.getdata(), g.getdata(), b.getdata()):
        # 转为 HSV 色值

        h, s, v = colorsys.rgb_to_hsv(pixel_r / 255., pixel_b / 255., pixel_b / 255.)

        # 转回 RGB 色系
        rgb = colorsys.hsv_to_rgb(h, s, s)
        # rgb = colorsys.hsv_to_rgb(s, 0, s)

        pixel_r, pixel_g, pixel_b = [int(x * 255.) for x in rgb]

        # 每个像素点结果保存
        result_r.append(pixel_r)
        result_g.append(pixel_g)
        result_b.append(pixel_b)

    r.putdata(result_r)
    g.putdata(result_g)
    b.putdata(result_b)

    # 合并图片
    image = Image.merge('RGB', (r, g, b))

    # 转为灰度
    image = image.convert('L')  # 转化为灰度图
    # 输出图片
    # dir = os.getcwd() + '/getresultimg/resultimg.jpg'
    dir2='resultimg.jpg'
    image.save(dir2)


    #识别图形验证码，获取结果
    App_ID = '18281215'
    API_Key = 'LaPVmmTzWM7ykVeGqzWWh2s4'
    Secret_Key = 'fnvu8AGOBzT2aFdDcFVlmDCSpCaUNDsV'

    client = AipOcr(App_ID, API_Key, Secret_Key)

    # img=Image.open('yzoutput1.jpg')

    # 读取图片
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    img = get_file_content(dir2)

    # 定义参数变量
    myoptions = {
        # 定义图像方向
        'detect_direction': 'true',
        # 识别语言类型，默认为'CHN_ENG'中英文混合
        'language_type': 'CHN_ENG',
    }

    result = client.general(img, options=myoptions)

    for word in result['words_result']:
        print(f"验证码是{word['words']}")
    return word['words']

login()
