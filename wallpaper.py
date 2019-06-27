"""
程序功能：抓取必应每日一图，设置为桌面壁纸
"""

import urllib.request
import requests         
import os.path
import ctypes
import datetime
import time
import re
from bs4 import BeautifulSoup
import msvcrt
import random


def save_img(img_url,filepath , dirname):
    #保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print ('文件夹',dirname,'不存在，重新建立')
            #os.mkdir(dirname)
            os.makedirs(dirname)
        urllib.request.urlretrieve(img_url,filepath)
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)
    print("Save", filepath, "successfully!")

# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)       
    img_url = r.url # 得到图片文件的网址
    print('img_url:', img_url)
    return img_url

def get_img_name(url):
    respnse = requests.get(url)
    try:
        if respnse.status_code == 200:
            html = respnse.text
            soup = BeautifulSoup(html,'lxml')
            classname = soup.find(class_='sc_light')
            name = classname['title']
            rightname = re.sub('[\/:*?"<>|]','-',name)
            return rightname
    except:
        dir = 'H:\\Python\\wallpaper'
        pathdir = os.listdir(dir)
        sample = random.sample(pathdir)
        set_img_as_wallpaper(sample)
        print('\n\n\n点击任何按键结束进程')
        while(True):
            if ord(msvcrt.getch()):
                break


# 设置图片绝对路径 filepath 所指向的图片为壁纸
def set_img_as_wallpaper(filepath):
    print(filepath)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
    print('\n\n' + str.replace(filepath,'H:\\Python\\wallpaper\\',''))


def set_random_img_as_wallpaper():
    dir = 'H:\\Python\\wallpaper'
    pathdir = os.listdir(dir)
    sample = random.sample(pathdir,1)[0]
    set_img_as_wallpaper(os.path.join(dir, sample))

def waitKeyInput():
    print('\n\n\n点击任何按键结束进程')
    while(True):
        if ord(msvcrt.getch()):
            break

def waitKeyStart():
    print('\n点击任何按键开始进程')
    while(True):
        if ord(msvcrt.getch()):
            break

def main():
    try:
        #pdb.set_trace()
        #time.sleep(5)
        #waitKeyStart()
        dirname = 'H:\\Python\\wallpaper'#用于存放壁纸的目录
        url = 'https://cn.bing.com/'
        picname = get_img_name(url)
        data = datetime.date.today()
        filepath = "H:\\Python\\wallpaper\\"+str(data)+ picname + ".png"       # 图片要被保存在的位置
        img_url = get_img_url()
        save_img(img_url, filepath , dirname)   # 图片文件的的路径
        set_img_as_wallpaper(filepath)
        waitKeyInput()
    except:
        set_random_img_as_wallpaper()
        waitKeyInput()

if __name__ == '__main__':
    main()